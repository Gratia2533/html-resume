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

## Example

- [Sample input](examples/sample-input.md)
- [Sample HTML output](examples/sample-output/resume.html)
- [Example notes](examples/README.md)

The sample content is fictional and is included to demonstrate the expected input and output shape. The sample explicitly requests two pages and a business-oriented navy and steel-blue palette; those colors are not Skill defaults.

## Installation

### Option 1: ChatGPT on the web

ChatGPT on the web uses the installable Plugin distribution for reusable Skills. A raw `SKILL.md` folder is intended for local authoring and is not, by itself, a web installation package.

This repository is Plugin-ready:

1. Publish or submit this repository as the `html-resume` Plugin using the [official Plugin packaging documentation](https://developers.openai.com/plugins/build/plugins).
2. In ChatGPT on the web, open the Plugin directory available to your workspace.
3. Search for `HTML Resume` and install it.
4. Start a conversation with a request such as:

   ```text
   Create an A4 HTML resume for a Senior Backend Engineer.
   Choose the page count based on the available content.
   Use a professional navy and steel-blue palette.
   Use the html-resume skill. Ask me for missing information first.
   ```

Availability of Plugin installation can depend on the ChatGPT product, workspace, and publication status. If the Plugin has not been published yet, use the local installation method below or submit it through the [official Plugin submission flow](https://developers.openai.com/plugins/deploy/submission).

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

After generating `resume.html`, export it with Chromium:

```bash
chromium \
  --headless \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf=resume.pdf \
  resume.html
```

Or use Playwright:

```js
import { chromium } from "playwright";

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto("file:///absolute/path/resume.html", { waitUntil: "networkidle" });
await page.pdf({
  path: "resume.pdf",
  format: "A4",
  printBackground: true,
  margin: { top: "0mm", right: "0mm", bottom: "0mm", left: "0mm" }
});
await browser.close();
```

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
├── LICENSE
├── README.md
└── README_zh.md
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
