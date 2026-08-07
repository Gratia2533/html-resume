# Examples

This directory shows the intended contract between an agent and the `html-resume` Skill.

- `sample-input.md` contains fictional career information, an exact two-page requirement, and an explicit color direction.
- `sample-output/resume.html` is a self-contained, two-page, PDF-ready HTML document generated from that input. It uses a business-oriented navy and steel-blue palette; the palette demonstrates the request and is not a Skill default.

Open `sample-output/resume.html` in a browser to preview it, or export it with Chromium:

```bash
chromium --headless --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf=sample-output/resume.pdf \
  sample-output/resume.html
```

The example request does not require PDF delivery. If you export the optional PDF, verify its page count and A4 dimensions, render every page to PNG, and inspect the result before treating it as validated.
