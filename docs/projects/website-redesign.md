# Website Redesign Project

MoonModules.org is being rebuilt from the ground up. The current site is a Jekyll fork that has grown organically and no longer reflects what MoonModules is today. This page tracks the redesign project using a sprint-based approach. Each sprint has a clear scope and can be refined and reviewed before execution.

This page is itself part of the redesigned website, as a practical example of how an open project can plan and document a website rebuild in public.

## Goals

- A website that is genuinely up to date and maintained
- Clean, modern design with no AI-generated feel: plain language, no excessive punctuation or emoji
- Three distinct audiences served well: casual visitors, technical contributors, and potential supporters or donors
- European tone of voice
- Easy for any contributor to add content without deep knowledge of the tooling
- Replaces the Jekyll fork with a clean MkDocs project built from scratch

## Proposed Navigation

```
Home
About
Products
  Repos
Support
Community
Projects
Archive
```

Repos moves under Products: it is less intimidating to non-technical visitors and accurately reflects that repositories are where the products live. Archive is a top-level section holding all migrated content from the current site.

**Projects** is the showcase of things MoonModules has actually built: art installations, hardware projects, 3D prints, PCB designs. It is not a software documentation section. Examples from Archive that belong here: the Cube202020, the Mikael Pedersen bike, the MoonHub75 PCB, the Universal Control Box, 3D print models on Bambu Labs / Printables. The website redesign itself also lives here as a meta-project.

**Support** will include a dedicated hardware buying guide, extracted from the Archive hardware page (the "Best buy guide" section). This gives non-technical visitors a clean shopping list without wading through hardware specifications aimed at developers.

## Audiences

| Audience | What they need |
|---|---|
| Non-technical — including friends and family who have no idea what any of this is | What is this, what can it do, how do I get it, can I see it |
| Technical | Project status, how to contribute, architecture |
| Supporter / donor | Who is behind this, what is the impact, how to support |

---

## Sprint 0: Foundation

**Scope:** Set up the new MkDocs project. This sprint produces a working skeleton, not finished content.

- Create a new MkDocs project in this repository (not forked from anything)
- Choose a theme: Material for MkDocs is the obvious choice given its navigation, search, and extensibility
- Configure GitHub Actions to build and deploy to moonmodules.org
- Set up the top-level navigation structure matching the proposed nav above
- Establish contribution guidelines: how to edit a page, how to add a news post, PR workflow
- Verify the build deploys correctly with placeholder content on all sections

**Definition of done:** The site builds, deploys, and is reachable at moonmodules.org with the new structure in place.

**Result:** MkDocs project created with Material theme, dark mode default, full navigation skeleton, and GitHub Actions deploy workflow. One manual step required before the site goes live: in the GitHub repository settings, change Pages source from "Deploy from a branch" to "GitHub Actions".

**Retrospective:**

What went well:
- Material for MkDocs covered all Sprint 0 requirements out of the box: dark/light toggle, edit button, search, tabs
- Keeping old Jekyll files at root untouched made the transition clean with no content loss
- CNAME placed in `docs/` ensures the custom domain survives the build

What was difficult:
- GitHub Pages requires a one-time manual settings change to switch from Jekyll to Actions-based deployment; this cannot be automated and must be done by a repo admin before the new site goes live

Points for Sprint 1:
- Decide on URL structure before any content is written: changing URLs later breaks external links
- The tone of voice guidelines are the most important output of Sprint 1 — without them, contributors will write inconsistently from the start
- Agree early on what counts as "blog content" vs "social feed content" so Sprint 2 archiving decisions are clear

---

## Sprint 1: Site Map

**Scope:** Define the full content structure before any migration or writing begins.

- Produce a detailed site map covering all pages and their purpose
- Map each existing page and post to its new location or to Archive
- Define which content is aimed at which audience
- Agree on URL structure (clean, no dates in non-blog URLs)
- Define the news strategy: social feeds (Reddit, YouTube) are the primary channel for ongoing activity; a blog section is planned but will start empty and is kept as a future option, not a maintenance burden
- Document tone of voice: plain language, no TLDR sections, no AI-sounding headings, European spelling

**Definition of done:** A reviewed site map document exists and there is agreement on where everything lives.

