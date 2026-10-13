#!/usr/bin/env python3
"""Sestaví stránky webu PREMIUM 60: src/*.html (obsah) + společná hlavička a patička → *.html v kořeni.
Spuštění z kořene repa:  python3 tools/sestav.py
Hlavička souboru v src/ (první řádek) je JSON v komentáři:
<!-- {"title": "...", "description": "...", "nav": "index", "css": "...", "scripts": ["..."]} -->
Při přechodu na vlastní doménu stačí změnit BASE (a doplnit soubor CNAME)."""
import json, re, pathlib

BASE = 'https://kucerazdenek78-jpg.github.io/premium60/'   # TODO: vlastní doména, např. https://premium60.cz/
VER = '20261013h'                                            # zvýšit při změně CSS/JS
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
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#0b263c">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css?v={ver}">
  <link rel="stylesheet" href="premium.css?v={ver}">{css}{robots}
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
        robots = '\n  <meta name="robots" content="noindex">' if meta.get('noindex') else ''
        scripts = ''.join('\n<script src="{}"></script>'.format(s.replace('{ver}', VER)) for s in meta.get('scripts', []))
        html = HEAD.format(title=meta['title'], description=meta['description'], url=url, base=BASE, ver=VER,
                           css=css, robots=robots, nav=nav) + body + FOOT.format(ver=VER, scripts=scripts)
        (ROOT / name).write_text(html, encoding='utf-8')
        if not meta.get('noindex'):
            out.append(url)
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += ['  <url><loc>{}</loc></url>'.format(u) for u in out] + ['</urlset>', '']
    (ROOT / 'sitemap.xml').write_text('\n'.join(sm), encoding='utf-8')
    (ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: {}sitemap.xml\n'.format(BASE), encoding='utf-8')
    print('Sestaveno:', ', '.join(p.name for p in sorted((ROOT / 'src').glob('*.html'))))


if __name__ == '__main__':
    build()
