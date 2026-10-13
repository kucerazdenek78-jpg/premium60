/* Seznam prodejců PREMIUM 60 – jediné místo, kde se prodejci zapisují.
   Nového prodejce přidáte zkopírováním celého bloku { … } a úpravou údajů.
   kraj = nadpis karty (prodejci se řadí podle krajů). Značka prodejce se na webu jinde neuvádí.
   Údaje u prodejce Bezpečné dveře převzaty z webu bezpecne-dvere.cz (stav 13. 10. 2026).
   Web sám poptávky ani akce nemá – poptavka = odkaz na poptávku/akce na webu prodejce. */
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
    oblast: ['Most', 'Litvínov', 'Teplice', 'Louny', 'Žatec', 'Chomutov', 'Klášterec nad Ohří', 'Litoměřice', 'Česká Lípa', 'Ústí nad Labem', 'Praha'],
    vyhody: [
      'Skladem, montáž do 14 dnů',
      'Doprava do 40 km zdarma',
      'Bez příplatku za cihlu a zapuštěnou zárubeň',
      '+1 rok záruky za registraci (dle podmínek)'
    ],
    poptavka: 'https://bezpecne-dvere.cz/poptavka-dvere.html?model=premium60',
    detail: 'https://bezpecne-dvere.cz/dvere-do-bytu.html#premium60'
  }
];