**Result:** Site map created at [projects/site-map.md](site-map.md) covering the full navigation tree, audience targeting per section, URL conventions, news strategy, and a mapping of all 14 existing posts and 7 existing pages to their archive slug and future home. Contributing guide created at [contributing.md](../contributing.md) with tone of voice rules and editing workflow. Logo moved to `docs/assets/` and wired into the theme. Both pages added to the nav.

**Retrospective:**

What went well:
- Mapping all existing content up front gives Sprint 2 a clear checklist with no decisions left to make
- Keeping the news strategy decision (social feeds primary, blog optional) in the site map makes the reasoning visible to future contributors
- The contributing guide doubles as a style reference during all subsequent sprints

What was difficult:
- Some post titles are ambiguous about their future home (release notes vs. product documentation vs. support articles); the mapping in the site map reflects a first judgement and may be revised in Sprint 2

Points for Sprint 2:
- Use the slug column in the site map as the exact file naming convention — do not invent new slugs during migration
- Flag content that is factually outdated at migration time; do not silently copy stale information into Archive
- The hardware page is large and mixes product descriptions with a buying guide — note the split point when archiving so Sprint 4 knows where to divide it

---

## Sprint 2: Content Archive

**Scope:** Preserve all existing content. Nothing is rewritten or moved to its final location yet; everything lands in the Archive section.

- Copy all existing blog posts into the Archive section in MkDocs format
- Copy the current pages (About, Software, Hardware, Community, Links) into Archive
- Re-tag and re-categorise each item to indicate its future home in the new structure
- Identify content that is outdated and flag it for update or removal in a later sprint
- No new writing, no final placement in this sprint

**Definition of done:** Every piece of existing content is in the Archive section and has a documented future home. Nothing is lost, nothing is moved yet. Content will be moved from Archive to its final location gradually across the sprints that follow.

**Result:** All 14 posts and 7 pages migrated to `docs/archive/`. Each page carries a Material admonition showing its future home and an outdated flag where relevant (5 posts and 2 pages flagged). The archive index provides a single table of all items with status. The `admonition` markdown extension was added to `mkdocs.yml`. Archive pages are deliberately not listed in the nav — they are reachable via the index table.

**Retrospective:**

What went well:
- The site map from Sprint 1 gave exact slugs and future homes, so no decisions were needed during migration
- The admonition format makes outdated content visible without breaking the page or losing the content
- The split-point annotation on hardware.md gives Sprint 4 a clear instruction without requiring any content to be touched now

What was difficult:
- Several posts reference StarBase and StarLight by name; flagging them as outdated is correct but the nuance is that the project history is accurate — only the product names changed. Sprint 4 will need to handle this carefully when writing the new Products pages
- MkDocs logs "not in nav" notices for all unlisted archive pages; this is expected behaviour and not an error, but worth noting so future contributors do not try to add them all to `mkdocs.yml`

Points for Sprint 3:
- The logo is already in `docs/assets/`; Sprint 3 should verify it renders well on both dark and light backgrounds before committing to it
- Agree on the colour palette before touching any other theme settings — colour affects how admonitions, code blocks, and links look throughout the whole site
- The hardware.md archive page has a divider comment marking the Products/Support split; Sprint 4 should use it as a literal cut line

---

## Sprint 3: Design and Branding

**Scope:** Establish the visual identity of the new site.

- Define or update the MoonModules logo (SVG, suitable for dark and light backgrounds)
- Choose a colour palette and typography that looks modern without being corporate — the current default feels too much like a GitHub documentation site; the goal is something that works for non-technical visitors and reflects the art and maker side of MoonModules
- Configure the MkDocs theme to match: header, footer, sidebar, font, colours
- Define what a good page looks like: heading hierarchy, image sizes, link style
- Day/night toggle in the header, defaulting to night (dark mode)
- No emoji in navigation or headings
- Review the homepage and a sample content page against the design

**Design direction — options for discussion:**

Three directions to consider, in order from least to most effort:

1. **Warmer dark theme** — keep the Material framework but swap the indigo palette for something with more warmth (deep teal, amber accent, or a purple-leaning dark). Less corporate, still fully functional. Low effort. Reference feel: creative tool documentation sites, not enterprise software.

2. **Image-led layout** — make the homepage and Projects section visually driven by photos and video stills of actual installations. The tech recedes to the background; the first thing a visitor sees is light art, not a sidebar. Medium effort, mostly CSS and layout adjustments to the Material theme.

3. **Custom typography** — add a display font for headings (something geometric or slightly playful, not a system font) while keeping a clean readable body font. Changes the personality of the site significantly without touching layout. Low to medium effort via the Material `font` config.

