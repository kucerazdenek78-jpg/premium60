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
