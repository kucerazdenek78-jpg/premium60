#!/usr/bin/env python3
"""Vytvoří dokumenty/premium-60-letak.pdf z tools/letak.html (Playwright, A4). Spuštění z kořene repa."""
import asyncio, pathlib
from playwright.async_api import async_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.goto((ROOT / 'tools' / 'letak.html').as_uri(), wait_until='load')
        (ROOT / 'dokumenty').mkdir(exist_ok=True)
        await pg.pdf(path=str(ROOT / 'dokumenty' / 'premium-60-letak.pdf'), format='A4', print_background=True, margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'})
        await b.close()
asyncio.run(main())

# název PDF pro vyhledávače
from pypdf import PdfReader, PdfWriter
_f = ROOT / 'dokumenty' / 'premium-60-letak.pdf'
_r = PdfReader(str(_f)); _w = PdfWriter()
for _p in _r.pages: _w.add_page(_p)
_w.add_metadata({'/Title': 'PREMIUM 60 – bezpečnostní dveře do bytu RC3, EI 60', '/Subject': 'Leták PREMIUM 60, výrobce GERDA', '/Keywords': 'PREMIUM 60, bezpečnostní dveře, RC3, EI 60, GERDA'})
_w.write(str(_f))