These can be combined. A decision is needed before any theme work begins so contributors do not redo each other's work.

**Definition of done:** The design is consistent, documented in a style guide page, the new site is committed to the repository and published publicly for the first time, and the fork from https://github.com/thundergolfer/thundergolfer.github.io is removed.

**Result:** Colour palette set to teal primary + amber accent, replacing the default Material indigo. Header given a distinctive dark gradient (`#0a1f1a` → `#0d3028`) with an amber accent line and subtle glow — consistent across both dark and light modes, inspired by the openframeworks.cc aesthetic of typographic confidence over corporate colour. Space Grotesk applied to h1–h4 and the site name. Navigation tabs styled uppercase with letter-spacing; active tab highlighted in amber. GitHub repository icon hidden from the header (edit button still works). Visual style guide added to `docs/contributing.md`. Fork detach is a manual step in GitHub Settings for the repo admin.

**Retrospective:**

What went well:
- Teal + amber reads as warm and craft-oriented rather than developer tooling — noticeably less corporate than the default Material purple
- Keeping the header dark in both schemes avoids the inconsistency of a colour flip when toggling day/night
- Space Grotesk gives the site name and headings real personality without requiring a custom typeface pipeline
- The openframeworks.cc reference was a useful anchor — the uppercase sparse tab lettering with a clean active indicator is the key detail that makes the header feel distinctive

What was difficult:
- MkDocs Material's hot reload does not always pick up CSS changes mid-session; a manual server restart was needed to see updates
- The logo PNG has a white background that may cause a slight halo on the dark header; `mix-blend-mode: lighten` is applied as a workaround, but the proper fix is an SVG version (backlog)

Points for Sprint 4:
- The archive hardware page has a clear divider marking where the Products content ends and the buying guide begins — use it as a literal cut line
- The Projects showcase pages will be the first pages on the new site with real images; check that image widths render consistently across dark and light modes before finishing the sprint
- Consider adding `navigation.instant` to `mkdocs.yml` features in Sprint 4 to make page transitions feel faster

---

## Sprint 4: Repository Showcase and Projects Showcase

**Scope:** Give every repository a clear description, build out the Projects section as a showcase of physical and art builds, and create a standalone buying guide in Support.

Repositories to cover:

**Core products**
- WLED-MM
- MoonLight
- projectMM
- FastLED-MM

**Supporting repositories**
- WLED-MM-Troyhacks (Troy)
- Hardware repo (MoonHub75 PCB, control boxes)
- Audio Reactive (extraction in progress)
- srg74 tooling (Serg)
- hpwit tooling (Yves) — ESPLiveScript, I2SClocklessLedDriver, I2SClocklessVirtualLedDriver

**Used and referenced projects**
- WLED (Aircoookie upstream)
- FastLED
- ArduinoJson
- AsyncWebServer
- ESPLiveScript (hpwit)
- I2SClocklessLedDriver / I2SClocklessVirtualLedDriver (hpwit)
- animartrix (Stefan Petrick)

For each repository:
- One-paragraph description aimed at a non-technical reader
- Key technical characteristics (audience, pixel scale, platform)
- Current status and roadmap note
- Link to GitHub with live star count
- Link to documentation where it exists

**Projects showcase** — extract from Archive and write up:

