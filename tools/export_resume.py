"""Build the downloadable CV and verify its PDF link annotations.

Requires playwright (with Chromium installed) and pypdf at export time only.
Run from any directory: python tools/export_resume.py
"""

from pathlib import Path
from urllib.parse import urljoin

from playwright.sync_api import sync_playwright
from pypdf import PdfReader


def main():
    root = Path(__file__).resolve().parents[1]
    output = root / "assets/krishna-kankipati-resume.pdf"
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto((root / "cv.html").as_uri(), wait_until="networkidle")
        canonical = page.locator('link[rel="canonical"]').get_attribute("href")
        assert canonical and canonical.startswith("https://")
        page.evaluate("document.fonts.ready")
        assert page.locator(".portrait").evaluate(
            "image => image.complete && image.naturalWidth > 0"
        ), "Portrait did not load"
        # Printed project links must open the public site, never local files.
        for anchor in page.locator("a[href]").all():
            anchor.evaluate(
                "(anchor, url) => anchor.href = url",
                urljoin(canonical, anchor.get_attribute("href")),
            )
        page.emulate_media(media="print")
        expected = set(page.locator("a[href]").evaluate_all(
            "anchors => anchors.filter(a => a.getClientRects().length)"
            ".map(a => a.href)"
        ))
        page.pdf(
            path=str(output), prefer_css_page_size=True,
            print_background=True, tagged=True,
        )
        browser.close()

    reader = PdfReader(output)
    destinations = set()
    for pdf_page in reader.pages:
        for annotation in pdf_page.get("/Annots", []):
            action = annotation.get_object().get("/A", {})
            if action.get("/S") == "/URI":
                destinations.add(str(action["/URI"]))
    assert expected <= destinations, f"Missing PDF links: {expected - destinations}"
    assert all(url.startswith("https://") for url in destinations), destinations
    print(f"Exported {len(reader.pages)} pages with {len(destinations)} verified link destinations: {output}")


if __name__ == "__main__":
    main()
