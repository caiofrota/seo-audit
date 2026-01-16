# SEO Audit (Browser-Based)

A SEO audit tool that analyzes websites **the way modern Google does**, using real browser rendering (Playwright) instead of static HTML parsing.

It generates a **client-ready SEO report** in Markdown, written in non-technical language and focused on clear, actionable improvements.

---

## 🚀 What this tool does

- Renders pages with **JavaScript enabled** (SPA, Next.js, React, etc.)
- Extracts data from the **real rendered DOM**
- Collects:
  - Page title, meta description, canonical and robots tags
  - Heading structure (H1, H2, H3)
  - Text content and word count
  - Internal, external, anchor and nofollow links
  - Images and missing ALT attributes
  - Social metadata (OpenGraph / Twitter)
  - **JSON-LD / Schema.org structured data**
- Automatically checks:
  - `robots.txt`
  - `sitemap.xml`
  - `llms.txt`
- Crawls a **limited number of internal pages**
- Generates a **client-ready SEO report** (`seo-report.md`)
- **No code snippets are included in the report**, only insights and recommendations

---

## 🧠 Why browser-based rendering?

Many SEO tools only read raw HTML and miss important content on modern websites.

This script:

- Executes JavaScript
- Reads the final rendered DOM
- Closely simulates modern Googlebot behavior

---

## 📦 Installation

### 1) Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Install Playwright browsers

playwright install

## ▶️ Usage

Basic audit

```bash
python seo-audit.py https://www.example.com
```

Limit the number of analyzed pages

```bash
python seo-audit.py https://www.example.com --max-pages 20
```

Specify output file

```bash
python seo-audit.py https://www.example.com --out seo-report.md
```

Automatically accept cookie banners (optional)

```bash
python seo-audit.py https://www.example.com --cookie-accept-text "Accept"
```

## 📄 Output

The script generates a Markdown file containing:

- Overall site score (0–100)
- Scores by SEO area (technical, content, schema, links, performance)
- Prioritized recommended actions
- Page-by-page summary table
- Detailed findings for each page

Example output:

```
seo-report.md
```

## ⚠️ Important notes

- The scoring system is heuristic: it helps prioritize improvements but does not guarantee rankings.
- For large websites, adjust --max-pages to control crawl time.
- Execution time depends on JavaScript complexity and site performance.

## 🛠️ Tech stack

- Python 3.10+
- Playwright (Chromium)
- BeautifulSoup
- lxml

## 🎯 Target audience

- Developers
- Technical SEO professionals
- Agencies
- Consultants
- Client-facing SEO audits

## 📄 License

MIT — see the [LICENSE](LICENSE) file for details.
