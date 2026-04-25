# Development

### Prerequisites

Python 3.12+ and pip.

### Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run locally

```bash
mkdocs serve
```

Opens at `http://127.0.0.1:8000`. Changes to `docs/` reload automatically.

### Build

```bash
mkdocs build
```

Output goes to `site/` (gitignored).

### Deploy

Deployment is automated via GitHub Actions on every push to `main`. The workflow in `.github/workflows/deploy.yml` runs `mkdocs build` and pushes the result to the `gh-pages` branch.

### Community feeds

Reddit, YouTube, and Instagram feeds are fetched nightly by `.github/workflows/update-feeds.yml` and committed to `docs/assets/`. The deploy workflow uses the pre-committed JSON files — it does not fetch feeds itself.

Feed scripts are in `scripts/`.
