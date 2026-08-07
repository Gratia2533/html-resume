#!/usr/bin/env python3
"""Convert a local HTML document to PDF with Playwright and Chromium."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a local HTML file to an A4 PDF with Playwright."
    )
    parser.add_argument("input_html", type=Path, help="Path to the source HTML file")
    parser.add_argument(
        "output_pdf",
        nargs="?",
        type=Path,
        help="Path to the output PDF (defaults to the input filename with .pdf)",
    )
    return parser.parse_args()


def html_to_pdf(input_html: Path, output_pdf: Path | None = None) -> Path:
    input_path = input_html.expanduser().resolve(strict=True)
    if not input_path.is_file():
        raise ValueError(f"input is not a file: {input_path}")
    if input_path.suffix.lower() not in {".html", ".htm"}:
        raise ValueError(f"input must be an HTML file: {input_path}")

    output_path = (
        output_pdf.expanduser().resolve()
        if output_pdf is not None
        else input_path.with_suffix(".pdf")
    )
    if output_path.suffix.lower() != ".pdf":
        raise ValueError(f"output must use a .pdf extension: {output_path}")

    try:
        from playwright.sync_api import Error as PlaywrightError
        from playwright.sync_api import sync_playwright
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "Playwright is not installed. Run 'uv sync' or "
            "'python3 -m pip install playwright'."
        ) from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            try:
                page = browser.new_page()
                page.goto(input_path.as_uri(), wait_until="networkidle")
                page.evaluate("() => document.fonts.ready")
                page.wait_for_function(
                    "() => Array.from(document.images).every((image) => image.complete)"
                )

                failed_images = page.evaluate(
                    """() => Array.from(document.images)
                        .filter((image) => image.naturalWidth === 0)
                        .map((image) => image.currentSrc || image.src)"""
                )
                if failed_images:
                    raise RuntimeError(
                        "HTML contains images that Chromium could not load: "
                        + ", ".join(failed_images)
                    )

                page.pdf(
                    path=str(output_path),
                    print_background=True,
                    prefer_css_page_size=True,
                    format="A4",
                )
            finally:
                browser.close()
    except PlaywrightError as exc:
        raise RuntimeError(
            "Playwright could not render the PDF. "
            "Install Chromium with 'uv run playwright install chromium' or "
            "'python3 -m playwright install chromium'. "
            f"Details: {exc}"
        ) from exc

    return output_path


def main() -> int:
    args = parse_args()
    try:
        output_path = html_to_pdf(args.input_html, args.output_pdf)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
