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
    <a href="#為什麼優先使用-html">優勢</a> ·
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

`html-resume` 協助 AI Agent 將任何求職平台匯出的履歷、既有 PDF 或職涯資料，快速整理成可自行修改且對招募者友善的履歷、CV、主管簡介、專業介紹與作品集摘要。它支援中翻英、英翻中與同語言重寫，並結合忠於事實的內容整理、克制的編輯層級、精確的 A4 版面、適合列印的 CSS，以及 PDF 驗證流程。

## 功能

- 建立或重新設計履歷、CV、主管簡介、專業介紹與作品集摘要。
- 將任何求職平台匯出的履歷或既有 PDF，轉為不受原平台與版面限制、可自行持續修改的文件。
- 支援中翻英、英翻中與同語言重寫，在保留事實的前提下改寫為自然且適合招募情境的文字。
- 在不虛構經歷、數據、職責歸屬或資格的前提下，提高內容清晰度與招募者掃讀效率。
- 採用克制的編輯層級，避免儀表板式或過度使用卡片的版面。
- 根據候選人的內容調整章節順序與頁數，不強制將所有履歷限制為兩頁。
- 使用者必須提供或確認履歷配色，Skill 不會強制套用固定色系。
- 照片與人物 Header 採用開放式排列，不放入 Card，並以克制的上下色帶框定實體頁面。
- 永遠以可直接使用的 HTML 作為單一真實來源（source of truth）。
- 需要 PDF 時，使用 Chromium 或 Playwright 產生精確的 A4 文件，並驗證頁面尺寸、溢出、裁切與視覺渲染。
- 確保英文與中文內容具備清楚易讀的排版，並保留可選取的文字。

## 為什麼優先使用 HTML

- HTML 提供 AI Agent 與人工都能修改的結構化來源。Agent 可以針對語意化章節與 CSS 進行調整，不必每次都從頭重建整份文件。
- 與直接產生 PDF 相比，HTML 產出後仍然方便人工修改；PDF 應被視為經驗證後的交付格式，而不是唯一的來源檔案。
- 與產生圖片相比，HTML 的文字可以選取、搜尋，也更容易驗證。圖片中的文字可能出現措辭、錯字、字元或版面不穩定等問題，之後也很難精確修改。
- 修改完成後，可以從同一份 HTML 再匯出 PDF；因此既保留原始來源的可編輯性，也能產生適合交付的最終文件。

## 撰寫建議

撰寫與潤飾內容時，可以依語言選擇以下工具作為輔助：

