# campervan forum scraper

Throwaway script that archives a phpBB3 forum topic (the weetjewel.nl T5 camper
build thread) into MkDocs-flavoured Markdown + locally downloaded images. Kept
for future reference — the value is in the phpBB-specific gotchas below, not the
code quality.

## What it does

- Walks every page of the topic (`viewtopic.php?...&start=N`).
- Extracts author, date and body per post; converts HTML → Markdown.
- Downloads inline attachments into `docs/assets/` and rewrites `src` to local paths.
- Rewrites relative forum links (`./viewtopic.php`, `./download/file.php`, …) to
  absolute `https://www.weetjewel.nl/phpbb3/...` URLs; leaves external links and
  local `assets/` alone.
- Cleans up phpBB attachment captions so they render without extra Markdown
  extensions (see "Captions" below).

## Usage

```sh
WEETJEWEL_USER='yourname' WEETJEWEL_PASS='yourpassword' \
  uv run --with requests,beautifulsoup4,markdownify scrape_campervan.py
```

Output lands in `./campervan/` (`mkdocs.yml`, `docs/campervan.md`, `docs/assets/`).

The password is read from the `WEETJEWEL_PASS` env var only — never hardcode it.
`WEETJEWEL_USER` / `WEETJEWEL_PASS` are your normal forum login (the username you
log in with, not the numeric user id).

## The gotchas (why this took several tries)

These are phpBB-specific and not obvious from the HTML. They are the reason this
file is worth keeping.

1. **Copying browser cookies does NOT work.** phpBB binds a session to the
   browser's IP / User-Agent. A `weetjewel_forum_sid` that is valid in your
   browser gets rejected from a script on a different connection — phpBB silently
   resets you to guest (`weetjewel_forum_u=1`) and serves a "you must be logged
   in" page. So the script logs in itself to get a session valid for *its* IP.
   (A `cookies.txt` fallback exists but is effectively dead for this reason.)

2. **On login, the hidden `sid` form field must NOT be POSTed.** phpBB's
   `form_token` validation fails with "Het verstuurde formulier is ongeldig"
   ("the submitted form is invalid") if you echo the `sid` back in the body. The
   sid is already in the cookie + URL; sending it again breaks the token check.
   Drop it; keep `creation_time`, `form_token`, and the (duplicate) `redirect`
   fields.

3. **phpBB throttles rapid logins.** After a few quick login attempts it returns
   the same "form invalid" error regardless of correctness. The script retries a
   few times with an increasing delay and a fresh cookie jar + fresh tokens per
   attempt. If it fails repeatedly, wait ~30s and rerun.

4. **Attachment downloads need a `Referer` header**, otherwise `download/file.php`
   returns 403 Forbidden (anti-hotlink protection).

5. **phpBB serves an SVG placeholder** instead of the real image when you lack
   access (not logged in / expired session). The script detects SVG content/
   content-type and skips it rather than saving a 1 KB "image". Emoji are also
   SVGs (twemoji CDN) and get skipped the same way — that's expected.

## Captions

phpBB attachment blocks come through markdownify as definition lists
(`:   ...` lines) and `Bijlagen` labels, which need the `def_list` / `md_in_html`
Markdown extensions to render. The target MkDocs site doesn't enable those (and
enabling them site-wide would affect every other page), so `clean_captions()`
rewrites those lines into plain images / italic captions that render anywhere.

## Files

- `scrape_campervan.py` — the script.
- `cookies.txt.example` — template for the (mostly dead) cookie fallback.
- `cookies.txt` — **never commit**; holds a live session + user id. Gitignored.

## Deploying the output

The generated `docs/campervan.md` was copied into the moonmodules.org MkDocs site
as `docs/campervan/index.md`, with `docs/assets/` copied alongside as
`docs/campervan/assets/`. It is an *unlisted* page (not in `nav`), reachable at
`https://moonmodules.org/campervan/` but hidden from the navigation.
