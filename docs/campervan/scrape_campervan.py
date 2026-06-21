#!/usr/bin/env python3
"""
Scrape een phpBB3-forumtopic naar MkDocs-Markdown + lokale plaatjes.

Gebruik:
    pip install requests beautifulsoup4 markdownify
    python scrape_campervan.py

Resultaat:
    ./campervan/
        mkdocs.yml
        docs/
            index.md
            campervan.md
            assets/   (alle gedownloade plaatjes)

Daarna:
    pip install mkdocs-material
    cd campervan
    mkdocs serve        # lokaal bekijken op http://127.0.0.1:8000
"""

import os
import re
import time
import sys
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# ──────────────────────────────────────────────────────────────────────────
# CONFIG — pas hier zo nodig aan
# ──────────────────────────────────────────────────────────────────────────

# Topic-URL ZONDER &start=... (de sid mag erin blijven staan)
BASE_URL = "https://www.weetjewel.nl/phpbb3/viewtopic.php?t=65821"

# Forum-basis (waar ucp.php / index.php onder staan)
FORUM_BASE = "https://www.weetjewel.nl/phpbb3"
LOGIN_URL = FORUM_BASE + "/ucp.php?mode=login"

# Inloggen via het script (aanbevolen): phpBB bindt sessies aan IP/User-Agent,
# dus cookies uit je browser plakken werkt meestal niet vanuit een script.
# Het script logt zelf in en krijgt zo een geldige sessie op dit IP.
#
# Vul je gebruikersnaam hier in (of via env-var WEETJEWEL_USER).
# Het WACHTWOORD nooit hardcoden — geef het mee via env-var WEETJEWEL_PASS:
#     WEETJEWEL_USER=... WEETJEWEL_PASS=... uv run ... scrape_campervan.py
FORUM_USER = os.environ.get("WEETJEWEL_USER", "")
FORUM_PASS = os.environ.get("WEETJEWEL_PASS", "")

# Aantal posts per pagina (phpBB standaard = 15; soms 10 of 25)
POSTS_PER_PAGE = 15

# Cookies: nodig om bijlagen (download/file.php) te kunnen ophalen. Zonder
# geldige login krijg je 403's en SVG-placeholders i.p.v. echte foto's.
#
# Je hoeft hieronder NIETS te plakken. Het script leest cookies bij voorkeur
# uit een los bestand "cookies.txt" naast dit script. Maak dat bestand zo:
#
#   1. Log in op het forum in je browser.
#   2. F12 > Application/Storage > Cookies > https://www.weetjewel.nl
#   3. Kopieer de waarden en zet ze regel-voor-regel in cookies.txt als:
#        weetjewel_forum_u=15453
#        weetjewel_forum_k=...
#        weetjewel_forum_sid=...
#      (Of plak de hele Cookie-header op één regel; beide werkt.)
#
# Alternatief: zet ze in de env-var WEETJEWEL_COOKIES (zelfde formaat).
# De hardcoded fallback hieronder laat je leeg.
COOKIES = {}

COOKIES_FILE = "cookies.txt"


def _parse_cookie_text(text):
    """Lees cookies uit 'naam=waarde' regels of een 'a=1; b=2'-header."""
    jar = {}
    # ondersteun zowel newline-gescheiden als '; '-gescheiden
    parts = re.split(r"[;\n\r]+", text)
    for part in parts:
        part = part.strip()
        if not part or part.startswith("#") or "=" not in part:
            continue
        name, _, value = part.partition("=")
        name, value = name.strip(), value.strip()
        if name and value:
            jar[name] = value
    return jar


def load_cookies():
    """Cookies uit env-var, dan cookies.txt, dan de hardcoded COOKIES."""
    env = os.environ.get("WEETJEWEL_COOKIES")
    if env:
        jar = _parse_cookie_text(env)
        if jar:
            print(f"Cookies geladen uit env-var WEETJEWEL_COOKIES ({len(jar)} stuks).")
            return jar

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), COOKIES_FILE)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            jar = _parse_cookie_text(f.read())
        if jar:
            print(f"Cookies geladen uit {COOKIES_FILE} ({len(jar)} stuks).")
            return jar
        print(f"[!] {COOKIES_FILE} bestaat maar bevat geen geldige cookies.")

    if COOKIES:
        print(f"Cookies geladen uit het script ({len(COOKIES)} stuks).")
        return dict(COOKIES)

    print("[!] Geen cookies gevonden — bijlagen zullen waarschijnlijk falen (403).")
    return {}

# Wacht tussen requests (wees netjes tegen de server)
DELAY_SECONDS = 1.0

