"""Generate AirGun India 20 paired header + supplied banner previews.

Run from this folder with: python3 build_previews.py
Source header files 01–10 are left unchanged; new combinations are derivative previews.
"""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parent
COMBINATIONS = ROOT / "combinations"
COMBINATIONS.mkdir(exist_ok=True)

CONCEPTS = [
    ("Marketplace Command", "Search-led · Scarlet", "#d92a2c"),
    ("Blue Search Market", "Search-led · Cobalt", "#2563a3"),
    ("Plum Bazaar", "Bold · Plum", "#8a3c7c"),
    ("Crimson Split", "Split brand block", "#c92d33"),
    ("Night Ops", "Premium · Graphite", "#212933"),
    ("Royal Burgundy", "Refined · Burgundy", "#682838"),
    ("Festival Pop", "Promotional · Warm", "#f06037"),
    ("Industrial Grid", "Technical · Steel", "#466878"),
    ("Editorial Luxe", "Editorial · Ivory", "#a4725b"),
    ("Floating Pro", "Layered · Modern", "#292d42"),
    ("Linear Minimal", "Minimal · Cream", "#d62e28"),
    ("Red Flagship", "Retail · High contrast", "#eb312c"),
    ("Black Workshop", "Industrial · Dark", "#191e24"),
    ("Aurora Teal", "Center-logo · Teal", "#087b75"),
    ("Studio White", "Editorial · Underline", "#9a2525"),
    ("Copper Atelier", "Warm · Heritage", "#b06b36"),
    ("Crimson Ledger", "Category bar · Red", "#ce272b"),
    ("Graphite Labs", "Square-cut · Carbon", "#38424b"),
    ("Blush Commerce", "Soft · Rounded", "#bf4a54"),
    ("Tactical Ultra", "Navy · Utility", "#17364e"),
]

ICON = {
    "search": '<circle cx="10.5" cy="10.5" r="6.4"/><path d="m16 16 5 5"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "user": '<circle cx="12" cy="8" r="3.5"/><path d="M5 21c.2-4.3 2.9-6.2 7-6.2s6.8 1.9 7 6.2"/>',
    "cart": '<path d="M3 5h2l2.5 12h12l2-9H6"/><circle cx="9.2" cy="21" r="1"/><circle cx="18" cy="21" r="1"/>',
    "heart": '<path d="M20.8 8.5c0 4.8-8.8 10.6-8.8 10.6S3.2 13.3 3.2 8.5a4.8 4.8 0 0 1 8.8-2.7 4.8 4.8 0 0 1 8.8 2.7Z"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M12 1v5m0 12v5M1 12h5m12 0h5"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M5 5l2.2 2.2m9.6 9.6L19 19M19 5l-2.2 2.2m-9.6 9.6L5 19"/>',
    "cube": '<path d="m12 2 9 5-9 5-9-5 9-5Zm-9 5v10l9 5 9-5V7M12 12v10"/>',
    "pen": '<path d="m4 18 13-13 3 3-13 13H4zM14 8l3 3"/>',
}


