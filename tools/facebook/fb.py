#!/usr/bin/env python3
"""Vyfotí grafiku pro Facebook z fb.html do složky zadané argumentem (výchozí: tools/facebook/out)."""
import sys, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE / 'out'); out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 1700, 'height': 1000})
    pg.goto((HERE / 'fb.html').as_uri(), wait_until='load'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
    for i, name in [('profil', 'premium60-fb-profilova.png'), ('titulka', 'premium60-fb-titulni.jpg'), ('prispevek', 'premium60-fb-prispevek.jpg')]:
        el = pg.locator('#' + i)
        el.screenshot(path=str(out / name), **({'type': 'jpeg', 'quality': 92} if name.endswith('.jpg') else {}))
    b.close()
print('hotovo', out)
