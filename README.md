<p align="center">
  <img src="assets/html-resume-banner.svg" alt="HTML Resume" width="100%">
</p>

<p align="center">
  AI Skills for ChatGPT · Codex · Antigravity · Claude · Cursor · Copilot
</p>

<div align="center">
  <h1>html-resume</h1>
  <p>A reusable agent skill for recruiter-friendly, production-ready HTML resumes and validated A4 PDFs.</p>
  <p>
    <a href="#what-it-does">English</a> ·
    <a href="README_zh.md">繁體中文</a> ·
    <a href="#why-html-first">Advantages</a> ·
    <a href="#example">Examples</a> ·
    <a href="#installation">Installation</a> ·
    <a href="#usage">Usage</a> ·
    <a href="#license">License</a>
  </p>
  <p>
    <a href="skills/html-resume/SKILL.md"><img alt="Skill valid" src="https://img.shields.io/badge/skill-valid-22c55e"></a>
    <a href=".codex-plugin/plugin.json"><img alt="Plugin ready" src="https://img.shields.io/badge/plugin-ready-2563eb"></a>
    <img alt="Version 0.1.0" src="https://img.shields.io/badge/version-v0.1.0-0ea5e9">
    <a href="LICENSE"><img alt="License MIT" src="https://img.shields.io/badge/license-MIT-16a34a"></a>
  </p>
</div>

---

`html-resume` helps AI agents turn career information into recruiter-friendly resumes, CVs, executive profiles, professional biographies, and portfolio summaries. It combines factual content rewriting, restrained editorial hierarchy, exact A4 layout, print-safe CSS, and PDF validation.

## 中文摘要

`html-resume` 是一個可重複使用的 Agent Skill，協助 AI 在不虛構經歷或數據的前提下，重寫並整理出對招募者友善的履歷、CV、主管簡介、專業介紹與作品集摘要。主要交付物永遠是 HTML；需要 PDF 時，會由同一份 HTML 產生精確 A4 文件並完成頁面驗證。

## What it does

- Creates or redesigns resumes, CVs, executive profiles, professional biographies, and portfolio summaries.
- Rewrites content for clarity and recruiter scanability without inventing facts, metrics, ownership, or qualifications.
- Uses restrained editorial hierarchy instead of dashboard-like, card-heavy layouts.
- Adapts section order and page count to the candidate rather than forcing every resume into two pages.
- Uses the color palette supplied or approved by the user instead of imposing a fixed Skill palette.
- Keeps the portrait and identity Header open and unboxed, with restrained color bands framing the physical pages.
- Always delivers production-ready HTML as the source of truth.
- Generates exact A4 PDF output with Chromium or Playwright when requested, then validates page size, overflow, clipping, and visual rendering.
- Preserves readable typography and selectable text for English and Chinese content.

## Why HTML first

- HTML gives both AI agents and people a structured, editable source. Agents can target semantic sections and CSS instead of recreating an entire document from scratch.
- Unlike generating a PDF directly, the HTML source remains practical to edit by hand after generation. The PDF is treated as the validated delivery format, not the only source file.
- Unlike generating an image, HTML keeps text selectable, searchable, and easier to validate. Image-generated text can contain unstable wording, spelling, character, or layout errors and is difficult to revise precisely.
- The same HTML can be exported to PDF after editing, so the workflow preserves source-level editability while still producing a polished final document.

## Writing recommendations

For language polishing during drafting, you can optionally use:

