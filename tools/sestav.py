#!/usr/bin/env python3
"""Sestaví stránky webu PREMIUM 60: src/*.html (obsah) + společná hlavička a patička → *.html v kořeni.
Spuštění z kořene repa:  python3 tools/sestav.py
Hlavička souboru v src/ (první řádek) je JSON v komentáři:
<!-- {"title": "...", "description": "...", "nav": "index", "css": "...", "scripts": ["..."]} -->
Při přechodu na vlastní doménu stačí změnit BASE (a doplnit soubor CNAME)."""
import json, re, pathlib, subprocess, datetime

BASE = 'https://premium60.cz/'
VER = '20261014a'                                            # zvýšit při změně CSS/JS
ROOT = pathlib.Path(__file__).resolve().parent.parent

NAV = [('index.html#parametry', 'Parametry', 'parametry'),
       ('index.html#dekory', 'Dekory', 'dekory'), ('kde-koupit.html', 'Kde koupit', 'kde-koupit'),
       ('servis-a-dokumenty.html', 'Servis a dokumenty', 'servis')]

HEAD = '''<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="cs_CZ">
  <meta property="og:site_name" content="PREMIUM 60">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{base}img/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Bezpečnostní dveře PREMIUM 60 – RC3, EI 60, 42 dB">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{base}img/og-image.jpg">
  <meta name="theme-color" content="#efe8de">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="icon" href="favicon-32.png" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">{preload}
  <link rel="stylesheet" href="style.css?v={ver}">
  <link rel="stylesheet" href="premium.css?v={ver}">{css}{robots}{jsonld}
</head>
<body>

<nav class="navbar" id="navbar">
  <div class="container">
    <div class="nav-inner">
      <a href="index.html" class="nav-logo nav-logo-word" aria-label="PREMIUM 60 – úvod">PREMIUM <b>60</b><small>RC3 · EI 60</small></a>
      <ul class="nav-menu" id="navMenu">
{nav}
      </ul>
      <div style="display:flex;align-items:center;gap:0.75rem;">
        <a href="kde-koupit.html" class="btn btn-primary" style="padding:0.6rem 1.2rem;font-size:0.85rem;">Kde koupit</a>
      </div>
      <button class="nav-toggle" id="navToggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>
'''

FOOT = '''
<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="nav-logo-word" style="color:#fff;padding:0 0 .6rem">PREMIUM <b>60</b></a>
        <p>Bezpečnostní bytové dveře RC3 s protipožární odolností EI 60. Výrobce GERDA.</p>
      </div>
      <div class="footer-col">
        <h5>Dveře</h5>
        <div class="footer-links">
          <a href="index.html#parametry">Technické parametry</a>
          <a href="index.html#dekory">Dekory</a>
          <a href="index.html#sestava">Co je v sestavě</a>
          <a href="index.html#certifikace">Certifikace</a>
          <a href="index.html#vyrobce">O výrobci GERDA</a>
        </div>
      </div>
      <div class="footer-col">
        <h5>Nákup</h5>
        <div class="footer-links">
          <a href="kde-koupit.html">Kde koupit</a>
          <a href="kde-koupit.html#stat-se-prodejcem">Stát se prodejcem</a>
        </div>
      </div>
      <div class="footer-col">
        <h5>Servis</h5>
        <div class="footer-links">
          <a href="servis-a-dokumenty.html">Servis a dokumenty</a>
          <a href="dokumenty/premium-60-letak.pdf" target="_blank" rel="noopener">Leták PREMIUM 60 (PDF)</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom" style="flex-direction:column;align-items:flex-start;gap:.6rem">
      <p class="p-disclaimer">PREMIUM 60 vyrábí GERDA Sp. z o.o. (Polsko). Tento web provozuje prodejce, nejde o oficiální web výrobce. Ceny, montáž a záruční podmínky určuje vždy konkrétní prodejce, který dveře i servisuje.</p>
      <span>© <span class="cy">2026</span> Provozovatel webu: Zdeněk Kučera, IČ 64682676, DIČ CZ7801242768, Zd. Štěpánka 2764/1, 434 01 Most</span>
    </div>
  </div>
</footer>

<script src="prodejci.js?v={ver}"></script>
<script src="site.js?v={ver}"></script>{scripts}
</body>
</html>
'''


