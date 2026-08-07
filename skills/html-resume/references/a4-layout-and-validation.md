# A4 Layout and Validation Reference

Read this reference when building print CSS, exporting PDF, or checking a resume generated with the Skill.

## Contents

1. Exact page foundation
2. Top and bottom color bands
3. Open Header patterns
4. PDF export
5. Validation workflow
6. Overflow recovery

## 1. Exact page foundation

Use explicit physical pages:

```css
@page {
  size: A4;
  margin: 0;
}

* {
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
}

body {
  background: var(--preview-bg);
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.resume-document {
  width: 210mm;
  margin: 0 auto;
}

.page {
  position: relative;
  width: 210mm;
  height: 297mm;
  margin: 10mm auto;
  padding: 14mm 15mm 18mm;
  overflow: hidden;
  background: var(--page-bg);
  break-after: page;
  page-break-after: always;
}

.page:last-child {
  break-after: auto;
  page-break-after: auto;
}

@media print {
  html,
  body {
    width: 210mm;
    background: var(--page-bg);
  }

  .resume-document {
    width: 210mm;
    margin: 0;
  }

  .page {
    margin: 0;
    box-shadow: none;
  }
}
```

Do not use viewport units or browser-dependent scaling. Keep the last body element above the footer safe area.

## 2. Top and bottom color bands

Derive colors from the user-approved palette:

```css
.top-band {
  position: absolute;
  inset: 0 0 auto;
  height: 7mm;
  background: linear-gradient(90deg, var(--primary-strong), var(--accent));
}

.footer-band {
  position: absolute;
  inset: auto 0 0;
  height: 10mm;
  padding: 0 15mm;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--primary-strong);
  color: var(--on-primary);
  font-size: 8pt;
  line-height: 1.2;
}
```

Use the same treatment on each page. Ensure `--on-primary` passes contrast checks against the footer background.

Footer markup:

```html
<footer class="footer-band">
  <span>{{candidate_name}} · {{target_role}}</span>
  <span>Page {{page_number}} / {{total_pages}}</span>
</footer>
```

Use either the candidate identity or concise contact information on the left. Never crowd the footer.

## 3. Open Header patterns

Do not add a Card around the portrait or Header.

First page:

```css
.identity-header {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 8mm;
  align-items: center;
  padding: 2mm 0 6mm;
  border-bottom: 1px solid var(--line);
}

.portrait {
  width: 33mm;
  height: 33mm;
  display: block;
  object-fit: cover;
  object-position: center;
  border-radius: 50%;
  border: 1.2mm solid var(--primary-soft);
}
```

Continuation pages:

```css
.continuation-header {
  display: flex;
  align-items: end;
  justify-content: space-between;
  padding: 1mm 0 4mm;
  margin-bottom: 5mm;
  border-bottom: 1px solid var(--line);
}
```

Keep backgrounds transparent. Use a monogram in the same open position when no portrait is available and a monogram improves balance.

## 4. PDF export

When working from this repository, use the Playwright-based `html_to_pdf.py` converter. Create the uv environment and install Chromium once:

```bash
uv sync
uv run playwright install chromium
```

Then convert the HTML:

```bash
uv run python html_to_pdf.py resume.html resume.pdf
```

The converter opens the local HTML in Chromium, waits for fonts and images, and calls `page.pdf()` with `print_background=True`, `prefer_css_page_size=True`, and `format="A4"`. This gives CSS `@page` declarations priority while preserving A4 as the fallback paper format. Do not enable browser-generated headers or footers.

If the repository converter is unavailable, implement the same settings with Playwright and Chromium rather than converting through an office document model.

## 5. Validation workflow

### Verify page size

Accept exact A4 dimensions:

```text
210 × 297 mm
595.28 × 841.89 points
```

Allow up to one point of rounding difference per dimension. Chromium may report approximately `594.96 × 841.92 points`.

Use `pdfinfo` or a PDF library. Reject the output if any page falls outside tolerance or the page count differs from the intended layout.

### Check browser overflow

Run in the rendered HTML:

```js
const pages = [...document.querySelectorAll(".page")];

const report = pages.map((page, index) => ({
  page: index + 1,
  clientHeight: page.clientHeight,
  scrollHeight: page.scrollHeight,
  overflow: page.scrollHeight > page.clientHeight
}));

console.table(report);
```

Also verify that the final content block on each page remains above the footer band.

### Render every page

Render all PDF pages to PNG and inspect:

- clipping and overlap
- awkward breaks or orphan headings
- excessive empty space
- footer collisions
- inconsistent margins or columns
- portrait crop and distortion
- text contrast and minimum size
- font rendering for every language used

### Validate text

Extract text from the PDF first. Use OCR only when rendered text may have disappeared, font embedding is uncertain, or the PDF contains rasterized text. OCR does not replace visual inspection.

## 6. Overflow recovery

Fix overflow in this order:

1. remove repetition
2. shorten weak bullets
3. reduce bullet count
4. move secondary content to the next page
5. tighten section spacing slightly
6. simplify decoration
7. reduce typography modestly without taking body text below `9pt`

Regenerate the PDF and repeat all checks after every layout revision.
