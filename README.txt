AIRGUN INDIA — ORIGINAL 10 E-COMMERCE HEADER CONCEPTS
=============================================

NEW: To view all 20 header + AGI Terminator banner combinations, open index.html.
See README-20-COMBINATIONS.txt for details. The below notes describe the
preserved original ten header-only prototypes.

OPEN preview-all-10.html in Chrome or Safari to see all 10 concepts.
Use Desktop / Tablet / Mobile controls to view responsive layouts.

FILES
-----
headers/    Complete standalone HTML previews (HTML + CSS included).
embed/      Copy-paste HTML including a <style> block for a prototype (one header per file).
css/        Separate CSS for each design (recommended for a proper implementation).

THE 10 DESIGNS
--------------
01 Marketplace Command — marketplace search hierarchy, strong red
02 Blue Search Market — blue-led search-focused marketplace
03 Plum Bazaar — rich purple/magenta accents
04 Crimson Split — strong red brand panel
05 Night Ops — graphite/dark premium
06 Royal Burgundy — burgundy + champagne
07 Festival Pop — orange-red promotional gradient
08 Industrial Grid — technical slate + teal
09 Editorial Luxe — premium ivory + burgundy
10 Floating Pro — modern pill-container header

IMPORTANT INTEGRATION NOTES
---------------------------
1. The designs are responsive visual prototypes, not pre-wired Flatsome header templates.
2. Original AirGun India logos are already included (square: designs 01, 04, 07; horizontal: all other designs).
3. Replace all #category-anchor placeholders with your REAL category URLs.
4. The search form uses normal WordPress product search: GET /?s=query&post_type=product
5. /my-account/ and /cart/ are standard WooCommerce routes, but verify your page URLs.
6. Live cart quantity/total, AJAX search suggestions, user login state, and wishlist
   require Flatsome/WooCommerce native widgets, PHP/WPCode hooks, or plugin integration.
7. Do not show a second header under Flatsome's existing header in production.
8. Safest approach for existing Flatsome Classic installations:
   - Backup dev and test on dev only.
   - Use Flatsome > Theme Options > Header or Header Designer to reproduce the chosen
     design using the native Logo, Search, Account, Cart and Mobile Menu elements.
   - Apply CSS as a custom class or through WPCode (CSS Snippet).
   - Keep Flatsome's dynamic cart, search, menus and sticky header behaviour.
9. If prototyping by insertion, do it on a TEST PAGE with a custom HTML widget first.
10. Avoid directly replacing parent theme files, as updates can overwrite changes.
11. Logo images have been embedded in HTML as data URIs, so previews work offline.
    For production, upload the provided assets/ images to WordPress Media Library
    and replace the data: image src with your new WordPress Media URLs.
12. Logo colors/identity are unchanged; white logo plates provide contrast on dark bars.

Inspired by broad e-commerce UX patterns (Amazon-like utility hierarchy,
Flipkart-like search prominence, Meesho-like vivid colour), NOT copied site code.
