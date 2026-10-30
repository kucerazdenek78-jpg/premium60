# Voda Údlice

Odečty vodoměrů a roční vyúčtování vody pro společnou přípojku (parc. 1116/1-50, Údlice).

- Živá aplikace (data, odečty, WhatsApp): https://claude.ai/artifact/Tzww2hdonF3byEZuApDu17
- `aplikace/index.html` je zdrojový kód stránky. Data (odběratelé, období, odečty) jsou ve sdílené databázi aplikace na claude.ai, ne v tomto repozitáři.
- Mimo claude.ai se stránka otevře, ale bez dat („Data nejsou dostupná").

## Jak se počítá vyúčtování
- Spotřeba = konečný − počáteční stav podružného vodoměru.
- Cena: poměrně (faktura SčVK ÷ součet podružných m³), nebo pevná cena za m³.
- Celkem k úhradě = náklady − zaplacená záloha + záloha na další rok.
- Návrh zálohy = spotřeba × cena × (1 + rezerva), zaokrouhleno nahoru na stovky.
- Kontrolní vyúčtování = spotřeba od začátku sezony k poslednímu odečtu × odhadní cena, porovnané se zálohou.
