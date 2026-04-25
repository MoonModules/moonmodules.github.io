# Site Map

This document defines the full content structure of moonmodules.org. It covers the navigation tree, audience targeting per section, URL conventions, the news strategy, and the mapping of all existing Jekyll content to its new home.

---

## Navigation tree

```
/                     Home
/about/               About
/products/            Products — overview
/products/repos/      Products — repository descriptions and star counts
/support/             Support
/community/           Community and social feeds
/projects/            Projects — internal MoonModules initiatives
/archive/             Archive — all migrated content from the old site
/contributing/        Contributing — how to edit and add content
```

---

## Section purposes and audiences

| Section | Purpose | Primary audience |
|---|---|---|
| Home | First impression, entry points for each audience | All |
| About | History, team, mission, collaborators, support/donate | Non-technical, donors |
| Products | What MoonModules makes and which to choose | Non-technical, technical |
| Products / Repos | Per-repository description, star count, docs link | Technical |
| Support | Getting started, hardware guide, useful links | Non-technical, technical |
| Community | Social feeds, Discord, collaborations, art showcase | All |
| Projects | Internal initiatives such as this redesign | Technical, contributors |
| Archive | Migrated content from the old site, preserved as-is | Historical reference |
| Contributing | How to edit pages, add content, and follow the style guide | Contributors |

---

## URL conventions

- Clean paths with no dates: `/products/`, `/support/`
- Archive slugs strip the date prefix: `2025-01-14-MoonHub75-PCB` becomes `/archive/moonhub75-pcb/`
- No query strings or file extensions in URLs
- Lowercase, hyphens between words, no underscores
- Subdirectory pages use the parent as a prefix: `/products/repos/` not `/repos/`

---

## News and updates strategy

Social feeds are the primary channel for ongoing activity. MoonModules is active on YouTube, Reddit, and Instagram — surfacing those feeds on the Community page gives visitors a live picture of the project without requiring anyone to maintain a separate blog.

A blog section is kept as a future option. It will not be populated or linked in the main navigation until there is a commitment to maintain it. The MkDocs blog plugin stays installed but disabled.

Historical news posts from the old site are preserved in Archive. They are not treated as current news.

---

## Content mapping: existing Jekyll pages

| Source file | Archive slug | Future home |
|---|---|---|
| `index.md` | — | Home (Sprint 7) |
| `about.md` | `/archive/about/` | About (Sprint 6) |
| `software.md` | `/archive/software/` | Products overview (Sprint 4) |
| `hardware.md` | `/archive/hardware/` | Products / Support split (Sprint 4) |
| `community.md` | `/archive/community/` | Community (Sprint 5/6) |
| `links.md` | `/archive/links/` | Support (future sprint) |
| `art.md` | `/archive/art/` | Community — art and installations (future sprint) |

---

## Content mapping: existing Jekyll posts

| Source file | Archive slug | Future home |
|---|---|---|
| `2024-11-04-moonmodules-website.md` | `/archive/moonmodules-website/` | Projects |
| `2024-11-04-waveshare-p4.md` | `/archive/waveshare-p4/` | Products |
| `2024-11-05-Star v0.5.0 released.md` | `/archive/star-v0-5-0-released/` | Products |
| `2024-11-06-ESPLiveScript-v1.2.0.md` | `/archive/esplive-script-v1-2-0/` | Products |
| `2024-11-28-Multi-pin-fixtures.md` | `/archive/multi-pin-fixtures/` | Support |
| `2024-12-01-Bike-leds-bicyclus.md` | `/archive/bike-leds-bicyclus/` | Community |
| `2024-12-20-Star v0.6.0-2024-wrapup.md` | `/archive/star-v0-6-0-2024-wrapup/` | Products |
| `2025-01-13-Portable_Rack_for_WLED_Lighting_Network_and_Audio.md` | `/archive/portable-rack/` | Support |
| `2025-01-13-Universal-Control-Box.md` | `/archive/universal-control-box/` | Support |
| `2025-01-14-MoonHub75-PCB.md` | `/archive/moonhub75-pcb/` | Products |
| `2025-03-17-Star-Mod-Base-Light-Moon-Svelte-Live.md` | `/archive/star-mod-base-light-moon-svelte-live/` | Products |
| `2025-03-29-MoonBase-Modules.md` | `/archive/moonbase-modules/` | Products |
| `2025-07-16-MoonLightv0.5.7-v0.5.8.md` | `/archive/moonlight-v0-5-7-v0-5-8/` | Products |
| `2025-09-09-MoonLight-Concert.md` | `/archive/moonlight-concert/` | Community |