- English: [blader/humanizer](https://github.com/blader/humanizer)
- Traditional Chinese: [kevintsai1202/Humanizer-zh-TW](https://github.com/kevintsai1202/Humanizer-zh-TW)

These tools can help make wording more natural, but they do not replace fact-checking. Keep employers, dates, metrics, ownership, qualifications, and contact details grounded in the source information.

## Example

- [Sample input](examples/sample-input.md)
- [Sample HTML output](examples/sample-output/resume.html)
- [Example notes](examples/README.md)

The sample content is fictional and is included to demonstrate the expected input and output shape. The sample explicitly requests two pages and a business-oriented navy and steel-blue palette; those colors are not Skill defaults.

## Installation

### Option 1: Personal Skill in ChatGPT

Personal use does not require publishing this repository as a Plugin. ChatGPT can create or upload a custom Personal Skill directly. Follow the official [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) workflow:

1. In the ChatGPT sidebar, select **Plugins**.
2. In the Plugin Directory, open the **Skills** tab.
3. Select **Create**, then **Upload from your computer**.
4. Upload the complete `skills/html-resume/` Skill package. Keep `SKILL.md`, `agents/`, and `references/` together so all instructions and supporting resources remain available.
5. After ChatGPT finishes scanning the upload, install the Skill and start a conversation with a request such as:

   ```text
   Create an A4 HTML resume for a Senior Backend Engineer.
   Choose the page count based on the available content.
   Use a professional navy and steel-blue palette.
   Use the html-resume skill. Ask me for missing information first.
   ```

You can also choose **Create with chat** or **Create with editor** and use this repository as the source material. Personal Skills are generally available for ChatGPT Business, Enterprise, Healthcare, and Edu. Enterprise and Edu workspaces may require an admin to enable Skills and Skill uploads. Personal Skills must be added separately on desktop and web/mobile and do not automatically sync across those surfaces.

### Option 2: Local agents

The portable Skill is located at `skills/html-resume/`. Copy the complete folder into the local agent's Skill directory.

For Codex CLI or the Codex IDE extension, install it for the current repository:

```bash
mkdir -p .agents/skills
cp -R skills/html-resume .agents/skills/html-resume
```

Or install it for the current user:

```bash
mkdir -p ~/.agents/skills
cp -R skills/html-resume ~/.agents/skills/html-resume
```

Then start a new agent session if the Skill does not appear automatically. Invoke it explicitly with `$html-resume`, or allow implicit invocation when the request matches its description.

For other agents that implement the [Agent Skills standard](https://agentskills.io/), point the agent to `skills/html-resume/SKILL.md` or copy the entire `skills/html-resume/` directory into that agent's documented Skill directory. Keep both `SKILL.md` and `agents/openai.yaml` together.

### Option 3: PDF conversion environment with uv

This repository includes `pyproject.toml` and `uv.lock` for the Playwright-based PDF converter. After [installing uv](https://docs.astral.sh/uv/getting-started/installation/), create the project environment and install Chromium:

```bash
uv sync
uv run playwright install chromium
```

`uv sync` creates the local `.venv` and installs the locked Python dependencies. The Chromium installation is managed separately by Playwright.

## Usage

The Skill can be invoked explicitly:

```text
Use $html-resume to create a polished A4 HTML resume from the attached career history.
Use a professional navy and steel-blue palette.
```

It can also be used in natural language:

```text
Turn this work history into a PDF-ready HTML resume for an AI application engineer.
Choose the page count based on the strength and amount of content.
Use English section headings with concise Traditional Chinese content where appropriate.
Use a charcoal and muted teal color palette.
```

The Skill does not impose a default resume color. Include your preferred palette or brand direction in the prompt; if you omit it, the agent should ask you to choose one before applying visual styling.

Before generating the document, provide or confirm:

- Target document type.
- Language and audience.
- Target role or positioning.
- Page-count preference or hard limit, if any.
- Required sections.
- Color palette or brand direction.
- Avatar or portrait availability.
- HTML-only or HTML plus PDF output.

## Export to PDF

The recommended conversion path uses **Playwright (a browser automation tool) + Chromium (the browser engine behind Chrome)** through [`html_to_pdf.py`](html_to_pdf.py). The script opens the local HTML in Chromium and calls `page.pdf()` with:

- `print_background=True`
- `prefer_css_page_size=True`
- `format="A4"`

This preserves CSS such as `@page { size: A4; }`, millimeter-based dimensions, and background colors more faithfully. Because Chromium renders the HTML and CSS directly, the result is generally more stable than converting through LibreOffice's document layout model.

With the uv environment described in the Installation section, convert an HTML file with:

```bash
uv run python html_to_pdf.py examples/sample-output/resume.html resume.pdf
```

If you prefer not to use uv, install Playwright and Chromium directly, then run the same script with Python:

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
python3 html_to_pdf.py examples/sample-output/resume.html resume.pdf
```

The output path is optional. When omitted, the script writes the PDF beside the input HTML using the same base filename.

Always verify the PDF page size, render every page to an image, and inspect clipping, orphan headings, footer overlap, contrast, and font rendering before sharing it.

## Repository structure

```text
.
├── .codex-plugin/
│   └── plugin.json              # Plugin metadata and bundled Skill path
├── assets/
│   └── html-resume-banner.svg   # README banner
├── skills/
│   └── html-resume/
│       ├── SKILL.md             # Agent workflow and design rules
│       ├── agents/
│       │   └── openai.yaml      # Optional Codex UI metadata
│       └── references/
│           └── a4-layout-and-validation.md
├── examples/
│   ├── README.md
│   ├── sample-input.md
│   └── sample-output/
│       └── resume.html
├── html_to_pdf.py               # Playwright-based HTML-to-PDF converter
├── LICENSE
├── pyproject.toml               # Python project and Playwright dependency
├── README.md
├── README_zh.md
└── uv.lock                      # Reproducible Python dependency lockfile
```

## Design scope

This Skill is designed for:

- Professional resumes and CVs.
- Personal and executive profiles.
- Portfolio summaries.
- PDF-ready HTML career documents.

It is not a replacement for fact-checking, career coaching, or a human review of employment dates, metrics, contact details, and claims. Agents should treat user-provided career information as the source of truth and ask before inventing missing facts.

## Contributing

Keep the Skill focused on resume and professional-document workflows. When changing the Skill:

1. Update `skills/html-resume/SKILL.md`.
2. Update the sample input or output when behavior changes.
3. Validate the YAML front matter and plugin manifest.
4. Check that the sample HTML remains printable on A4 pages.

## License

Released under the [MIT License](LICENSE).
