AIRGUN INDIA — 20 HEADER + AGI TERMINATOR BANNER COMBINATIONS
==============================================================

START HERE
----------
1. Extract this entire ZIP to a normal folder.
2. Open index.html (or preview-all-20.html) in Chrome, Safari, or Firefox.
3. Click any of the 20 designs on the left.
4. Use the compact Banner dropdown to mix each header with 10 layouts.
5. Use Desktop, Tablet, or Mobile to compare the responsive layouts.
6. Click "Open" to view a specific combination separately.
7. If you prefer, open combinations/01-marketplace-command.html?banner=02 etc.
   directly, changing banner=01 through banner=10.

The gallery and all 20 designs are designed to work OFFLINE. No website
admin access, installation, or external assets are required.

CLIENT SHARING / GITHUB PAGES
-----------------------------
The design explorer now has a minimal light dashboard with NO left sidebar.
The 20 header options appear in a compact two-row grid along the top, with
the banner dropdown and device options in the slim toolbar. This leaves much
more room for the actual website preview. The subtitle under the logo has
been removed. For GitHub Pages see GITHUB-PAGES-SETUP.txt in this folder.

YOUR ORIGINAL TEN DESIGNS (PRESERVED)
-------------------------------------
01 Marketplace Command — search-focused red e-commerce
02 Blue Search Market — blue search-led marketplace
03 Plum Bazaar — purple and magenta
04 Crimson Split — split red brand panel
05 Night Ops — charcoal dark premium
06 Royal Burgundy — burgundy and champagne
07 Festival Pop — energetic orange-red
08 Industrial Grid — technical steel tones
09 Editorial Luxe — restrained ivory and burgundy
10 Floating Pro — floating pill surface

TEN ADDITIONAL DESIGNS
----------------------
11 Linear Minimal — cream strip and rounded search
12 Red Flagship — retail red and black category navigation
13 Black Workshop — full dark industrial header
14 Aurora Teal — centered logo, left search, right actions
15 Studio White — editorial menu, underlined search
16 Copper Atelier — heritage timber/copper warmth
17 Crimson Ledger — full red category bar
18 Graphite Labs — geometric graphite and aqua
19 Blush Commerce — soft blush and pill navigation
20 Tactical Ultra — navy / precision red

All combinations include:
- Your supplied 2048 x 1152 AGI TERMINATOR AIR RIFLE banner, unchanged.
- The original AirGun India logos from your original ZIP.
- A capabilities strip (Design, Manufacturing, Shooting Technology, OEM).
- Responsive navigation and search; 11–20 have a usable mobile menu.
- Extra mobile text beneath the banner for key specs readability.

NEW MINIMAL / COMPACT UPDATE
----------------------------
- Shorter, calmer headers: approximately 130px desktop across common designs,
  with compact logo, search, actions and navigation.
- Compact mobile versions remove the top promotional bar.
- Ten selectable homepage banner compositions combined with all 20 headers.
  This gives 200 header × banner pairings without duplicating 200 pages.

THE TEN BANNER LAYOUTS
----------------------
B01 Classic Duo        — hero left + 2 stacked product cards right
B02 Product Quad       — hero left + 2x2 product grid right
B03 Editorial Rail     — hero left + 3 horizontal product rows right
B04 Catalogue Stack    — hero left + 4 compact stacked product rows right
B05 Featured Mosaic    — hero left + one wide and two mini product cards
B06 Premium Four-Up    — hero left + 4 spacious premium tiles
B07 Asymmetric         — hero left + two different-height products right
B08 Slim Product Rail  — hero left + 4 very compact collection strips
B09 Outlined Grid      — hero left + 4 outlined category tiles
B10 Dark Showcase      — hero left + 2 dark premium product cards

Products represented: AARYA Mk3, AARYA STX, AGI Tactical Chassis,
PCP Filling Systems and Shooting Accessories. Card artwork is vector concept
illustration, NOT verified catalogue photography. Replace card artwork and
URLs with real WooCommerce product images/links during integration.

FOLDER GUIDE
------------
index.html, preview-all-20.html — same visual explorer.
combinations/                — all twenty complete header+banner pages.
headers/                     — untouched original header-only previews.
embed/                       — untouched original header-only embed snippets.
css/header-*.css             — original ten separated stylesheets.
css/new-headers.css          — styles for designs 11–20.
css/combo.css                — shared banner and responsive strip.
css/compact-header.css       — shared smaller header sizing for all 20.
css/banner-studio.css        — ten different card/banner layouts.
js/banner-studio.js          — local banner selector renderer for each page.
assets/                      — original AGI logos and AGI Terminator banner.
preview-all-10.html          — preserved older navigation-only preview.
build_previews.py            — regenerates the twenty combinations.

WORDPRESS / WOOCOMMERCE / FLATSOME INTEGRATION NOTES
---------------------------------------------------
- These are STATIC VISUAL PROTOTYPES, not a plugin or installable theme.
- No code or content on dev.airgunsofindia.com is changed.
- Product search uses WooCommerce GET ?s=...&post_type=product, but
  local-file searching needs an actual WooCommerce installation.
- Menu destinations marked #... are demonstration placeholders.
- Live cart amounts, wishlists, login state, AJAX suggestions, sticky header
  and real menu URLs require WordPress/Flatsome integration.
- Keep WooCommerce/Flatsome header functionality and never render a duplicate
  header on the live website.
- Recommended implementation: pick one design, back up dev, then reproduce it
  with Flatsome Header Designer and isolated custom-plugin CSS/JS.
- Never directly edit Flatsome parent theme files.

RESPONSIVE NOTES
----------------
- New designs switch to mobile navigation at 850px; existing originals
  retain their original 900px responsive logic.
- The original banner image stays complete at all sizes. Detailed embedded
  image text is tiny on phones; a readable specs strip is included below.
- Explorer preview widths: Desktop adaptive, Tablet 768px, Mobile 390px.
- Responsive layouts also adjust to actual browser width outside explorer.