def svg(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>'


NAV_ITEMS = [
    ("Home", "/"), ("AGI Products", "/shop/"), ("Shop", "/shop/"),
    ("Technology", "#technology"), ("Shooting", "#shooting"),
    ("OEM & ODM", "#oem-odm"), ("Distributor", "#distributor"),
    ("Support", "/contact/"), ("Blogs", "/blog/"), ("About", "/about-us/"),
]


def new_header(n):
    links = "".join(f'<a href="{url}">{html.escape(label)}</a>' for label, url in NAV_ITEMS)
    return f'''<header class="agi-new agi-new--{n}" role="banner">
      <div class="nh-top"><div class="nh-shell"><span>DESIGNED &amp; MADE IN INDIA <strong>◆</strong> PRECISION AIRGUN ENGINEERING</span><span class="nh-toplinks"><a href="/contact/">Contact AGI</a><a href="/my-account/">My account</a></span></div></div>
      <div class="nh-shell nh-main">
        <details class="nh-mobile"><summary aria-label="Open navigation menu">{svg('menu')}</summary><nav class="nh-mobile-menu" aria-label="Mobile navigation">{links}</nav></details>
        <a href="/" class="nh-logo" aria-label="AirGun India homepage"><img src="../assets/airgun-india-horizontal-logo.png" alt="AirGun India original logo" width="1676" height="421"></a>
        <form class="nh-search" action="/" method="get" role="search"><input aria-label="Search airgun products" name="s" type="search" placeholder="Search AGI products, accessories..." required><input type="hidden" name="post_type" value="product"><button type="submit" aria-label="Search">{svg('search')}</button></form>
        <div class="nh-actions"><a class="nh-action" href="/my-account/" aria-label="My account">{svg('user')}<span>Account</span></a><a class="nh-action" href="#wishlist" aria-label="Wishlist">{svg('heart')}<span>Wishlist</span></a><a class="nh-action nh-action--cart" href="/cart/" aria-label="Shopping cart">{svg('cart')}<span>Cart</span></a></div>
      </div>
      <div class="nh-navwrap"><nav class="nh-shell nh-nav" aria-label="Main navigation">{links}</nav></div>
    </header>'''


BENEFITS = [
    ("pen", "Design & Development"),
    ("gear", "Precision Manufacturing"),
    ("target", "Shooting Technology"),
    ("cube", "OEM / Private Label"),
]


def main_content(n, label):
    perks = "".join(f'<div class="agi-benefits__item"><span class="agi-benefits__icon">{svg(icon)}</span><span>{text}</span></div>' for icon, text in BENEFITS)
    return f'''<main class="agi-page" id="main-content">
      <div id="agiBannerStudio"><section class="agi-hero" aria-label="AGI Terminator air rifle banner fallback">
        <img class="agi-hero__image" src="../assets/agi-terminator-banner.png" width="2048" height="1152" alt="AGI Terminator PCP air rifle, supplied original promotional banner" loading="eager" decoding="async">
      </section></div>
      <section class="agi-benefits" aria-label="AGI capabilities">{perks}</section>
      <div class="agi-preview-footer"><strong>{n:02d} — {html.escape(label)}</strong> · Visual header + original AGI Terminator banner concept. For preview and selection only; not a ready-to-activate WordPress theme or plugin.</div>
    </main>'''


def document(n, title, header):
    css = f'<link rel="stylesheet" href="../css/header-{SOURCE[n - 1]}.css">' if n <= 10 else '<link rel="stylesheet" href="../css/new-headers.css">'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#ffffff"><title>AGI Concept {n:02d} — {html.escape(title)} + Terminator Banner Studio</title>{css}<link rel="stylesheet" href="../css/combo.css"><link rel="stylesheet" href="../css/compact-header.css"><link rel="stylesheet" href="../css/banner-studio.css"><script src="../js/banner-studio.js" defer></script></head><body>
{header}
{main_content(n, title)}
</body></html>
'''


header_files = sorted((ROOT / "headers").glob("header-*.html"))
assert len(header_files) == 10, f"Expected ten original headers; got {len(header_files)}"
SOURCE = [f.name.removeprefix("header-").removesuffix(".html") for f in header_files]

for n, (title, _, _) in enumerate(CONCEPTS, 1):
    if n <= 10:
        original = header_files[n - 1].read_text(encoding="utf-8")
        match = re.search(r'<header\b[^>]*class="agi-header[^>]*>.*?</header>', original, re.S)
        if not match:
            raise RuntimeError(f"Cannot find header in {header_files[n - 1]}")
        header = match.group(0)
        is_square = "agi-brand__logo--square" in header
        logo_file = "airgun-india-square-logo.png" if is_square else "airgun-india-horizontal-logo.png"
        header, replaced = re.subn(r'src="data:image/png;base64,[^"]+"', f'src="../assets/{logo_file}"', header)
        if replaced != 1:
            raise RuntimeError(f"Expected one logo in concept {n}, found {replaced}")
    else:
        header = new_header(n)
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    (COMBINATIONS / f"{n:02d}-{slug}.html").write_text(document(n, title, header), encoding="utf-8")

items_js = ",\n".join(
    f"  {{id:{n},title:{title!r},tag:{tag!r},color:{color!r},url:'combinations/{n:02d}-{re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')}.html'}}"
    for n, (title, tag, color) in enumerate(CONCEPTS, 1)
)

INDEX = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>AirGun India — Header &amp; Banner Concepts</title><style>
 :root{font-family:Inter,Arial,Helvetica,sans-serif;color-scheme:dark;background:#0c1018;color:#f0f3f8}
 *{box-sizing:border-box} body{margin:0;overflow-x:hidden}
 button,select{font:inherit}button{cursor:pointer}a{color:inherit}
 .app{display:grid;grid-template-columns:294px minmax(0,1fr);min-height:100vh}
 .sidebar{background:#121824;border-right:1px solid #273040;padding:23px 16px;position:sticky;top:0;height:100vh;display:flex;flex-direction:column;gap:18px;min-width:0}
 .brand{display:flex;align-items:center;gap:12px}.brand img{width:47px;height:47px;object-fit:contain;background:#fff;border-radius:10px;padding:4px}.brand b{font-size:15px}.brand small{font-size:10px;color:#9ea9b8;display:block;letter-spacing:.14em;margin-top:4px}
 .sidebar h1{font-size:22px;line-height:1.15;letter-spacing:-.7px;margin:5px 0}.sidebar .muted{font-size:12px;color:#98a5b8;line-height:1.6;margin:0}
 .tabs{display:grid;grid-template-columns:1fr 1fr;gap:6px}.tab{border:1px solid #2d3747;border-radius:8px;background:#1a2230;color:#a4b4c8;font-size:11px;padding:10px}.tab[aria-selected=true]{background:#d42b29;border-color:#d42b29;color:#fff;font-weight:750}
 .design-list{display:grid;gap:6px;overflow-y:auto;min-height:0;padding:0 3px 15px 0;scrollbar-color:#424c5f transparent}
 .design{display:flex;width:100%;text-align:left;gap:11px;align-items:center;padding:10px;border:1px solid transparent;border-radius:11px;background:transparent;color:#e2e8ef}.design:hover{background:#1c2532}.design[aria-current=true]{background:#252d3a;border-color:#d42b29;box-shadow:inset 3px 0 #d42b29}.swatch{display:block;width:37px;height:37px;border-radius:9px;flex:0 0 auto;box-shadow:inset 0 0 0 6px #ffffff14}.design b{font-size:12px;display:block;margin-bottom:5px}.design small{font-size:10px;color:#91a0b4}.badge{font-size:9px;color:#e6c9a9;border:1px solid #5b4530;border-radius:100px;padding:4px 7px;margin-left:auto;flex-shrink:0}
 .sidebar-footer{font-size:10px;color:#8995a9;border-top:1px solid #293243;padding-top:12px;line-height:1.6}
 .workspace{min-width:0;display:flex;flex-direction:column}
 .toolbar{display:flex;justify-content:space-between;align-items:center;gap:18px;padding:18px 26px;border-bottom:1px solid #293445;background:#101622;position:sticky;top:0;z-index:5;flex-wrap:wrap}
 .toolbar h2{font-size:17px;margin:0 0 4px;letter-spacing:-.3px}.toolbar p{font-size:11px;margin:0;color:#8ea0b7}
 .controls{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
 .btn,.choice{border:1px solid #344154;border-radius:8px;background:#1a2533;color:#d7dfea;padding:10px 13px;font-size:12px;font-weight:700;min-height:38px}
 .choice.active{background:#d72e2b;color:white;border-color:#d72e2b}.btn:hover,.choice:hover{border-color:#d14c48}
 .viewer-wrap{padding:29px 22px 60px;overflow:hidden;min-width:0;text-align:center;background:radial-gradient(ellipse at 50% -20%,#273046 0,#141c2a 65%,#111824 100%);flex:1}
 .frame-label{font-size:12px;letter-spacing:.12em;color:#aebdd0;margin-bottom:14px;text-transform:uppercase;display:flex;justify-content:center;gap:12px}
 .browser{margin:0 auto;width:min(100%,1440px);background:#fff;border:1px solid #455164;border-radius:14px;overflow:hidden;box-shadow:0 35px 75px #0007;transition:width .28s ease}
 .browser-bar{height:38px;background:#e9ebef;display:flex;align-items:center;justify-content:space-between;padding:0 15px;color:#626f7a;font-size:11px;gap:15px}
 .dots{display:flex;gap:6px}.dots i{width:9px;height:9px;border-radius:50%;background:#ff655d}.dots i:nth-child(2){background:#ffb739}.dots i:nth-child(3){background:#2bc66d}
 .browser-address{background:#d6dae0;padding:5px 18px;border-radius:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:70%}
 iframe{border:0;background:#fff;display:block;width:100%;height:calc(100vh - 215px);min-height:650px}
 .browser.tablet{width:768px;max-width:100%}.browser.mobile{width:390px;max-width:100%}
 .browser.mobile iframe{height:760px;min-height:0}.browser.tablet iframe{height:890px;min-height:0}
 .viewer-notes{max-width:900px;text-align:left;margin:20px auto;color:#a3afbf;font-size:12px;line-height:1.7}
 .viewer-notes strong{color:#f6f8fb}
 .bottom-controls{display:flex;justify-content:center;gap:10px;margin-top:15px;flex-wrap:wrap}
 .mobile-sidebar-toggle{display:none}
 @media(max-width:950px){.app{grid-template-columns:235px minmax(0,1fr)}.sidebar{padding:15px 10px}.toolbar{padding:15px}.viewer-wrap{padding:20px 12px 50px}.toolbar h2{font-size:15px}}
 @media(max-width:700px){.app{display:block}.sidebar{position:static;height:auto;border-right:0;padding:13px 15px;gap:8px}.sidebar h1,.sidebar .muted,.sidebar .tabs,.sidebar-footer{display:none}.brand img{height:36px;width:36px}.mobile-sidebar-toggle{display:block;margin-left:auto;border:1px solid #384456;color:#fff;background:#252e3c;border-radius:7px;padding:7px 11px;font-size:12px}.design-list{display:none;grid-template-columns:repeat(2,1fr);max-height:380px;padding-top:10px}.design-list.open{display:grid}.design{padding:8px}.design b{font-size:11px}.swatch{width:26px;height:26px}.badge{display:none}.toolbar{position:static}.controls{width:100%}.btn,.choice{padding:9px 11px}.browser-bar{height:28px}.browser-address{max-width:65%}.viewer-wrap{padding:15px 8px 40px}.viewer-notes{padding:0 10px}.frame-label{font-size:10px}.browser iframe{height:740px;min-height:0}}
 /* Client presentation theme: slim controls, bright neutral workspace, wider preview. */
 :root{color-scheme:light;background:#f5f6f8;color:#202936}
 .app{grid-template-columns:220px minmax(0,1fr)}
 .sidebar{background:#fff;border-right:1px solid #e8ebef;padding:15px 10px;gap:13px}
 .brand{gap:9px;padding:0 5px}.brand img{width:34px;height:34px;border:1px solid #f0f0f1;border-radius:7px;padding:2px}.brand b{font-size:12px;letter-spacing:.03em;color:#202936}.brand small{font-size:9px;letter-spacing:.13em;margin-top:3px;color:#8e9aa8}
 .sidebar h1{font-size:12px;margin:4px 5px 0;letter-spacing:.04em;color:#747e8b;text-transform:uppercase}.sidebar .muted,.sidebar-footer{display:none}
 .tabs{gap:3px;padding:3px;background:#f4f5f6;border-radius:7px}
 .tab{background:transparent;border:0;color:#737c88;font-size:10px;padding:8px 5px;border-radius:5px;font-weight:650}.tab[aria-selected=true]{background:#fff;color:#c92d2a;border:0;box-shadow:0 1px 4px #00000011}
 .design-list{gap:2px;padding:0 0 12px;scrollbar-color:#d6dbe3 transparent}
 .design{padding:9px 8px;gap:8px;border-radius:7px;color:#394352;min-height:40px}
 .design:hover{background:#f5f6f9}.design[aria-current=true]{background:#fff1ef;border-color:#f4c5c1;box-shadow:inset 3px 0 #d3312a;color:#a7201d}
 .swatch{width:20px;height:20px;border-radius:5px;box-shadow:inset 0 0 0 3px #ffffff25}.design b{font-size:11px;margin:0;font-weight:760;line-height:1.28}.design small,.badge{display:none}
 .toolbar{padding:10px 18px;min-height:62px;background:#fff;border-bottom:1px solid #e8ebef;gap:10px}
 .toolbar h2{font-size:15px;color:#222b38;margin:0 0 3px}.toolbar p{font-size:10px;color:#9aa3af}
 .controls{gap:5px}.btn,.choice{min-height:34px;padding:8px 11px;font-size:11px;background:#f7f8fa;color:#526072;border-color:#e5e8ee;border-radius:7px}
 .choice.active{background:#d3332c;color:#fff;border-color:#d3332c}.btn:hover,.choice:hover{border-color:#d3332c}
 .banner-select{appearance:auto;max-width:236px;min-width:172px;height:34px;padding:0 11px;border:1px solid #e0e5eb;border-radius:7px;background:#fff;color:#313c49;font-size:11px;font-weight:700;outline-offset:3px;margin-right:5px;cursor:pointer}
 .viewer-wrap{background:#f5f6f8;padding:17px 16px 30px}.frame-label{display:none}
 .browser{border:1px solid #dde2e9;border-radius:10px;box-shadow:0 12px 34px #202d4212}
 .browser-bar{height:26px;background:#f0f1f4;color:#8b96a3;padding:0 12px}.dots i{width:7px;height:7px}.browser-address{background:#e5e8ed;font-size:10px;padding:4px 13px}
 iframe{height:calc(100vh - 151px);min-height:650px}
 .viewer-notes{max-width:1100px;text-align:center;margin:11px auto;font-size:10px;color:#9ca5b2}.viewer-notes strong{color:#646f7f}
 .bottom-controls{margin-top:10px;gap:7px}
 .mobile-sidebar-toggle{background:#fff;color:#394657;border-color:#e2e6ec}
 @media(max-width:950px){.app{grid-template-columns:205px minmax(0,1fr)}.sidebar{padding:12px 8px}.toolbar{padding:9px 10px}.banner-select{max-width:180px;min-width:150px}}
 @media(max-width:700px){.app{display:block}.sidebar{position:static;height:auto;padding:9px 12px;gap:7px;border-right:0;border-bottom:1px solid #e8ebef}.brand img{height:31px;width:31px}.sidebar h1,.sidebar .muted{display:none}.sidebar .tabs{display:grid;margin-top:3px}.mobile-sidebar-toggle{display:block;color:#364353;background:#f7f8fa;border-color:#e0e4e9;font-size:10px;padding:6px 9px}.design-list{display:none;grid-template-columns:repeat(2,1fr);max-height:310px}.design-list.open{display:grid}.design{min-height:34px}.toolbar{position:static;gap:9px;padding:9px 10px}.toolbar h2{font-size:13px}.controls{width:100%;gap:4px;flex-wrap:wrap}.banner-select{max-width:100%;min-width:160px;flex:1;margin-right:0}.btn,.choice{font-size:10px;min-height:32px;padding:7px 9px}.viewer-wrap{padding:9px 7px 20px}.browser{border-radius:7px}.browser-bar{height:24px}.browser-address{font-size:9px}.browser iframe{height:740px;min-height:0}.viewer-notes{font-size:9px;padding:0 8px}}
</style></head><body><div class="app"><aside class="sidebar"><div class="brand"><img src="assets/airgun-india-square-logo.png" alt="AirGun India logo"><div><b>AIRGUN INDIA</b><small>DESIGN EXPLORER</small></div><button class="mobile-sidebar-toggle" id="toggleList" aria-expanded="false" aria-controls="designList">All designs ▾</button></div><div><h1>20 header + banner combinations</h1><p class="muted">Ten original header concepts, ten new compositions. All paired with your AGI Terminator banner.</p></div><div class="tabs"><button class="tab" data-filter="original" aria-selected="true">01–10 Original</button><button class="tab" data-filter="new" aria-selected="false">11–20 New</button></div><nav class="design-list" id="designList" aria-label="Choose navigation design"></nav><div class="sidebar-footer">Visual-only prototype · Uses supplied original AGI logos and original Terminator banner.<br>Works offline after unzipping.</div></aside><main class="workspace"><header class="toolbar"><div><h2 id="activeTitle">01 / Marketplace Command</h2><p id="activeTag">Search-led · Scarlet</p></div><div class="controls" role="group" aria-label="Preview screen width"><button class="choice active" data-mode="desktop" aria-pressed="true">Desktop</button><button class="choice" data-mode="tablet" aria-pressed="false">Tablet</button><button class="choice" data-mode="mobile" aria-pressed="false">Mobile</button><a class="btn" id="openFull" href="#" target="_blank" rel="noopener">↗ Full page</a></div></header><div class="viewer-wrap"><div class="frame-label"><span id="viewportLabel">Desktop preview · adaptive width</span><span>● Banner included</span></div><div class="browser" id="browser"><div class="browser-bar"><div class="dots"><i></i><i></i><i></i></div><span class="browser-address">dev.airgunsofindia.com — visual concept</span><span>↗</span></div><iframe id="preview" title="AirGun India navigation and banner concept preview" loading="eager"></iframe></div><div class="bottom-controls"><button class="btn" id="prev">← Previous design</button><button class="btn" id="next">Next design →</button></div><p class="viewer-notes"><strong>How to use:</strong> Pick any design and switch Desktop / Tablet / Mobile. You can open its full page separately. The original 10 headers are preserved; the new 10 explore different combinations. Site links, WooCommerce cart totals, login state, and search results are illustrative until connected to WordPress/Flatsome. The banner itself is your supplied image.</p></div></main></div><script>
 const designs=[
__ITEMS__
 ];
 const sidebar=document.querySelector('.sidebar');
 const toolbar=document.querySelector('.toolbar');
 const brand=sidebar.querySelector('.brand');
 brand.querySelector('small')?.remove();
 brand.querySelector('.mobile-sidebar-toggle')?.remove();
 toolbar.prepend(brand);
 const list=document.createElement('nav');
 list.className='header-grid';list.setAttribute('aria-label','Choose one of 20 header concepts');
 toolbar.after(list);
 sidebar.remove();
 const frame=document.getElementById('preview'), browser=document.getElementById('browser');
 const bannerNames=['Classic duo','Product quad','Editorial rail','Catalogue stack','Featured mosaic','Premium four-up','Asymmetric spotlight','Slim product rail','Outlined grid','Dark showcase'];
 const shortNames=['Market','Blue','Plum','Split','Night','Royal','Festival','Industrial','Editorial','Floating','Linear','Flagship','Workshop','Teal','Studio','Copper','Ledger','Graphite','Blush','Tactical'];
 let current=1,mode='desktop',banner=1;
 const bannerSelect=document.createElement('select');bannerSelect.className='banner-select';bannerSelect.setAttribute('aria-label','Banner layout');bannerSelect.title='Choose one of 10 hero banner layouts';
 bannerNames.forEach((name,i)=>{const option=document.createElement('option');option.value=String(i+1);option.textContent='Banner '+String(i+1).padStart(2,'0')+' · '+name;bannerSelect.append(option)});
 document.querySelector('.controls').prepend(bannerSelect);
 bannerSelect.addEventListener('change',()=>{banner=Number(bannerSelect.value);select(current)});
 document.querySelector('.viewer-notes').innerHTML='<strong>Design preview only.</strong> Product cards, menu links and live cart features will be connected during WordPress implementation.';
 document.querySelector('.browser-address').textContent='AIRGUN INDIA / HOMEPAGE CONCEPT';
 document.getElementById('openFull').textContent='↗ Open';
 function renderList(){list.textContent='';for(const d of designs){const b=document.createElement('button');b.className='header-chip';b.type='button';b.setAttribute('aria-label',String(d.id).padStart(2,'0')+' — '+d.title);b.setAttribute('title',d.title);b.setAttribute('aria-current',String(d.id===current));const dot=document.createElement('i');dot.className='header-chip__dot';dot.style.background=d.color;const n=document.createElement('b');n.textContent=String(d.id).padStart(2,'0');const label=document.createElement('span');label.className='header-chip__name';label.textContent=shortNames[d.id-1];b.append(dot,n,label);b.addEventListener('click',()=>select(d.id));list.append(b)}}
 function select(id){current=Math.max(1,Math.min(20,id));const d=designs[current-1];document.getElementById('activeTitle').textContent=String(current).padStart(2,'0')+' / '+d.title;document.getElementById('activeTag').textContent=d.tag;const path=d.url+'?banner='+String(banner).padStart(2,'0');frame.src=path;document.getElementById('openFull').href=path;bannerSelect.value=String(banner);try{history.replaceState(null,'','#design-'+String(current).padStart(2,'0')+'&banner-'+String(banner).padStart(2,'0'))}catch(e){}renderList()}
 function setMode(m){mode=m;browser.className='browser '+(mode==='desktop'?'':mode);document.querySelectorAll('[data-mode]').forEach(b=>{b.classList.toggle('active',b.dataset.mode===mode);b.setAttribute('aria-pressed',String(b.dataset.mode===mode))});document.getElementById('viewportLabel').textContent=mode==='desktop'?'Desktop preview · adaptive width':mode==='tablet'?'Tablet preview · 768px':'Mobile preview · 390px'}
 document.querySelectorAll('[data-mode]').forEach(b=>b.addEventListener('click',()=>setMode(b.dataset.mode)));
 document.getElementById('prev').addEventListener('click',()=>select(current===1?20:current-1));document.getElementById('next').addEventListener('click',()=>select(current===20?1:current+1));
 document.addEventListener('keydown',e=>{if(e.target.matches('input,button,select,textarea'))return;if(e.key==='ArrowLeft')select(current===1?20:current-1);if(e.key==='ArrowRight')select(current===20?1:current+1)});
 const requested=Number((location.hash.match(/design-(\d{1,2})/)||[])[1]);const requestedBanner=Number((location.hash.match(/banner-(\d{1,2})/)||[])[1]);banner=requestedBanner>=1&&requestedBanner<=10?requestedBanner:1;select(requested>=1&&requested<=20?requested:1);
 </script></body></html>'''

index_html = INDEX.replace("__ITEMS__", items_js).replace('<small>DESIGN EXPLORER</small>', '')
index_html = index_html.replace('</style></head>', '</style><link rel="stylesheet" href="css/dashboard-top-grid.css"></head>')
(ROOT / "index.html").write_text(index_html, encoding="utf-8")
(ROOT / "preview-all-20.html").write_text(index_html, encoding="utf-8")
print(f"Generated {len(list(COMBINATIONS.glob('*.html')))} combinations and preview-all-20.html")