# Plaatjes met deze patronen in de URL worden overgeslagen (smileys, avatars, icons)
SKIP_IMG_PATTERNS = [
    "/images/smilies/",
    "/styles/",
    "/images/avatars/",
    "avatar",
    "smiley",
    "/icon",
]

OUTPUT_DIR = "campervan"
DOCS_DIR = os.path.join(OUTPUT_DIR, "docs")
ASSETS_DIR = os.path.join(DOCS_DIR, "assets")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

# ──────────────────────────────────────────────────────────────────────────

session = requests.Session()
session.headers.update(HEADERS)


def _is_logged_in_html(html):
    """phpBB toont een 'Afmelden'/logout-link als je ingelogd bent."""
    return bool(re.search(r"mode=logout|Afmelden|Uitloggen|Logout", html))


def _login_once(username, password):
    """Eén login-poging met verse form-tokens. Geeft (ok, foutmelding) terug."""
    # schone cookie-jar: phpBB geeft dan verse tokens + sid die bij elkaar horen
    session.cookies.clear()

    r = session.get(LOGIN_URL, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    form = next((f for f in soup.find_all("form")
                 if f.find("input", {"type": "password"})), None)
    if form is None:
        return False, "login-formulier niet gevonden"

    # Neem hidden velden over (creation_time, form_token, redirect, ...) als
    # lijst van paren, zodat dubbele velden (bv. redirect) bewaard blijven.
    # LET OP: het 'sid'-veld moet NIET mee in de body — phpBB's form_token-
    # validatie faalt dan ("formulier ongeldig"). De sid zit al in cookie+URL.
    pairs = []
    for inp in form.find_all("input"):
        name = inp.get("name")
        if name and name not in ("username", "password", "login", "sid"):
            pairs.append((name, inp.get("value", "")))
    pairs += [
        ("username", username),
        ("password", password),
        ("login", "Aanmelden"),
        ("autologin", "on"),   # vraag een blijvende sessie (_k cookie)
    ]

    action = (form.get("action") or LOGIN_URL).replace("&amp;", "&")
    post_url = urljoin(LOGIN_URL, action)

    resp = session.post(post_url, data=pairs, timeout=30,
                        headers={"Referer": LOGIN_URL})
    resp.raise_for_status()

    # verifieer met een echte topic-fetch
    check = session.get(BASE_URL, timeout=30)
    if _is_logged_in_html(check.text) and "aangemeld bent om dit forum" not in check.text:
        return True, ""

    err = BeautifulSoup(resp.text, "html.parser").select_one(".error, .message")
    msg = err.get_text(" ", strip=True)[:200] if err else "onbekende reden"
    return False, msg


def login(username, password, attempts=4):
    """Log in op phpBB. phpBB throttelt snelle login-pogingen en geeft dan
    'formulier ongeldig' terug; daarom proberen we het een paar keer met een
    oplopende pauze (verse tokens per poging)."""
    print(f"Inloggen als '{username}' ...")
    for i in range(1, attempts + 1):
        ok, msg = _login_once(username, password)
        if ok:
            print("    Login gelukt.")
            return True
        # "formulier ongeldig" = throttling -> even wachten en opnieuw
        wait = 3 * i
        if i < attempts:
            print(f"    poging {i} mislukt ({msg}); {wait}s wachten en opnieuw...")
            time.sleep(wait)
        else:
            print(f"[!] Login mislukt na {attempts} pogingen: {msg}")
    return False


def get_soup(url):
    r = session.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding  # voorkomt rare tekens (ë, ï, etc.)
    return BeautifulSoup(r.text, "html.parser")


def find_posts(soup):
    """Probeer meerdere selectors; phpBB-thema's verschillen."""
    for selector in ["div.post", "div.postbody", "div[id^='p']"]:
        found = soup.select(selector)
        # filter op containers die echt een postbody bevatten
        real = [p for p in found if p.select_one(".content, .postbody, .post-content")]
        if real:
            return real
    return []


def extract_author(post):
    for sel in [".author strong", ".author a", ".username", ".username-coloured",
                ".postauthor", ".author"]:
        el = post.select_one(sel)
        if el:
            txt = el.get_text(strip=True)
            # knip "door" / "Bericht door" weg
            txt = re.sub(r"^(Bericht\s+)?door\s+", "", txt, flags=re.I)
            if txt:
                return txt
    return "Onbekend"


def extract_date(post):
    for sel in [".author time", "time", ".postdetails", ".author"]:
        el = post.select_one(sel)
        if el:
            t = el.get("datetime") or el.get_text(" ", strip=True)
            m = re.search(r"\d{1,2}[-/ ]\w+[-/ ]\d{4}|\d{4}-\d{2}-\d{2}", t)
            if m:
                return m.group(0)
    return ""


def extract_body(post):
    el = post.select_one(".content, .postbody .content, .post-content, .postbody")
    return el


def should_skip_img(src):
    low = src.lower()
    return any(p in low for p in SKIP_IMG_PATTERNS)


def download_images(body, post_idx):
    """Download plaatjes lokaal, herschrijf src naar assets/..."""
    for i, img in enumerate(body.find_all("img")):
        src = img.get("src") or img.get("data-src")
        if not src:
            continue
        if should_skip_img(src):
            img.decompose()  # smiley/avatar weg
            continue

        full = urljoin(BASE_URL, src)
        path = urlparse(full).path
        ext = os.path.splitext(path)[1].lower()
        if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"):
            ext = ".jpg"
        fname = f"post{post_idx:03d}_img{i:02d}{ext}"
        dest = os.path.join(ASSETS_DIR, fname)

        try:
            # phpBB blokkeert bijlage-downloads zonder geldige Referer
            resp = session.get(full, timeout=30, headers={"Referer": BASE_URL})
            resp.raise_for_status()

            content = resp.content
            ctype = resp.headers.get("Content-Type", "").lower()

            # phpBB serveert een SVG-placeholder als je geen toegang hebt
            # tot de bijlage (niet ingelogd / verlopen sessie). Detecteer dat.
            head = content[:200].lstrip().lower()
            if "svg" in ctype or head.startswith(b"<svg") or head.startswith(b"<?xml"):
                print(f"    [!] geen echte afbeelding (SVG-placeholder), "
                      f"waarschijnlijk niet ingelogd: {full}")
                img.decompose()
                time.sleep(0.2)
                continue

            with open(dest, "wb") as f:
                f.write(content)
            img["src"] = f"assets/{fname}"
            # ruim attributen op die markdownify in de war brengen
            for attr in ["data-src", "srcset", "width", "height", "class", "style"]:
                img.attrs.pop(attr, None)
            print(f"    afbeelding: {fname}")
        except Exception as e:
            print(f"    [!] kon afbeelding niet ophalen: {full} ({e})")
            img.decompose()
        time.sleep(0.2)


def clean_captions(markdown):
    """phpBB bijlagen worden door markdownify omgezet naar definitie-lijsten
    (':   ...'-regels) en 'Bijlagen'-labels. De hoofdsite heeft de def_list/
    md_in_html extensies niet, dus die regels zouden als letterlijke ':'-tekst
    tonen. Hier zetten we ze om naar gewone Markdown die overal werkt.
    """
    lines = markdown.split("\n")
    out = []
    for line in lines:
        stripped = line.strip()

        # 'Bijlagen'-kopje boven een lijst bijlagen: weglaten
        if stripped == "Bijlagen":
            continue

        # ':   [![..]](..)' of ':   ![..](..)' -> losse (gelinkte) afbeelding
        if stripped.startswith(":") :
            content = stripped.lstrip(":").strip()
            if content.startswith(("![", "[![")):
                out.append(content)
                continue
            # ':   *bijschrift*' -> cursief bijschrift op eigen regel
            if content.startswith("*") and content.endswith("*") and len(content) > 2:
                out.append(content)
                continue
            # ':   bestandsnaam.jpg (12 KiB) 34 keer bekeken' -> ruis, weglaten
            if re.search(r"\(\d[\d.,]*\s*[KMG]i?B\)", content) or "keer bekeken" in content:
                continue
            # overige ':   tekst' -> gewone tekst
            if content:
                out.append(content)
            continue

        out.append(line)

    cleaned = "\n".join(out)
    # eventueel ontstane drievoudige lege regels weer terugbrengen
    return re.sub(r"\n{3,}", "\n\n", cleaned)


def absolutize_links(body):
    """Maak relatieve forum-links absoluut richting weetjewel.

    Lokale afbeeldingen (assets/...) en links die al absoluut zijn
    (http/https/mailto/#) blijven ongemoeid. phpBB gebruikt './...' en
    '/phpbb3/...' relatieve hrefs; die wijzen naar het forum.
    """
    for a in body.find_all("a"):
        href = a.get("href")
        if not href:
            continue
        low = href.lower()
        # al absoluut of speciaal -> laten staan
        if low.startswith(("http://", "https://", "mailto:", "#", "tel:")):
            continue
        # lokale assets nooit aanraken
        if href.startswith("assets/"):
            continue
        a["href"] = urljoin(BASE_URL, href)

    # vangnet: resterende <img> die niet lokaal zijn (bv. niet-gedownloade)
    # ook absoluut maken, zodat ze in elk geval vanaf het forum laden.
    for img in body.find_all("img"):
        src = img.get("src")
        if not src or src.startswith(("assets/", "http://", "https://", "data:")):
            continue
        img["src"] = urljoin(BASE_URL, src)


def authenticate():
    """Probeer in te loggen; val terug op cookies als dat niet kan."""
    if FORUM_USER and FORUM_PASS:
        try:
            if login(FORUM_USER, FORUM_PASS):
                return
            print("[!] Inloggen mislukt — val terug op cookies (indien aanwezig).")
        except Exception as e:
            print(f"[!] Fout bij inloggen: {e} — val terug op cookies.")

    jar = load_cookies()
    if jar:
        session.cookies.update(jar)

    if not (FORUM_USER and FORUM_PASS) and not jar:
        print("[!] Geen login én geen cookies. Zet WEETJEWEL_USER + WEETJEWEL_PASS")
        print("    in je omgeving, bv.:")
        print("    WEETJEWEL_USER=jouwnaam WEETJEWEL_PASS=geheim \\")
        print("        uv run --with requests,beautifulsoup4,markdownify scrape_campervan.py")


def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)
    authenticate()

    all_posts = []
    start = 0
    page = 1

    while True:
        url = f"{BASE_URL}&start={start}"
        print(f"\nPagina {page}: {url}")
        try:
            soup = get_soup(url)
        except Exception as e:
            print(f"[!] fout bij ophalen pagina: {e}")
            break

        # topic-titel van de eerste pagina
        if page == 1:
            title_el = soup.select_one("h2 a, h2, .topic-title")
            global TOPIC_TITLE
            TOPIC_TITLE = title_el.get_text(strip=True) if title_el else "Camperbouw"

        posts = find_posts(soup)
        if not posts:
            if page == 1:
                print("[!] Geen posts gevonden. Mogelijke oorzaken:")
                print("    - login vereist -> vul COOKIES in bovenaan het script")
                print("    - andere CSS-selectors -> bekijk de HTML (F12) en pas find_posts() aan")
            break

        print(f"    {len(posts)} posts gevonden")
        for post in posts:
            all_posts.append({
                "author": extract_author(post),
                "date": extract_date(post),
                "body": extract_body(post),
            })

        # stoppen als deze pagina minder dan een volle pagina had
        if len(posts) < POSTS_PER_PAGE:
            break

        start += POSTS_PER_PAGE
        page += 1
        time.sleep(DELAY_SECONDS)

    if not all_posts:
        print("\nNiets opgehaald. Stoppen.")
        sys.exit(1)

    print(f"\nTotaal {len(all_posts)} posts. Markdown schrijven...")

    md_path = os.path.join(DOCS_DIR, "campervan.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# {TOPIC_TITLE}\n\n")
        f.write(f"> Gearchiveerd vanaf [het originele forumtopic]({BASE_URL}).\n\n")
        for idx, post in enumerate(all_posts):
            if post["body"] is None:
                continue
            download_images(post["body"], idx)
            absolutize_links(post["body"])
            heading = post["author"]
            if post["date"]:
                heading += f" — {post['date']}"
            f.write(f"\n\n## {heading}\n\n")
            markdown = md(str(post["body"]), heading_style="ATX", strip=["a"] if False else None)
            markdown = clean_captions(markdown)
            # opschonen: meer dan 2 lege regels terugbrengen naar 2
            markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()
            f.write(markdown + "\n")

    # index.md
    with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write(f"# {TOPIC_TITLE}\n\n")
        f.write("Welkom op het gearchiveerde bouwverslag van mijn camper.\n\n")
        f.write("Ga naar [De bouw](campervan.md) om te beginnen.\n")

    # mkdocs.yml
    with open(os.path.join(OUTPUT_DIR, "mkdocs.yml"), "w", encoding="utf-8") as f:
        f.write(f"""site_name: {TOPIC_TITLE}
site_url: https://moonmodules.org/campervan/
theme:
  name: material
  features:
    - navigation.top
    - content.code.copy
  palette:
    - scheme: default
      primary: teal
plugins:
  - search
  - glightbox        # klik op foto's voor lightbox
markdown_extensions:
  - attr_list
  - md_in_html
nav:
  - Home: index.md
  - De bouw: campervan.md
""")

    print(f"\nKlaar! Output staat in ./{OUTPUT_DIR}/")
    print("\nVolgende stappen:")
    print("    pip install mkdocs-material mkdocs-glightbox")
    print(f"    cd {OUTPUT_DIR}")
    print("    mkdocs serve")


TOPIC_TITLE = "Camperbouw"

if __name__ == "__main__":
    main()
