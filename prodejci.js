/* Seznam prodejců PREMIUM 60 – jediné místo, kde se prodejci zapisují. Pořadí = pořadí na webu.
   Nového prodejce přidáte zkopírováním celého bloku { … } a úpravou údajů.
   kraj = nadpis karty a vybarvený kraj na mapě (mapa_kraje = víc krajů). Web sám poptávky ani akce nemá – akce = odkaz na místní akce prodejce,
   poptavka = odkaz na poptávku/objednávku u prodejce.
   Bezpečné dveře: údaje z bezpecne-dvere.cz; K.V. DOORS: údaje z kvdoors.cz/kontakt (stav 13. 10. 2026). */
window.PRODEJCI = [
  {
    id: 'ustecky-kraj',
    kraj: 'Ústecký kraj',
    nazev: 'Bezpečné dveře',
    podtitul: 'Prodejna a vzorkovna, Most',
    adresa: 'Obchodní 36, 434 01 Most',
    mapa: 'https://mapy.com/fnc/v1/search?query=Obchodn%C3%AD%2036%2C%20Most',
    telefon: '+420 725 559 235',
    telefonDoba: 'Po–Pá 8:00–17:00',
    whatsapp: '420725559235',
    email: 'chci@bezpecne-dvere.cz',
    web: 'https://bezpecne-dvere.cz/',
    provozovatel: 'Zdeněk Kučera, IČ 64682676',
    oblast: ['Most', 'Litvínov', 'Teplice', 'Louny', 'Žatec', 'Chomutov', 'Klášterec nad Ohří', 'Litoměřice', 'Ústí nad Labem'],
    vyhody: [
      'Skladem, montáž do 14 dnů',
      'Doprava do 40 km zdarma',
      'Bez příplatku za cihlu a zapuštěnou zárubeň',
      '+1 rok záruky za registraci (dle podmínek)'
    ],
    akce: 'https://bezpecne-dvere.cz/dvere-do-bytu.html#premium60',
    poptavka: 'https://bezpecne-dvere.cz/poptavka-dvere.html?model=premium60'
  },
  {
    id: 'karlovarsky-kraj',
    kraj: 'Karlovarský kraj',
    nazev: 'K.V. DOORS',
    podtitul: 'Prodejna dveří, Karlovy Vary',
    adresa: 'Rosnice 66, 360 17 Karlovy Vary',
    mapa: 'https://mapy.com/fnc/v1/search?query=Rosnice%2066%2C%20Karlovy%20Vary',
    telefon: '+420 353 569 711',
    telefonDoba: 'Po–Pá 8:00–17:00, So 9:00–12:00',
    email: 'prodej@kvdoors.cz',
    web: 'https://kvdoors.cz/',
    provozovatel: 'K.V. DOORS s.r.o., IČ 26363895',
    akce: 'https://kvdoors.cz/',
    poptavka: 'https://kvdoors.cz/kontakt'
  },
  {
    id: 'stredocesky-kraj',
    kraj: 'Středočeský kraj',
    krajPozn: 'po Prahu',
    mapa_kraje: ['Středočeský kraj – do 120 km od Mostu', 'Hlavní město Praha'],   // jen část kraje po Prahu (tools/mapa-kraju.svg)
    oblast: ['Praha a západní část Středočeského kraje do cca 120 km od Mostu'],
    nazev: 'Bezpečné dveře',
    podtitul: 'Prodejna a vzorkovna, Most',
    adresa: 'Obchodní 36, 434 01 Most',
    mapa: 'https://mapy.com/fnc/v1/search?query=Obchodn%C3%AD%2036%2C%20Most',
    telefon: '+420 725 559 235',
    telefonDoba: 'Po–Pá 8:00–17:00',
    whatsapp: '420725559235',
    email: 'chci@bezpecne-dvere.cz',
    web: 'https://bezpecne-dvere.cz/',
    provozovatel: 'Zdeněk Kučera, IČ 64682676',
    vyhody: [
      'Skladem, montáž do 14 dnů',
      'Bez příplatku za cihlu a zapuštěnou zárubeň',
      '+1 rok záruky za registraci (dle podmínek)'
    ],
    akce: 'https://bezpecne-dvere.cz/dvere-do-bytu.html#premium60',
    poptavka: 'https://bezpecne-dvere.cz/poptavka-dvere.html?model=premium60'
  }
];
