/* Ten banner compositions; no network calls, third-party libraries or tracking. */
(() => {
  const host = document.getElementById('agiBannerStudio');
  if (!host) return;
  const requested = Number(new URLSearchParams(location.search).get('banner'));
  const variant = requested >= 1 && requested <= 10 ? requested : 1;
  const svg = (paths) => `<svg viewBox="0 0 96 96" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${paths}</svg>`;
  const icons = {
    precision: svg('<circle cx="48" cy="48" r="29"/><circle cx="48" cy="48" r="13"/><path d="M48 5v22m0 42v22M5 48h22m42 0h22"/>'),
    gear: svg('<path d="m48 10 8 9 12-2 3 12 12 5-4 13 7 11-10 9-1 13-13 1-10 9-10-9-13-1-1-13-10-9 7-11-4-13 12-5 3-12 12 2z"/><circle cx="48" cy="48" r="15"/>'),
    rifle: svg('<path d="M9 52h58l14-14h6l-10 17-14 5H48l-5 22H24l10-23H9z"/><path d="M27 42h28l6 10M43 42l-2-13h24v13M61 29h8"/>'),
    fill: svg('<rect x="30" y="30" width="35" height="49" rx="6"/><path d="M39 30V17h16v13M47 17V8M23 58h-6v13h13"/><circle cx="47" cy="52" r="11"/><path d="m47 52 5-5"/>'),
    box: svg('<path d="m48 9 33 18-33 18-33-18 33-18Zm-33 18v40l33 20 33-20V27M48 45v42M33 18l33 19"/>'),
    scope: svg('<circle cx="48" cy="48" r="31"/><circle cx="48" cy="48" r="18"/><path d="M48 8v22m0 36v22M8 48h22m36 0h22"/><circle cx="48" cy="48" r="3"/>'),
  };
  const products = [
    { name:'AARYA Mk3 Air Rifle', eyebrow:'PCP AIR RIFLES', subtitle:'AGI platform', tone:'charcoal',icon:'rifle' },
    { name:'AGI Tactical Chassis', eyebrow:'PRECISION COMPONENTS', subtitle:'Engineered accessories', tone:'red',icon:'gear' },
    { name:'AARYA STX Regulated', eyebrow:'FEATURED PRODUCTS', subtitle:'Precision range', tone:'blue',icon:'precision' },
    { name:'PCP Filling Systems', eyebrow:'AIRGUN FILLING', subtitle:'Explore the category', tone:'mint',icon:'fill' },
    { name:'Shooting Accessories', eyebrow:'ESSENTIAL EQUIPMENT', subtitle:'Explore the collection', tone:'cream',icon:'box' },
    { name:'Optics & Accessories', eyebrow:'SPORT SHOOTING', subtitle:'Explore the category', tone:'plum',icon:'scope' },
  ];
  const styles = [
    { name:'Classic duo', items:[0,1] },
    { name:'Product quad', items:[0,1,2,3] },
    { name:'Editorial rail', items:[2,4,5] },
    { name:'Catalogue stack', items:[0,1,3,4] },
    { name:'Featured mosaic', items:[1,0,5] },
    { name:'Premium four-up', items:[2,1,4,3] },
    { name:'Asymmetric spotlight', items:[0,4] },
    { name:'Slim product rail', items:[0,1,2,5] },
    { name:'Outlined grid', items:[2,3,4,5] },
    { name:'Dark showcase', items:[0,1] },
  ];
  const selection = styles[variant - 1];
  function card(product) {
    return `<a class="ab-card ab-card--${product.tone}" href="/shop/" aria-label="Browse ${product.name}">
      <div class="ab-card__head"><span class="ab-card__eyebrow">${product.eyebrow}</span><strong>${product.name}</strong><span class="ab-card__subtitle">${product.subtitle}</span></div>
      <div class="ab-card__media">${icons[product.icon]}</div>
      <div class="ab-card__tail"><span>EXPLORE COLLECTION</span><span aria-hidden="true">↗</span></div>
    </a>`;
  }
  host.innerHTML = `<section class="ab-studio ab-layout-${String(variant).padStart(2,'0')}" aria-label="Homepage hero with ${selection.name} product cards">
    <div class="ab-stage"><div class="ab-feature">
      <div class="ab-feature__visual"><img src="../assets/agi-terminator-banner.png" alt="AGI Terminator PCP air rifle promotional banner supplied by AirGun India" width="2048" height="1152" loading="eager" decoding="async"></div>
      <div class="ab-feature__bar"><span><b>AGI TERMINATOR</b><small>PCP air rifle · Designed and made in India</small></span><a class="ab-feature__button" href="/shop/">VIEW COLLECTION <span aria-hidden="true">↗</span></a></div>
    </div><div class="ab-cards">${selection.items.map(id => card(products[id])).join('')}</div></div>
    <div class="ab-info-row" aria-label="Product specifications"><span>4.55 mm / .177 cal</span><i aria-hidden="true"></i><span>PCP Air Rifle</span><i aria-hidden="true"></i><span>975 FPS</span><i aria-hidden="true"></i><span>Under 20 Joules</span></div>
  </section>`;
})();
