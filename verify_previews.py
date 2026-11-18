"""Read-only checks of file integrity and combinations (no browser required)."""
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = []
        self.headers = 0
        self.banners = 0
        self.navs = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "header":
            self.headers += 1
        if tag == "nav":
            self.navs += 1
        if tag == "img" and "agi-hero__image" in attrs.get("class", ""):
            self.banners += 1
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.assets.append(attrs["href"])
        if tag == "img":
            self.assets.append(attrs["src"])


pages = sorted((ROOT / "combinations").glob("*.html"))
assert len(pages) == 20, f"Expected 20 pages, found {len(pages)}"
for n, page_path in enumerate(pages, 1):
    parsed = Page()
    page = page_path.read_text(encoding="utf-8")
    parsed.feed(page)
    assert page_path.name.startswith(f"{n:02d}-")
    assert parsed.headers == 1, page_path
    assert parsed.banners == 1, page_path
    assert parsed.navs >= 1, page_path
    assert "agi-terminator-banner.png" in page
    assert "agiBannerStudio" in page
    assert "banner-studio.js" in page
    assert "compact-header.css" in page
    assert "agi-benefits__item" in page
    assert "@media" in (ROOT / "css" / ("new-headers.css" if n > 10 else "combo.css")).read_text()
    if n > 10:
        assert "nh-mobile-menu" in page, page_path
    for asset in parsed.assets:
        if not asset.startswith(("data:", "https:", "http:")):
            assert (page_path.parent / asset).is_file(), (page_path, asset)

gallery = (ROOT / "index.html").read_text(encoding="utf-8")
assert gallery.count("url:'combinations/") == 20
assert "bannerNames=[" in gallery and "bannerSelect=document.createElement('select')" in gallery
assert "dashboard-top-grid.css" in gallery
assert "header-chip" in gallery and "header-grid" in gallery
assert "CLIENT PREVIEW" not in gallery
grid_css = (ROOT / "css" / "dashboard-top-grid.css").read_text(encoding="utf-8")
assert "grid-template-columns:repeat(10,minmax(0,1fr))" in grid_css
assert ".sidebar { display:none !important; }" in grid_css
assert "?banner=" in gallery
renderer = (ROOT / "js" / "banner-studio.js").read_text(encoding="utf-8")
for i in range(1, 11):
    assert f"ab-layout-{i:02d}" in (ROOT / "css" / "banner-studio.css").read_text(), i
assert renderer.count("items:[") == 10
assert 'data-mode="desktop"' in gallery and 'data-mode="mobile"' in gallery
assert (ROOT / "assets" / "agi-terminator-banner.png").is_file()
print("PASS: 20 unique pages, image/CSS paths, compact headers, 10 banner layouts and gallery choices")
print("NOTE: Visual browser QA could not be completed in this execution environment.")