def prodejci():
    """Načte prodejce z prodejci.js (přes node)."""
    js = "global.window={};require(process.argv[1]);console.log(JSON.stringify(window.PRODEJCI))"
    return json.loads(subprocess.check_output(['node', '-e', js, str(ROOT / 'prodejci.js')], text=True))


def clean_links(html):
    """Interní odkazy na úvod vedou na ./ (shodně s canonical), ne na index.html."""
    return html.replace('href="index.html#', 'href="./#').replace('href="index.html"', 'href="./"')


def jsonld(name, meta, url):
    """Strukturovaná data schema.org pro vyhledávače – jen ověřené údaje z webu."""
    if meta.get('noindex'):
        return []
    P = prodejci()
    crumbs = {'@type': 'BreadcrumbList', '@context': 'https://schema.org', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'PREMIUM 60', 'item': BASE}]}
    if name != 'index.html':
        crumbs['itemListElement'].append({'@type': 'ListItem', 'position': 2, 'name': meta['title'].split(' – ')[0], 'item': url})
    out = [crumbs]
    if name == 'index.html':
        out.append({'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'PREMIUM 60', 'url': BASE, 'inLanguage': 'cs'})
        out.append({
            '@context': 'https://schema.org', '@type': 'Product', 'name': 'PREMIUM 60',
            'description': 'Bezpečnostní dveře do bytu v bezpečnostní třídě RC3 s požární odolností EI 60, odhlučněním 42 dB a certifikací NBÚ ČR. Komplet s bezpečnostní zárubní, prahem, kováním, vložkou a kukátkem.',
            'brand': {'@type': 'Brand', 'name': 'GERDA'},
            'manufacturer': {'@type': 'Organization', 'name': 'GERDA Sp. z o.o.', 'url': 'https://gerda.pl/cs/'},
            'category': 'Bezpečnostní dveře do bytu',
            'image': [BASE + 'img/og-image.jpg', BASE + 'img/premium60-dvere.webp', BASE + 'img/rez-dveri.webp'],
            'color': 'Ořech, Dub, Světlé wenge, Bílá, Černá perleť, Antracit',
            'additionalProperty': [
                {'@type': 'PropertyValue', 'name': 'Bezpečnostní třída', 'value': 'RC3'},
                {'@type': 'PropertyValue', 'name': 'Požární odolnost', 'value': 'EI 60'},
                {'@type': 'PropertyValue', 'name': 'Odhlučnění', 'value': '42 dB'},
                {'@type': 'PropertyValue', 'name': 'Tloušťka křídla', 'value': '60 mm'},
                {'@type': 'PropertyValue', 'name': 'Tloušťka plechu', 'value': '1,2 mm'},
                {'@type': 'PropertyValue', 'name': 'Tepelná propustnost', 'value': '1,2 W/m²K'},
                {'@type': 'PropertyValue', 'name': 'Certifikace', 'value': 'NBÚ ČR, Trezor test s.r.o.'}],
            'offers': {'@type': 'AggregateOffer', 'priceCurrency': 'CZK', 'lowPrice': 42500, 'highPrice': 42500,
                       'offerCount': len(P), 'availability': 'https://schema.org/InStock',
                       'description': 'Cena kompletu vč. montáže na klíč a 12 % DPH. Prodejci mohou mít místní akce.'}})
        faq = re.findall(r'<summary>(.*?)</summary><p>(.*?)</p>', (ROOT / 'src' / name).read_text(encoding='utf-8'))
        if faq:
            out.append({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
                {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': re.sub(r'<[^>]+>', '', a).replace('&nbsp;', ' ')}}
                for q, a in faq]})
    if name == 'kde-koupit.html':
        items = []
        for i, p in enumerate(P, 1):
            street, city = [x.strip() for x in p['adresa'].split(',', 1)]
            psc, mesto = city[:6], city[7:]
            biz = {'@type': 'LocalBusiness', 'name': p['nazev'], 'url': p.get('web'), 'telephone': p.get('telefon'),
                   'email': p.get('email'), 'areaServed': p['kraj'],
                   'address': {'@type': 'PostalAddress', 'streetAddress': street, 'postalCode': psc,
                               'addressLocality': mesto, 'addressCountry': 'CZ'}}
            items.append({'@type': 'ListItem', 'position': i, 'item': {k: v for k, v in biz.items() if v}})
        out.append({'@context': 'https://schema.org', '@type': 'ItemList', 'name': 'Prodejci PREMIUM 60', 'itemListElement': items})
    return out


def prerender():
    """Vykreslí karty prodejců, mapu a legendu do statického HTML (kvůli vyhledávačům); site.js je pak jen obnoví."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print('Prerender přeskočen (chybí playwright).'); return
    sel = ['[data-prodejci]', '[data-map-legend]', '[data-servis]', '[data-kraje]', '.p-map']
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page()
        for f in sorted(ROOT.glob('*.html')):
            pg.goto(f.as_uri(), wait_until='load')
            html = f.read_text(encoding='utf-8')
            for s in sel:
                for el in pg.query_selector_all(s):
                    outer = el.evaluate('e => e.outerHTML')
                    tag = el.evaluate('e => e.tagName.toLowerCase()')
                    attr = s.strip('[]') if s.startswith('[') else 'class="p-map"'
                    m = re.search(r'<' + tag + r'[^>]*' + re.escape(attr) + r'[^>]*>(?:</' + tag + '>)?', html)
                    if s == '.p-map':
                        m = re.search(r'<svg class="p-map".*?</svg>', html, re.S)
                    if m:
                        html = html[:m.start()] + outer + html[m.end():]
            f.write_text(html, encoding='utf-8')
        b.close()
    print('Prerender: prodejci a mapa vloženi do HTML.')


def build():
    out = []
    for src in sorted((ROOT / 'src').glob('*.html')):
        text = src.read_text(encoding='utf-8')
        m = re.match(r'<!--\s*(\{.*?\})\s*-->\n', text, re.S)
        meta = json.loads(m.group(1)); body = text[m.end():]
        name = src.name
        if '<!--MAPA-->' in body:
            body = body.replace('<!--MAPA-->', (ROOT / 'tools' / 'mapa-kraju.svg').read_text(encoding='utf-8'))
        url = BASE + ('' if name == 'index.html' else name)
        nav = '\n'.join('        <li class="nav-item"><a href="{h}" class="nav-link{a}">{t}</a></li>'.format(
            h=h, t=t, a=' active' if meta.get('nav') == k else '') for h, t, k in NAV)
        css = ('\n  <style>\n' + meta['css'] + '\n  </style>') if meta.get('css') else ''
        robots = '\n  <meta name="robots" content="noindex">' if meta.get('noindex') else '\n  <meta name="robots" content="index, follow, max-image-preview:large">'
        preload = ('\n  <link rel="preload" as="image" href="' + meta['preload'] + '" fetchpriority="high">') if meta.get('preload') else ''
        ld = jsonld(name, meta, url)
        jsonld_html = ''.join('\n  <script type="application/ld+json">' + json.dumps(x, ensure_ascii=False, separators=(',', ':')) + '</script>' for x in ld)
        scripts = ''.join('\n<script src="{}"></script>'.format(s.replace('{ver}', VER)) for s in meta.get('scripts', []))
        html = HEAD.format(title=meta['title'], description=meta['description'], url=url, base=BASE, ver=VER,
                           css=css, robots=robots, nav=nav, preload=preload, jsonld=jsonld_html) + body + FOOT.format(ver=VER, scripts=scripts)
        html = clean_links(html)
        (ROOT / name).write_text(html, encoding='utf-8')
        if not meta.get('noindex'):
            out.append(url)
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    today = datetime.date.today().isoformat()
    sm += ['  <url><loc>{}</loc><lastmod>{}</lastmod></url>'.format(u, today) for u in out] + ['</urlset>', '']
    (ROOT / 'sitemap.xml').write_text('\n'.join(sm), encoding='utf-8')
    (ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: {}sitemap.xml\n'.format(BASE), encoding='utf-8')
    print('Sestaveno:', ', '.join(p.name for p in sorted((ROOT / 'src').glob('*.html'))))
    prerender()


if __name__ == '__main__':
    build()
