# Contributing

Anyone can suggest changes to this site. All content lives in the [GitHub repository](https://github.com/MoonModules/moonmodules.github.io) and is edited via pull requests.

---

## Editing an existing page

Every page has a pencil icon in the top right corner. Clicking it opens the file directly in GitHub. Make your changes, write a short description, and propose a pull request. A maintainer will review and merge it.

## Adding a new page

1. Add a Markdown file to the relevant folder under `docs/`
2. Add an entry for it in `mkdocs.yml` under `nav:`
3. Submit a pull request

## Adding a new post (when the blog is active)

The blog is not yet active. When it is, instructions will be added here.

---

## Style guide

### Language

- Write in plain English. Assume the reader is intelligent but not a WLED or ESP32 expert.
- Use European spelling: colour, favourite, grey, recognise, centre.
- Write in the third person for documentation. Use "you" only in direct instructions.
- Keep sentences short. One idea per sentence.

### What to avoid

- No TLDR sections. If a page needs a summary, shorten the page.
- No AI-sounding phrases: avoid "dive into", "leverage", "seamlessly", "robust", "comprehensive", "unlock".
- No hyphens for stylistic effect: write "easy to use" not "easy-to-use".
- No excessive emoji. Emoji in headings or navigation are not used on this site.
- No excessive bullet lists. Three or more bullet points that each deserve a sentence should be rewritten as a short paragraph.

### Headings

- Describe the content, not the action: "Installation" not "How to install it step by step".
- Use sentence case: "Getting started" not "Getting Started".
- No emoji in headings.

### Links

- Use descriptive link text: "read the MoonHub75 guide" not "click here".
- External links open in the same tab unless there is a specific reason not to.

### Images

- Compress images to under 200 KB before uploading. Use [TinyPNG](https://tinypng.com) or [Kraken](https://kraken.io/web-interface).
- Set an explicit width in pixels so the layout does not break on different screen sizes.
- Images can be stored in the GitHub repository (drag and drop while editing) or in external cloud storage.