- Art installations: Cube202020, Mikael Pedersen bike, BFC (Big Freakin' Cube), concert at festival
- Hardware builds: MoonHub75 PCB, Universal Control Box (with Bambu Labs / Makerworld links)
- 3D prints: 16x16 LED matrix grid, illuminated sphere, control boxes
- Each project gets a title, one image, a short description, and links to relevant resources

**Buying guide** — extract the "Best buy guide" section from the hardware Archive page into `docs/support/buying-guide.md`. Keep it as a practical shopping list for people who want to get started without reading through developer documentation.

**Definition of done:** The Repos section is complete and accurate for all categories above. The Projects section has at least one page per project type (art, hardware, 3D prints). The buying guide is live under Support.

**Result:** Repos page rewritten with full descriptions for all four core products (WLED-MM, MoonLight, projectMM, FastLED-MM) and all supporting repos, plus a credits table for third-party dependencies. Projects section expanded with four new pages: art installations, concert at a festival (standalone), hardware builds, and 3D prints. Support converted from a single file to a section; buying guide extracted from `archive/hardware.md` and published at `support/buying-guide.md`. Navigation updated throughout.

**Retrospective:**

What went well:
- Archive content from Sprint 2 was complete enough that the Projects and buying guide pages needed almost no new writing — the work was restructuring and trimming, not researching from scratch
- The split-point annotation on `archive/hardware.md` from Sprint 2 made the buying guide extraction a clean cut with no ambiguity
- Keeping "Used and referenced projects" as a credits table rather than full descriptions keeps the repos page readable without losing attribution

What was difficult:
- projectMM has limited public documentation; the description is based on what is inferrable from the codebase and archive posts — worth reviewing for accuracy
- The concert archive page was already very detailed; deciding how much detail to carry into the new Projects page required judgement calls

Points for Sprint 5:
- The Community page currently has placeholder content — Sprint 5 social feeds work will make it the most immediately useful page for returning visitors
- The shields.io star count badges on the repos page are live at build time but static once deployed; if star counts matter for credibility, consider a note about when the page was last updated
- The archive pages for moonhub75-pcb, universal-control-box, art, and moonlight-concert now have corresponding final-home pages — their admonition notes could be updated to link directly to the new pages

---

## Sprint 5: Social Feeds

**Scope:** Surface activity from the channels where MoonModules is actually active.

- YouTube: embed or link the MoonModules channel, show recent videos
- Reddit: link the r/moonmodules community or relevant posts
- Instagram: show recent posts or a profile link
- Discord: invite link and member count, the primary communication channel
- GitHub: live star counts on the main repositories (via shields.io badges or similar)

Note: fully automated live feeds require either JavaScript widgets or a build-time fetch. Decide on static vs dynamic per platform based on maintenance cost.

**Definition of done:** Each social channel has a presence on the Community page and at least one is a live or regularly updated feed.

**Result:** Community page rewritten with sections for Discord, Reddit, YouTube (split into Shorts and Videos), GitHub, and Instagram. Reddit and YouTube feeds are generated at build time via Python scripts (`scripts/fetch_reddit.py`, `scripts/fetch_youtube.py`) and written to static JSON files in `docs/assets/`. The JavaScript reads these local files on page load — no external API calls, no CORS issues. A nightly GitHub Actions workflow (`update-feeds.yml`) refreshes the feeds independently of code commits. Reddit posts show thumbnails and description text. YouTube cards show thumbnail, title, and date in a row layout. Reddit feed appears on both the homepage and the Community page via a `data-feed="reddit"` attribute. GitHub shows live star count badges via shields.io. Instagram lists three contributor profiles. The `attr_list` markdown extension was added to enable Material button styling. Products section restructured: `repos.md` split into one page per core product plus Supporting and Acknowledgements pages. projectMM and FastLED-MM descriptions rewritten from their GitHub READMEs.

**Retrospective:**

What went well:
- Build-time fetch eliminates CORS entirely — the JSON files are local assets served by MkDocs, so the JavaScript is trivial and reliable
- Separating YouTube into Shorts and Videos required only a URL check (`/shorts/` in the link) — the RSS contains all entries in a single feed
- The nightly workflow pattern (fetch → commit if changed → deploy triggers) keeps feeds fresh without any manual intervention and without coupling feed updates to code changes
- Using `data-feed` attribute instead of `id` for the Reddit container lets the same feed appear on multiple pages with one JS function

What was difficult:
- Three consecutive fetch strategies were tried for YouTube (rss2json.com → allorigins.win → build-time script) before landing on the right approach; both third-party CORS proxies had reliability or access issues
- Reddit's public JSON API returns 403 without a correctly formatted User-Agent string; this works fine from Python at build time but cannot be set from browser JavaScript
- YouTube Shorts have no description text in the RSS feed; the `media:description` element is present but empty — nothing to show until descriptions are added in YouTube Studio
- Instagram has no public API suitable for a static site; individual contributor profile links are the only viable option

Points for Sprint 6:
- The About page is the most text-heavy sprint — start with the team section and let the history and mission flow from there rather than writing top-to-bottom
- The collaboration section (Apollo Automation, Glorb, Tarna, srg74, hpwit, Stefan Petrick, wladi) benefits from a one-liner per collaborator rather than a list of names — a sentence each is more informative for a visitor who doesn't know these names
- The Reddit feed on the homepage gives Sprint 7 a strong foundation — the homepage already has live content and does not need a blog or manually maintained news section
- The About page is the most text-heavy sprint — start with the team section and let the history and mission flow from there rather than writing top-to-bottom
- The collaboration section (Apollo Automation, Glorb, Tarna, srg74, hpwit, Stefan Petrick, wladi) benefits from a one-liner per collaborator rather than a list of names — a sentence each is more informative for a visitor who doesn't know these names
- If the community page live feeds are working as expected after deployment, consider linking to Community from the homepage in Sprint 7 rather than duplicating content

---

## Sprint 6: About Page

**Scope:** Tell the MoonModules story clearly and for all three audiences.

- History: from Atuline fork in 2021 to the current project landscape
- Team: Ewowi, Harry, SoftHack007, Troy, Sören, NetMindz, and key collaborators
- Mission: open source lighting, ESP32, GPL/EUPL, community-led
- What we use the site for and how to contribute to it
- Collaboration section: Apollo Automation, Glorb, Tarna art car, srg74, hpwit, Stefan Petrick, wladi
- Support or donate section: for investors and donors, explain the project's sustainability model
- No long lists of bullet points; write in paragraphs

**Definition of done:** A reviewer unfamiliar with MoonModules can read the About page and understand who this is, what they build, and how to get involved.

**Result:** `docs/about.md` written in full with five sections: Who we are, History, Team (table), Collaborators, and Support/Donate. The collaborator section covers Apollo Automation, Glorb, Tarna, QuinLED, Wladislaw Waag, hpwit, srg74, and Stefan Petrick — each with a one-liner and a link where applicable. Descriptions compiled from their public websites and GitHub profiles. PayPal donation link added as a Material button. `docs/products/index.md` updated with three new sections: Project timeline (narrative replacing the flat list from the archive), Roadmap (April 2026), and a What to use decision table. Both the history prose in `about.md` and the product timeline in `products/index.md` are written to be readable by a non-technical visitor.

**Retrospective:**

What went well:
- The archive/about.md had enough factual content that the rewrite was structuring and trimming rather than research — the history section wrote itself once the events were in order
- Fetching collaborator websites directly produced accurate one-liners without guesswork; QuinLED and myhome-control.de were particularly clear about their scope
- Separating the donation section from the general support/contribute text keeps the ask from feeling heavy; the Material button makes it unambiguous without being prominent
- The "What to use" table replaces a flat bullet list with a decision matrix that is significantly easier to scan

What was difficult:
- Tarna's site (tarna.ca) had an expired SSL certificate and could not be fetched directly; the description is intentionally minimal
- Apollo Automation's WLED-MM connection required searching GitHub (ApolloAutomation/WLED-MM-M1) to confirm the relationship — their main site focuses on the broader smart home product line

Points for Sprint 7:
- The About page collaborator section and the Homepage could share a condensed version of the collaborator list — consider a short "used by" row of logos or names on the homepage
- The What to use table in products/index.md links directly to product pages; verify all anchor links resolve after deployment
- The homepage is the only remaining page with placeholder-level content — Sprint 7 can now draw on the full site to build it

---

## Sprint 7: Homepage

**Scope:** The homepage is the last sprint because it depends on all other content being in place.

- Clear headline: what MoonModules is in one sentence
- Three entry points: casual visitor, technical user, supporter
- Featured projects with thumbnail and one-line description
- Recent news: live Reddit feed already placed in Sprint 5 — verify it renders correctly and fits the final homepage layout
- Community call to action: Discord, GitHub
- No wall of text, no AI-generated summary paragraph
- Works on mobile

**Definition of done:** The homepage accurately represents the site, loads quickly, and passes a review by at least two contributors who were not involved in writing it.

---

## Backlog (not yet scheduled)

- Detach fork from thundergolfer/thundergolfer.github.io — option not available in GitHub Settings UI; contact [GitHub Support](https://support.github.com) to request detach, or leave as cosmetic issue
- SVG version of the MoonModules logo — current PNG has a white background causing a slight halo on the dark header; `mix-blend-mode: lighten` is the current workaround
- Support / documentation section: getting started guides for each product
- Hardware buying guide: migrate the current detailed hardware page
- Art and showcase gallery: projects made with MoonModules software
- Multilingual support (EU audience)
- Analytics: confirm GA4 is configured correctly on the new site

---

## How to contribute to this plan

Edit this page directly in the GitHub repository and submit a pull request. If you want to discuss a sprint scope before committing, open a GitHub issue or raise it on Discord.
