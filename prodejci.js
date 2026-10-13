/* Seznam prodejců PREMIUM 60 – jediné místo, kde se prodejci zapisují.
   Nového prodejce přidáte zkopírováním celého bloku { … } a úpravou údajů.
   Údaje u prodejce Bezpečné dveře převzaty z webu bezpecne-dvere.cz (stav 13. 10. 2026).
   cena / bezna = cena PREMIUM 60 u daného prodejce v Kč vč. DPH a montáže (null = cenu neuvádět).
   poptavka = kam vede tlačítko „Poptat“ (stránka na tomto webu nebo web prodejce). */
window.PRODEJCI = [
  {
    id: 'bezpecne-dvere',
    nazev: 'Bezpečné dveře',
    podtitul: 'Prodejna a vzorkovna KK SYSTEM',
    logo: 'img/logo-bezpecne-dvere.jpg',
    adresa: 'Obchodní 36, 434 01 Most',
    mapa: 'https://mapy.com/s/?q=Obchodn%C3%AD%2036%2C%20Most',
    telefon: '+420 725 559 235',
    telefonDoba: 'Po–Pá 8:00–17:00',
    whatsapp: '420725559235',
    email: 'chci@bezpecne-dvere.cz',
    web: 'https://bezpecne-dvere.cz/',
    provozovatel: 'Zdeněk Kučera, IČ 64682676',
    oblast: ['Most', 'Litvínov', 'Teplice', 'Louny', 'Žatec', 'Chomutov', 'Klášterec nad Ohří', 'Litoměřice', 'Česká Lípa', 'Ústí nad Labem', 'Praha'],
    cena: 38890,
    bezna: 42500,
    cenaPozn: 'akční cena vč. 12 % DPH, montáže na klíč a dopravy do 40 km',
    vyhody: [
      'Skladem, montáž do 14 dnů',
      'Doprava do 40 km zdarma',
      'Bez příplatku za cihlu a zapuštěnou zárubeň',
      '+1 rok záruky za registraci (dle podmínek)'
    ],
    poptavka: 'poptavka.html',
    detail: 'https://bezpecne-dvere.cz/dvere-do-bytu.html#premium60'
  }
];