- 英文：[blader/humanizer](https://github.com/blader/humanizer)
- 繁體中文：[kevintsai1202/Humanizer-zh-TW](https://github.com/kevintsai1202/Humanizer-zh-TW)

這些工具可以協助讓文字更自然，但不能取代事實查核。雇主、日期、數據、職責歸屬、資格與聯絡資訊，都應以原始資料為依據。

## 範例

- [輸入範例](examples/sample-input.md)
- [HTML 輸出範例](examples/sample-output/resume.html)
- [範例說明](examples/README.md)

範例內容皆為虛構資料，僅用於展示預期的輸入與輸出格式。範例明確要求兩頁，並指定商業感 navy／steel blue 配色；這組顏色不是 Skill 的預設值。

## 安裝

### 方式一：在 ChatGPT 建立個人 Skill

個人使用不需要先將此 Repo 發佈為 Plugin。ChatGPT 可以直接建立或上傳自訂的個人 Skill。請依照官方 [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) 流程操作：

1. 在 ChatGPT 側邊欄選擇 **Plugins**。
2. 在 Plugin Directory 開啟 **Skills** 分頁。
3. 選擇 **Create**，再選擇 **Upload from your computer**。
4. 上傳完整的 `skills/html-resume/` Skill 套件。請讓 `SKILL.md`、`agents/` 與 `references/` 保持在一起，確保所有指示與支援資源都能使用。
5. ChatGPT 完成安全掃描後，安裝 Skill。上傳既有履歷並使用下方的**路徑一**，或提供職涯資料並使用**路徑二**。

也可以選擇 **Create with chat** 或 **Create with editor**，並將此 Repo 作為建立 Skill 的參考來源。個人 Skills 目前主要適用於 ChatGPT Business、Enterprise、Healthcare 與 Edu；Enterprise 與 Edu 工作區可能需要管理員先啟用 Skills 與 Skill 上傳權限。個人 Skills 必須分別加入桌面版與 web／mobile，這些使用介面之間不會自動同步。

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

#### 選用：使用 MarkItDown 擷取既有 PDF

若本地 Agent 無法直接讀取上傳的 PDF，可以使用 [Microsoft MarkItDown](https://github.com/microsoft/markitdown) 將履歷擷取為適合 LLM 讀取的 Markdown。使用 uv 將 PDF 支援安裝成隔離的命令列工具：

```bash
uv tool install 'markitdown[pdf]'
markitdown path/to/existing-resume.pdf -o existing-resume.md
```

請將產生的 Markdown 提供給 Agent，並在可行時一併提供原始 PDF。MarkItDown 只負責協助讀取來源，不是最終履歷轉換工具；姓名、日期、數據、連結與章節順序仍應對照原始檔案確認。純圖片或掃描型 PDF 可能需要額外的 OCR（光學字元辨識）步驟。

### 方式三：使用 uv 建立 PDF 轉換環境

此 Repo 已提供 `pyproject.toml` 與 `uv.lock`，用於管理 Playwright PDF 轉換工具的依賴。完成 [uv 安裝](https://docs.astral.sh/uv/getting-started/installation/)後，建立專案環境並安裝 Chromium：

```bash
uv sync
uv run playwright install chromium
```

`uv sync` 會建立本機 `.venv`，並安裝 lockfile 鎖定的 Python 依賴；Chromium 則由 Playwright 另外管理。

## 使用方式

### 路徑一：從求職平台履歷或既有 PDF 開始

若 Agent 支援 PDF 輸入，請直接上傳原始履歷；若本地工作流程無法直接讀取 PDF，可先依照上方說明使用 MarkItDown 轉換。來源與輸出都可以是中文或英文，並支援雙向翻譯。

```text
使用 $html-resume，將我上傳的求職平台履歷或既有 PDF，製作成一份由我自行維護、可持續修改的 A4 HTML 履歷。
輸出語言使用［英文／繁體中文／簡體中文］；來源語言不同時請進行翻譯。
請保留雇主、職稱、日期、數據、技能、聯絡資訊與原意，使用自然且適合招募者閱讀的方式重寫，不要逐句硬翻。遇到模糊或缺少的資訊時先詢問我，不得自行虛構。
請依內容決定頁數，並使用［偏好的配色］。
同時匯出並驗證 PDF。
```

### 路徑二：從職涯資料開始

也可以用既有的職涯文字明確呼叫 Skill：

```text
Use $html-resume to create a polished A4 HTML resume from the attached career history.
Use a professional navy and steel-blue palette.
```

或直接用自然語言描述需求：

```text
Turn this work history into a PDF-ready HTML resume for an AI application engineer.
Choose the page count based on the strength and amount of content.
Use English section headings with concise Traditional Chinese content where appropriate.
Use a charcoal and muted teal color palette.
```

Skill 不會強制套用預設履歷顏色。請在提示中自行指定偏好的配色或品牌方向；如果沒有指定，Agent 應先詢問你要使用的顏色，再開始套用視覺樣式。

產生文件前，請提供或確認以下資訊：

- 目標文件類型。
- 來源語言、輸出語言與目標讀者。
- 目標職位或定位。
- 頁數偏好或硬性限制（如有）。
- 必要章節。
- 色彩配置或品牌方向。
- 是否提供頭像或個人照片。
- 僅需 HTML，或同時需要 HTML 與 PDF。

## 匯出 PDF

建議使用 [`html_to_pdf.py`](html_to_pdf.py)，透過 **Playwright（瀏覽器自動化工具）+ Chromium（Chrome 核心瀏覽器引擎）** 進行轉換。腳本會讓 Chromium 開啟本機 HTML，再呼叫 `page.pdf()`，並設定：

- `print_background=True`
- `prefer_css_page_size=True`
- `format="A4"`

因此 CSS 裡的 `@page { size: A4; }`、以 `mm` 設定的尺寸與背景色，都能較忠實地保留。Chromium 會直接渲染 HTML 與 CSS，通常也會比經由 LibreOffice 文件版面模型轉換更穩定。

使用 Installation 段落建立的 uv 環境後，可執行：

```bash
uv run python html_to_pdf.py examples/sample-output/resume.html resume.pdf
```

若不使用 uv，也可以直接安裝 Playwright 與 Chromium，再以 Python 執行同一支腳本：

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
python3 html_to_pdf.py examples/sample-output/resume.html resume.pdf
```

輸出路徑可以省略；若未指定，腳本會在輸入 HTML 旁以相同檔名產生 PDF。

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
├── html_to_pdf.py               # 使用 Playwright 的 HTML 轉 PDF 工具
├── LICENSE
├── pyproject.toml               # Python 專案與 Playwright 依賴
├── README.md
├── README_zh.md
└── uv.lock                      # 可重現的 Python 依賴 lockfile
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
