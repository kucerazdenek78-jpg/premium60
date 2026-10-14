# Web PREMIUM 60 – pravidla

Komunikace: česky, neformálně, důsledně, nic si nevymýšlet (ověřovat, co nevím, říct to).

## Co to je
Samostatný **produktový web** bezpečnostních dveří PREMIUM 60 (výrobce GERDA, Polsko). Není to web GERDA ani web prodejce.
- **Žádná poptávka, objednávka ani akce na webu.** Jen pevná cena kompletu **42 500 Kč** vč. montáže a 12 % DPH.
  Poptávky, objednávky a místní akce mají prodejci u sebe – web na ně odkazuje z karty prodejce.
- **Značku Bezpečné dveře nikde neuvádět**, jen v kartě prodejce pro Ústecký kraj (`prodejci.js`).
  V patičce zůstává jen „Provozovatel webu: Zdeněk Kučera, IČ…“ (povinný údaj) a že nejde o oficiální web výrobce.
- **Servis** (záruka, reklamace, klíče) dělá vždy prodejce, u kterého zákazník dveře koupil – stránka servisu jen vypisuje prodejce.
- Mapa krajů (`tools/mapa-kraju.svg`, vkládá ji `sestav.py` místo `<!--MAPA-->`) se vybarví podle `prodejci.js`
  (`kraj`, případně `mapa_kraje`). Středočeský kraj je na mapě jen zčásti: kruh 95 km vzdušně od Mostu (≈ 120 km po silnici), cesta `data-kraj="Středočeský kraj – do 120 km od Mostu"`. Zdroj hranic: github.com/siwekm/czech-geojson (kraje.json), zjednodušeno.
- Výbava „Základ / Na přání“ (#vybava) je z gerda.pl/cs (PREMIUM 60), **bez balíčku ELITE**.
- GERDA a její ocenění (sekce #vyrobce) jen jako informace o výrobci. Ocenění ověřena z budownictwo.org (10/2026).

## Struktura
- `src/*.html` = obsah stránek. **Needitovat přímo HTML v kořeni** – po změně v `src/` spustit `python3 tools/sestav.py`
  (doplní hlavičku, menu, patičku, sitemap.xml a robots.txt).
- `tools/sestav.py`: `BASE` = adresa webu (https://premium60.cz/, doména u Forpsi, soubor CNAME),
  `VER` = verze CSS/JS (zvýšit při každé změně `*.css` / `*.js`).
- `prodejci.js` = seznam prodejců po krajích (karty na úvodu a na Kde koupit). Nový prodejce = nový blok.
- `style.css` = kopie základu z bezpecne-dvere.cz, `premium.css` = vzhled tohoto webu (barvy podle loga GERDA: #0b263c).
- Leták `dokumenty/premium-60-letak.pdf` je bez značky prodejce (místo na razítko). Zdroj `tools/letak.html`,
  PDF vytvoří `python3 tools/letak.py`.
- Fotky dekorů, schéma čepů a kování jsou výřezy z původního letáku Bezpečných dveří (bez loga).

## SEO
- `sestav.py` generuje meta tagy (title ≤ 65 znaků, description ≤ 160), Open Graph/Twitter, `robots`, sitemap s `lastmod`
  a JSON-LD: BreadcrumbList všude, na úvodu WebSite + Product (cena 42 500 Kč) + FAQPage (z `<details>` v sekci #otazky),
  na Kde koupit ItemList prodejců (LocalBusiness) z `prodejci.js`.
- Po sestavení `prerender()` (Playwright) vloží karty prodejců, mapu a legendu přímo do HTML, aby je vyhledávače viděly bez JS.
- Interní odkazy na úvod jsou `./` (ne `index.html`), shodně s canonical.
- Obrázky: velké fotky ve WebP, všechny `<img>` mají width/height; písmo Inter přes `<link>` (ne @import).
- FAQ jen z ověřených údajů na webu – nic nepřidávat bez zdroje.

## Údaje o dveřích
Zdroj pravdy = `dvere-do-bytu.html` na bezpecne-dvere.cz (sekce #premium60). Při rozporu s letákem
použít web a upozornit Zdenka.

## Konvence
- Statické HTML, GitHub Pages, větev `main`. Hover efekty jen v `@media (hover:hover)`.
- Po změně: Playwright screenshot (desktop + 390 px), žádný horizontální scroll, žádné 404. Commity česky.
