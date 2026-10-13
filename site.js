/* Společný skript webu PREMIUM 60: menu + vykreslení prodejců z prodejci.js */
(function () {
  'use strict';
  var nav = document.getElementById('navbar');
  if (nav) {
    window.addEventListener('scroll', function () { nav.classList.toggle('scrolled', window.scrollY > 40); });
    var t = document.getElementById('navToggle');
    if (t) t.addEventListener('click', function () { nav.classList.toggle('open'); });
  }
  var y = document.querySelectorAll('.cy');
  for (var i = 0; i < y.length; i++) y[i].textContent = new Date().getFullYear();

  var P = window.PRODEJCI || [];
  var kc = function (n) { return n.toLocaleString('cs-CZ').replace(/\s/g, ' ') + ' Kč'; };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var tel = function (s) { return 'tel:' + String(s).replace(/[^+0-9]/g, ''); };

  /* karty prodejců */
  function card(p) {
    var c = [];
    if (p.adresa) c.push('<div>📍 ' + (p.mapa ? '<a href="' + esc(p.mapa) + '" target="_blank" rel="noopener">' + esc(p.adresa) + '</a>' : esc(p.adresa)) + '</div>');
    if (p.telefon) c.push('<div>📞 <a href="' + tel(p.telefon) + '">' + esc(p.telefon) + '</a>' + (p.telefonDoba ? ' <span>· ' + esc(p.telefonDoba) + '</span>' : '') + '</div>');
    if (p.whatsapp) c.push('<div>💬 <a href="https://wa.me/' + esc(p.whatsapp) + '" target="_blank" rel="noopener">WhatsApp</a></div>');
    if (p.email) c.push('<div>✉️ <a href="mailto:' + esc(p.email) + '">' + esc(p.email) + '</a></div>');
    if (p.web) c.push('<div>🌐 <a href="' + esc(p.web) + '" target="_blank" rel="noopener">' + esc(p.web.replace(/^https?:\/\//, '').replace(/\/$/, '')) + '</a></div>');
    return '<article class="p-dealer" id="' + esc(p.id) + '">' +
      '<div class="p-dealer-main"><div class="p-dealer-top">' + (p.logo ? '<img src="' + esc(p.logo) + '" alt="' + esc(p.nazev) + '">' : '') +
      '<div>' + (p.kraj ? '<span class="p-dealer-kraj">' + esc(p.kraj) + '</span>' : '') + '<h3>' + esc(p.nazev) + '</h3>' + (p.podtitul ? '<small>' + esc(p.podtitul) + '</small>' : '') + '</div></div>' +
      '<div class="p-dealer-contact">' + c.join('') + '</div>' +
      (p.oblast && p.oblast.length ? '<p class="p-dealer-area"><b>Montáž:</b> ' + p.oblast.map(esc).join(', ') + '</p>' : '') +
      (p.provozovatel ? '<p class="p-dealer-area">Provozovatel: ' + esc(p.provozovatel) + '</p>' : '') + '</div>' +
      '<div class="p-dealer-side">' +
      (p.akce ? '<a class="p-dealer-akce" href="' + esc(p.akce) + '" target="_blank" rel="noopener"><b>Místní akce</b><span>Aktuální akční cenu PREMIUM 60 v tomto kraji najdete u prodejce →</span></a>' : '') +
      (p.vyhody && p.vyhody.length ? '<b class="p-dealer-sidehead">Služby prodejce</b>' : '') +
      (p.vyhody && p.vyhody.length ? '<ul>' + p.vyhody.map(function (v) { return '<li>' + esc(v) + '</li>'; }).join('') + '</ul>' : '') +
      '<div class="p-dealer-btns">' + (p.poptavka ? '<a class="btn btn-primary" href="' + esc(p.poptavka) + '" target="_blank" rel="noopener">Poptávka u prodejce</a>' : '') +
      (p.telefon ? '<a class="btn btn-outline" href="' + tel(p.telefon) + '">Zavolat</a>' : '') + '</div></div></article>';
  }
  document.querySelectorAll('[data-prodejci]').forEach(function (el) {
    el.innerHTML = P.length ? P.map(card).join('') : '<p>Seznam prodejců připravujeme.</p>';
  });
  document.querySelectorAll('[data-kraje]').forEach(function (el) {
    el.innerHTML = P.map(function (p) { return '<a href="kde-koupit.html#' + esc(p.id) + '">' + esc(p.kraj) + '</a>'; }).join('');
  });
  document.querySelectorAll('[data-pocet-prodejcu]').forEach(function (el) {
    var n = P.length; el.textContent = n + (n === 1 ? ' prodejce' : (n < 5 ? ' prodejci' : ' prodejců'));
  });
})();
