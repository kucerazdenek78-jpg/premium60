# Web PREMIUM 60 – pravidla

Komunikace: česky, neformálně, důsledně, nic si nevymýšlet (ověřovat, co nevím, říct to).

## Co to je
Samostatný web bezpečnostních dveří PREMIUM 60 (výrobce GERDA). Provozuje ho Zdeněk Kučera (Bezpečné dveře)
jako prodejce – **není to oficiální web výrobce** (upozornění je v patičce, nechat ho tam).
Zatím jediný prodejce Bezpečné dveře; další prodejci přibudou.

## Struktura
- `src/*.html` = obsah stránek. **Needitovat přímo HTML v kořeni** – po změně v `src/` spustit `python3 tools/sestav.py`
  (doplní hlavičku, menu, patičku, sitemap.xml a robots.txt).
- `tools/sestav.py`: `BASE` = adresa webu (při přechodu na vlastní doménu změnit + přidat soubor CNAME),
  `VER` = verze CSS/JS (zvýšit při každé změně `*.css` / `*.js`).
- `prodejci.js` = seznam prodejců (karty na úvodu a na Kde koupit, cena v hero). Nový prodejce = nový blok.
- `style.css` = kopie základu z bezpecne-dvere.cz, `premium.css` = vzhled tohoto webu.
- `poptavka.js` = **kopie** `poptavka-dvere.js` z repa bezpecne-dvere (jen PREMIUM 60, rozdíly označené `PREMIUM60:`).
  `poptavka-pdf/` = kopie stejnojmenné složky. Když se v bezpecne-dvere změní ceny/volby PREMIUM 60 nebo formulář,
  přenést změnu i sem (a naopak). Poptávky jdou na kucerazd@kksystem.cz + kopie chci@bezpecne-dvere.cz,
  v předmětu „(web PREMIUM 60)“ a pole „Zdroj“. Odkaz „Vytvořit objednávku“ vede na bezpecne-dvere.cz/objednavka-dvere.html.
- Fotky dekorů, schéma čepů a kování jsou výřezy z `dokumenty/letak-premium-60.pdf`.

## Údaje o dveřích
Zdroj pravdy = `dvere-do-bytu.html` na bezpecne-dvere.cz (sekce #premium60). Při rozporu s letákem
použít web a upozornit Zdenka.

## Konvence
- Statické HTML, GitHub Pages, větev `main`. Hover efekty jen v `@media (hover:hover)`.
- Po změně: Playwright screenshot (desktop + 390 px), žádný horizontální scroll, žádné 404. Commity česky.
