<p align="center">
  <img src="assets/html-resume-banner.svg" alt="HTML Resume" width="100%">
</p>

<p align="center">
  AI Skills for ChatGPT · Codex · Antigravity · Claude · Cursor · Copilot
</p>

<div align="center">
  <h1>html-resume</h1>
  <p>一個可重複使用的 Agent Skill，用於建立對招募者友善、可直接使用的 HTML 履歷與經驗證的 A4 PDF。</p>
  <p>
    <a href="README.md">English</a> ·
    <a href="README_zh.md">繁體中文</a> ·
    <a href="#範例">範例</a> ·
    <a href="#安裝">安裝</a> ·
    <a href="#使用方式">使用方式</a> ·
    <a href="#授權">授權</a>
  </p>
  <p>
    <a href="skills/html-resume/SKILL.md"><img alt="Skill valid" src="https://img.shields.io/badge/skill-valid-22c55e"></a>
    <a href=".codex-plugin/plugin.json"><img alt="Plugin ready" src="https://img.shields.io/badge/plugin-ready-2563eb"></a>
    <img alt="Version 0.1.0" src="https://img.shields.io/badge/version-v0.1.0-0ea5e9">
    <a href="LICENSE"><img alt="License MIT" src="https://img.shields.io/badge/license-MIT-16a34a"></a>
  </p>
</div>

---

`html-resume` 協助 AI Agent 將職涯資料整理為對招募者友善的履歷、CV、主管簡介、專業介紹與作品集摘要。它結合忠於事實的內容重寫、克制的編輯層級、精確的 A4 版面、適合列印的 CSS，以及 PDF 驗證流程。

## 功能

- 建立或重新設計履歷、CV、主管簡介、專業介紹與作品集摘要。
- 在不虛構經歷、數據、職責歸屬或資格的前提下，提高內容清晰度與招募者掃讀效率。
- 採用克制的編輯層級，避免儀表板式或過度使用卡片的版面。
- 根據候選人的內容調整章節順序與頁數，不強制將所有履歷限制為兩頁。
- 使用者必須提供或確認履歷配色，Skill 不會強制套用固定色系。
- 照片與人物 Header 採用開放式排列，不放入 Card，並以克制的上下色帶框定實體頁面。
- 永遠以可直接使用的 HTML 作為單一真實來源（source of truth）。
- 需要 PDF 時，使用 Chromium 或 Playwright 產生精確的 A4 文件，並驗證頁面尺寸、溢出、裁切與視覺渲染。
- 確保英文與中文內容具備清楚易讀的排版，並保留可選取的文字。

## 範例

- [輸入範例](examples/sample-input.md)
- [HTML 輸出範例](examples/sample-output/resume.html)
- [範例說明](examples/README.md)

範例內容皆為虛構資料，僅用於展示預期的輸入與輸出格式。範例明確要求兩頁，並指定商業感 navy／steel blue 配色；這組顏色不是 Skill 的預設值。

## 安裝

### 方式一：ChatGPT 網頁版

ChatGPT 網頁版透過可安裝的 Plugin 發佈可重複使用的 Skills。原始的 `SKILL.md` 資料夾適合本地編寫，但本身並不是網頁版的安裝套件。

此 Repo 已準備好 Plugin 所需結構：

1. 依照[官方 Plugin 封裝文件](https://developers.openai.com/plugins/build/plugins)，將此 Repo 發佈或提交為 `html-resume` Plugin。
2. 在 ChatGPT 網頁版開啟工作區可用的 Plugin 目錄。
3. 搜尋 `HTML Resume` 並安裝。
4. 開始對話，輸入類似以下的需求：

   ```text
   Create an A4 HTML resume for a Senior Backend Engineer.
   Choose the page count based on the available content.
   Use a professional navy and steel-blue palette.
   Use the html-resume skill. Ask me for missing information first.
   ```

Plugin 是否可安裝，取決於 ChatGPT 產品方案、工作區設定與發佈狀態。如果 Plugin 尚未發佈，請改用下方的本地安裝方式，或透過[官方 Plugin 提交流程](https://developers.openai.com/plugins/deploy/submission)提交。

### 方式二：本地 Agent

可攜式 Skill 位於 `skills/html-resume/`。請將完整資料夾複製到本地 Agent 的 Skill 目錄。

若使用 Codex CLI 或 Codex IDE extension，可安裝到目前的 Repo：

```bash
mkdir -p .agents/skills
cp -R skills/html-resume .agents/skills/html-resume
```

或安裝到目前使用者的環境：

```bash
mkdir -p ~/.agents/skills
cp -R skills/html-resume ~/.agents/skills/html-resume
```

如果 Skill 沒有自動出現，請重新啟動 Agent session。你可以用 `$html-resume` 明確呼叫，也可以在需求符合 Skill 描述時讓 Agent 自動判斷使用。

若其他 Agent 支援 [Agent Skills standard](https://agentskills.io/)，請讓 Agent 指向 `skills/html-resume/SKILL.md`，或將完整的 `skills/html-resume/` 資料夾複製到該 Agent 文件指定的 Skill 目錄。請確保 `SKILL.md` 與 `agents/openai.yaml` 一起保留。

## 使用方式

可以明確呼叫 Skill：

```text
Use $html-resume to create a polished A4 HTML resume from the attached career history.
Use a professional navy and steel-blue palette.
```

也可以直接用自然語言描述需求：

```text
Turn this work history into a PDF-ready HTML resume for an AI application engineer.
Choose the page count based on the strength and amount of content.
Use English section headings with concise Traditional Chinese content where appropriate.
Use a charcoal and muted teal color palette.
```

Skill 不會強制套用預設履歷顏色。請在提示中自行指定偏好的配色或品牌方向；如果沒有指定，Agent 應先詢問你要使用的顏色，再開始套用視覺樣式。

產生文件前，請提供或確認以下資訊：

- 目標文件類型。
- 語言與目標讀者。
- 目標職位或定位。
- 頁數偏好或硬性限制（如有）。
- 必要章節。
- 色彩配置或品牌方向。
- 是否提供頭像或個人照片。
- 僅需 HTML，或同時需要 HTML 與 PDF。

## 匯出 PDF

產生 `resume.html` 後，可使用 Chromium 匯出：

```bash
chromium \
  --headless \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf=resume.pdf \
  resume.html
```

或使用 Playwright：

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

分享 PDF 前，務必確認頁面尺寸，將每一頁渲染為圖片，並檢查裁切、孤立標題、頁尾重疊、對比度與字型渲染。

## Repo 結構

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

## 適用範圍

此 Skill 適用於：

- 專業履歷與 CV。
- 個人簡介與主管簡介。
- 作品集摘要。
- 可匯出 PDF 的 HTML 職涯文件。

它不能取代事實查核、職涯諮詢，也不能取代人工確認任職日期、數據、聯絡資訊與相關陳述。Agent 應將使用者提供的職涯資料視為單一真實來源，缺少資訊時應先詢問，不得自行虛構。

## 貢獻

請讓 Skill 專注於履歷與專業文件工作流程。修改 Skill 時：

1. 更新 `skills/html-resume/SKILL.md`。
2. 行為變更時，同步更新輸入或輸出範例。
3. 驗證 YAML front matter 與 Plugin manifest。
4. 確認 HTML 範例仍可正確列印為 A4 頁面。

## 授權

本專案採用 [MIT License](LICENSE) 授權。
