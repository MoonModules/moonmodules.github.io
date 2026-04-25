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

## Audiences

| Audience | What they need |
|---|---|
| Non-technical | What is this, what can it do, how do I get it |
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

---

## Sprint 3: Design and Branding

**Scope:** Establish the visual identity of the new site.

- Define or update the MoonModules logo (SVG, suitable for dark and light backgrounds)
- Choose a colour palette and typography that looks modern without being corporate
- Configure the MkDocs theme to match: header, footer, sidebar, font, colours
- Define what a good page looks like: heading hierarchy, image sizes, link style
- Day/night toggle in the header, defaulting to night (dark mode)
- No emoji in navigation or headings
- Review the homepage and a sample content page against the design

**Definition of done:** The design is consistent, documented in a style guide page, the new site is committed to the repository and published publicly for the first time, and the fork from https://github.com/thundergolfer/thundergolfer.github.io is removed.

---

## Sprint 4: Repository Showcase

**Scope:** Give every repository a clear, honest description so visitors understand the landscape.

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
- Yves / srg74 tooling

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

**Definition of done:** The Repos section is complete and accurate for all categories above.

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

---

## Sprint 7: Homepage

**Scope:** The homepage is the last sprint because it depends on all other content being in place.

- Clear headline: what MoonModules is in one sentence
- Three entry points: casual visitor, technical user, supporter
- Featured projects with thumbnail and one-line description
- Recent news (latest two or three posts from the blog)
- Community call to action: Discord, GitHub
- No wall of text, no AI-generated summary paragraph
- Works on mobile

**Definition of done:** The homepage accurately represents the site, loads quickly, and passes a review by at least two contributors who were not involved in writing it.

---

## Backlog (not yet scheduled)

- Support / documentation section: getting started guides for each product
- Hardware buying guide: migrate the current detailed hardware page
- Art and showcase gallery: projects made with MoonModules software
- Multilingual support (EU audience)
- Analytics: confirm GA4 is configured correctly on the new site

---

## How to contribute to this plan

Edit this page directly in the GitHub repository and submit a pull request. If you want to discuss a sprint scope before committing, open a GitHub issue or raise it on Discord.
