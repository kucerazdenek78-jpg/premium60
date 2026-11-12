#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vygeneruje sekci Rady pro web PREMIUM 60: src/rady.html (přehled) + src/rady-<slug>.html (články).
Spuštění z kořene repa:  python3 tools/build_rady.py  (pak python3 tools/sestav.py)
Obsah je produktově neutrální (bez značky prodejce), odkazy vedou na Kde koupit / Servis u prodejce.
Všechny články jsou rovnou viditelné (knihovna rad) – dobré pro vyhledávače."""
import os, html, json, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://premium60.cz/"
CZ_M = ["", "ledna","února","března","dubna","května","června","července","srpna","září","října","listopadu","prosince"]
def cz(d):
    y,m,dd = d.split("-"); return f"{int(dd)}. {CZ_M[int(m)]} {y}"

KDE = ("kde-koupit.html", "Kde koupit PREMIUM 60")
SERVIS = ("servis-a-dokumenty.html", "Servis a dokumenty")
CERT = ("servis-a-dokumenty.html#certifikaty", "Certifikáty ke stažení")

A = [
{"den":"2026-11-11","slug":"rc3-a-ei60-co-to-znamena","kat":"PREMIUM 60",
 "titulek":"PREMIUM 60: co znamená RC3 a EI 60",
 "perex":"Zkratky RC3 a EI 60 u dveří PREMIUM 60 nejsou marketing. Vysvětlujeme, co přesně znamenají a proč u bytových dveří dávají smysl.",
 "obsah":"""<p>U dveří PREMIUM 60 najdete označení RC3 a EI 60. Za oběma stojí konkrétní normy a zkoušky. Co znamenají v praxi?</p>
<h2>RC3 – bezpečnostní třída</h2>
<p>RC (Resistance Class) podle normy ČSN EN 1627 říká, jak dveře odolají násilnému vniknutí. Třída RC3 počítá s pachatelem, který kromě hrubé síly použije i páčidlo a další nářadí. PREMIUM 60 jistí křídlo osmi aktivními čepy (sedm vodorovných a jeden svislý nahoře) a šesti pevnými trny na straně závěsů – páčení v horním rohu tak není bez ochrany.</p>
<h2>EI 60 – požární odolnost</h2>
<p>EI je požární klasifikace: E znamená celistvost (dveře zabrání průniku plamenů) a I izolaci (zadrží teplo). Číslo 60 je počet minut. PREMIUM 60 tedy 60 minut brání šíření požáru mezi bytem a chodbou.</p>
<h2>Ověřeno zkušebnami</h2>
<p>Dveře mají plech 1,2 mm (o 71 % silnější než standard) a prošly certifikací Národního bezpečnostního úřadu ČR, zkušebny TREZOR TEST i PAVUS. Odhlučnění je 42 dB.</p>""",
 "cta":KDE,"cta_t":"Kde PREMIUM 60 koupit","cta_x":"Pevná cena kompletu 42 500 Kč vč. montáže a 12 % DPH. Prodejci podle krajů."},

{"den":"2026-11-14","slug":"bezpecnostni-tridy-rc2-rc3-rc4","kat":"Bezpečnost",
 "titulek":"Bezpečnostní třídy RC2, RC3 a RC4 – čemu odolají",
 "perex":"Co znamenají bezpečnostní třídy RC2, RC3 a RC4 u dveří a proč je RC3 rozumný standard do bytu.",
 "obsah":"""<p>Bezpečnostní třída (RC – Resistance Class) podle normy ČSN EN 1627 říká, jak dlouho dveře odolají násilnému vniknutí. Čím vyšší číslo, tím odolnější.</p>
<h2>RC2</h2>
<p>Počítá s pachatelem, který se dveře snaží vypáčit jednoduchým nářadím (šroubovák, klín). Základní ochrana.</p>
<h2>RC3</h2>
<p>Nejčastější volba do bytu. Předpokládá i použití páčidla. Toto je třída dveří PREMIUM 60.</p>
<h2>RC4</h2>
<p>Vyšší odolnost pro náročnější situace, počítá i s údery a výkonnějším nářadím.</p>
<h2>Jakou zvolit</h2>
<p>Pro běžný byt je rozumným standardem RC3 – dobrý poměr mezi bezpečností a cenou.</p>""",
 "cta":KDE,"cta_t":"PREMIUM 60 je v třídě RC3","cta_x":"Kde dveře koupit a za kolik."},

{"den":"2026-11-17","slug":"certifikaty-premium-60","kat":"PREMIUM 60",
 "titulek":"Certifikáty PREMIUM 60: NBÚ, TREZOR TEST a PAVUS",
 "perex":"Dveře PREMIUM 60 prošly nezávislými zkouškami. Které certifikáty mají a kde si je stáhnout.",
 "obsah":"""<p>U bezpečnostních dveří je dobré, když jejich vlastnosti potvrdil někdo nezávislý. PREMIUM 60 prošly hned několika zkouškami.</p>
<h2>Národní bezpečnostní úřad ČR</h2>
<p>Certifikát technického prostředku č. T0030/2026 – patří mezi bytové dveře ověřené přímo v České republice.</p>
<h2>TREZOR TEST</h2>
<p>Certifikát shody č. TT-120/2026 potvrzuje bezpečnostní třídu RC 3 podle ČSN EN 1627.</p>
<h2>PAVUS</h2>
<p>Certifikát výrobku č. 216/C5/2024/0015 dokládá požární odolnost EI 60.</p>
<p>Všechny certifikáty jsou ke stažení v sekci Servis a dokumenty – hodí se třeba pro SVJ nebo pojišťovnu.</p>""",
 "cta":CERT,"cta_t":"Certifikáty ke stažení","cta_x":"NBÚ, TREZOR TEST i PAVUS v PDF."},

{"den":"2026-11-20","slug":"protipozarni-dvere-rocni-kontrola","kat":"Protipožární dveře",
 "titulek":"Protipožární dveře v bytě: povinná roční kontrola",
 "perex":"Protipožární dveře v bytě musí mít pravidelnou roční kontrolu. Co to znamená a na co u nich dbát.",
 "obsah":"""<p>PREMIUM 60 jsou i protipožární dveře (EI 60). Na protipožární dveře se vztahují pravidla, na která se často zapomíná.</p>
<h2>Roční kontrola je povinná</h2>
<p>Požárně bezpečnostní zařízení, kam protipožární dveře patří, se podle vyhlášky č. 246/2001 Sb. kontroluje nejméně jednou ročně. Kontrola ověří, že dveře plní svou funkci – tedy že samy dovřou a těsní.</p>
<h2>Nikdy je nepodkládejte</h2>
<p>Protipožární dveře nesmí být zaklínované ani podložené rohožkou. Při požáru musí samy dovřít, jinak ztrácejí smysl. Totéž platí pro samozavírač.</p>
<h2>Co kontrolovat průběžně</h2>
<ul><li>dveře samy dovírají až na doraz,</li><li>těsnění je celé a pružné,</li><li>kování a zámek fungují.</li></ul>""",
 "cta":SERVIS,"cta_t":"Servis řeší váš prodejce","cta_x":"Kontrolu, seřízení i reklamace vyřizuje prodejce, u kterého jste dveře koupili."},

{"den":"2026-11-24","slug":"udrzba-dveri-tesneni-a-mazani","kat":"Údržba",
 "titulek":"Údržba bezpečnostních dveří: těsnění a mazání",
 "perex":"Jednoduchá údržba každých šest měsíců prodlouží životnost dveří. Jak ošetřit těsnění a co promazat.",
 "obsah":"""<p>Bezpečnostní dveře vydrží dlouho, když se o ně párkrát do roka postaráte. Zabere to pár minut.</p>
<h2>Těsnění</h2>
<p>Těsnění dveří a zárubně ošetřete silikonovým mazivem. Zůstane pružné, dveře dobře dolehnou a netáhne. Obzvlášť se to vyplatí před zimou.</p>
<h2>Zamykací čepy a samozavírač</h2>
<p>Zamykací čepy a krycí misku vložky promažte olejem. Kluznou lištu samozavírače promažte jednou za čas – dveře pak dovírají tiše a plynule.</p>
<h2>Vložka zámku</h2>
<p>Do samotné cylindrické vložky olej nepatří, chytá na sebe prach. Použijte jen teflonový nebo grafitový sprej.</p>
<p>Pravidelná údržba je důležitá i pro záruku – podmínky určuje váš prodejce.</p>""",
 "cta":SERVIS,"cta_t":"Záruka a servis u prodejce","cta_x":"Podmínky záruky a servis vyřizuje prodejce, u kterého jste dveře koupili."},

{"den":"2026-11-28","slug":"vlozka-zamku-jen-grafit","kat":"Údržba",
 "titulek":"Vložka zámku: proč do ní patří jen grafit",
 "perex":"Do cylindrické vložky zámku nepatří olej. Vysvětlujeme, proč použít teflonový nebo grafitový sprej.",
 "obsah":"""<p>Zadrhává klíč ve vložce? Než sáhnete po oleji, přečtěte si tohle.</p>
<h2>Olej do vložky nepatří</h2>
<p>Olej je mastný a chytá na sebe prach a nečistoty. V cylindrické vložce vznikne po čase mazlavá vrstva, která chod zhorší, ne zlepší.</p>
<h2>Použijte teflon nebo grafit</h2>
<p>Do vložky patří jen teflonový nebo grafitový sprej. Maže, ale neváže na sebe prach, takže vložka zůstane čistá a klíč jde lehce.</p>
<h2>Zbytek kování je jiná písnička</h2>
<p>Pozor na rozdíl: zamykací čepy a krycí misku vložky naopak olejem promazat můžete. Jen do samotné vložky olej nedávejte.</p>""",
 "cta":SERVIS,"cta_t":"Klíče a vložky u prodejce","cta_x":"Náhradní klíče i výměnu vložky řeší váš prodejce."},

{"den":"2026-12-02","slug":"odhlucneni-dveri-42-db","kat":"Komfort",
 "titulek":"Hluk z chodby? Odhlučnění dveří a 42 dB",
 "perex":"Vchodové dveře umí ztlumit hluk z chodby. Co odhlučnění ovlivní a co znamená 42 dB u PREMIUM 60.",
 "obsah":"""<p>Slyšíte z chodby každý krok a zabouchnutí výtahu? Část hluku jdou utlumit i vchodové dveře.</p>
<h2>Co znamená 42 dB</h2>
<p>Údaj v decibelech říká, o kolik dveře zvuk ztlumí. PREMIUM 60 mají odhlučnění 42 dB, což z chodby propustí výrazně méně hluku než běžné dveře.</p>
<h2>Na čem odhlučnění stojí</h2>
<ul><li>hmotnost a konstrukce křídla (celokovové, plech 1,2 mm),</li><li>kvalitní těsnění po celém obvodu,</li><li>správné osazení a seřízení.</li></ul>
<h2>Nezapomeňte na těsnění</h2>
<p>Aby odhlučnění fungovalo, musí dveře dobře dolehnout. Těsnění proto párkrát ročně ošetřete silikonem.</p>""",
 "cta":KDE,"cta_t":"PREMIUM 60 – 42 dB","cta_x":"Kde dveře koupit a za kolik."},

{"den":"2026-12-06","slug":"bezpecnost-klicu","kat":"Bezpečnost",
 "titulek":"Bezpečnost klíčů: na klíčenku nikdy nepište adresu",
 "perex":"Klíče jsou slabé místo i u nejlepších dveří. Pár návyků, které se vyplatí.",
 "obsah":"""<p>I ty nejlepší bezpečnostní dveře obejdete klíčem. Proto se vyplatí s klíči zacházet opatrně.</p>
<h2>Žádná adresa na klíčence</h2>
<p>Na klíčenku nikdy nepište adresu ani jméno. Ztracený klíč s adresou je pozvánka k vašim dveřím.</p>
<h2>Náhradní klíč ne pod rohožku</h2>
<p>Rohožka, květináč, parapet – to jsou první místa, kam se podívá nezvaný host. Náhradní klíč dejte někomu blízkému.</p>
<h2>Při ztrátě zvažte vložku</h2>
<p>Pokud klíče zmizí a nevíte kde, je nejbezpečnější vyměnit cylindrickou vložku. Staré klíče tím přestanou platit.</p>""",
 "cta":SERVIS,"cta_t":"Klíče a vložky u prodejce","cta_x":"Objednání klíčů i výměnu vložky vyřizuje váš prodejce."},

{"den":"2026-12-10","slug":"chytry-zamek-tedee","kat":"Chytrá domácnost",
 "titulek":"Chytrý zámek: PREMIUM 60 a tedee",
 "perex":"Dveře PREMIUM 60 lze doplnit o chytrý zámek tedee. Co to umí a jak to funguje.",
 "obsah":"""<p>Chytrý zámek je praktický, když nechcete řešit klíče. Dveře PREMIUM 60 je možné doplnit o chytrý zámek tedee.</p>
<h2>Co chytrý zámek umí</h2>
<ul><li>odemknout a zamknout z mobilu,</li><li>sdílet přístup rodině nebo úklidu bez předávání klíčů,</li><li>přehled o tom, kdy byly dveře otevřené.</li></ul>
<h2>Klíč zůstává zálohou</h2>
<p>I s chytrým zámkem klíč dál funguje jako záloha, takže se nemusíte bát vybité baterie.</p>
<h2>Pro koho</h2>
<p>Hodí se rodinám, lidem, kteří často pouští návštěvy, i tomu, kdo prostě nerad hledá klíče.</p>""",
 "cta":KDE,"cta_t":"Zajímá vás PREMIUM 60?","cta_x":"Kde dveře koupit; chytrý zámek proberte s prodejcem."},

{"den":"2026-12-14","slug":"protipozarni-dvere-caste-chyby","kat":"Protipožární dveře",
 "titulek":"Protipožární dveře: čeho se vyvarovat",
 "perex":"U protipožárních dveří rozhoduje, že při požáru samy dovřou. Nejčastější chyby, které tomu brání.",
 "obsah":"""<p>Protipožární dveře mají jeden hlavní úkol: při požáru zabránit šíření ohně a kouře. Aby fungovaly, nesmí se dělat pár věcí.</p>
<h2>Nepodkládat a neklínovat</h2>
<p>Dveře nikdy nezaklínujte a nepodkládejte rohožkou. Otevřené protipožární dveře ztrácejí smysl.</p>
<h2>Nevyřazovat samozavírač</h2>
<p>Samozavírač musí být funkční a nesmí se odpojovat. Právě on dveře dovře, i když na to nikdo nemyslí.</p>
<h2>Nezanedbat roční kontrolu</h2>
<p>Podle vyhlášky 246/2001 Sb. se protipožární dveře kontrolují nejméně jednou ročně.</p>""",
 "cta":SERVIS,"cta_t":"Servis u prodejce","cta_x":"Kontrolu a seřízení vyřizuje prodejce, u kterého jste dveře koupili."},

{"den":"2026-12-18","slug":"jak-dlouho-vydrzi-bezpecnostni-dvere","kat":"Výběr",
 "titulek":"Jak dlouho vydrží bezpečnostní dveře",
 "perex":"Bezpečnostní dveře jsou investice na dlouhá léta. Co jejich životnost ovlivní.",
 "obsah":"""<p>Dveře se nekupují každý rok. Při rozumné péči slouží bezpečnostní dveře mnoho let – a dá se pro to něco udělat.</p>
<h2>Kvalita a montáž</h2>
<p>Základ je kvalitní provedení a správná montáž. Celokovové dveře PREMIUM 60 osazené do bezpečnostní zárubně a seřízené při předání vydrží víc než narychlo nasazené křídlo.</p>
<h2>Údržba</h2>
<p>Pár minut párkrát do roka hodně pomůže: ošetřit těsnění silikonem, promazat kování, vložku jen teflonem nebo grafitem.</p>
<h2>Servis, když je potřeba</h2>
<p>Když se dveře po letech trochu rozladí, seřízení je vrátí do formy. Servis vyřizuje váš prodejce.</p>""",
 "cta":KDE,"cta_t":"Dveře na dlouho","cta_x":"Kde PREMIUM 60 koupit a za kolik."},

{"den":"2026-12-22","slug":"zimni-pece-o-dvere","kat":"Údržba",
 "titulek":"Zimní péče o dveře: mráz a vlhkost",
 "perex":"V zimě dveře čelí mrazu i vlhkosti. Co jim v chladném období prospěje.",
 "obsah":"""<p>Zima dá dveřím zabrat – mráz, vlhkost i rozdíl teplot. Pár věcí jim pomůže.</p>
<h2>Těsnění především</h2>
<p>V zimě se nejvíc pozná těsnění. Ošetřete ho silikonovým mazivem, aby zůstalo pružné a neztvrdlo mrazem – dveře pak dobře dolehnou a netáhne.</p>
<h2>Vložka a zámek</h2>
<p>Když zámek v mrazu drhne, nepoužívejte olej (chytá vlhkost a prach). Jen teflonový nebo grafitový sprej.</p>
<h2>Kondenzace</h2>
<p>Při velkém rozdílu teplot se může objevit vlhkost. Pomáhá větrání a dobré těsnění, které udrží teplo uvnitř.</p>""",
 "cta":SERVIS,"cta_t":"Servis u prodejce","cta_x":"Seřízení a servis vyřizuje prodejce, u kterého jste dveře koupili."},
]

SRC = os.path.join(ROOT, "src")

def article_src(a):
    canon = BASE + f"rady-{a['slug']}.html"
    ld = {"@context":"https://schema.org","@type":"Article","headline":a["titulek"],
          "description":a["perex"],"datePublished":a["den"],"dateModified":a["den"],
          "inLanguage":"cs","mainEntityOfPage":canon,"image":BASE+"img/og-image.jpg",
          "author":{"@type":"Organization","name":"PREMIUM 60"},
          "publisher":{"@type":"Organization","name":"PREMIUM 60","url":BASE}}
    meta = {"title": f"{a['titulek']} – PREMIUM 60", "description": a["perex"], "nav": "rady"}
    cta_h, cta_l = a["cta"]
    # související: 3 jiné
    rel = [x for x in A if x["slug"] != a["slug"]][:3]
    more = "".join(f'<a href="rady-{x["slug"]}.html">{html.escape(x["titulek"])}</a>' for x in rel)
    body = f"""<!-- {json.dumps(meta, ensure_ascii=False)} -->

<header class="p-sub">
  <div class="container">
    <span class="p-kicker">Rady · {html.escape(a['kat'])}</span>
    <h1>{html.escape(a['titulek'])}</h1>
    <p>{cz(a['den'])}</p>
  </div>
</header>

<section class="p-sec">
  <div class="container">
    <article class="rady-article">
      <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(',',':'))}</script>
{a['obsah']}
      <div class="rady-cta">
        <h3>{html.escape(a['cta_t'])}</h3>
        <p>{html.escape(a['cta_x'])}</p>
        <a class="btn btn-primary" href="{cta_h}">{html.escape(cta_l)}</a>
      </div>
      <nav class="rady-more" aria-label="Další rady">
        <h3>Další rady</h3>
        {more}
      </nav>
    </article>
  </div>
</section>
"""
    with open(os.path.join(SRC, f"rady-{a['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(body)

def index_src():
    arts = sorted(A, key=lambda x: x["den"], reverse=True)
    cards = ""
    for a in arts:
        cards += f"""      <a class="rady-card" href="rady-{a['slug']}.html">
        <span class="rady-kat">{html.escape(a['kat'])}</span>
        <b>{html.escape(a['titulek'])}</b>
        <span class="rady-perex">{html.escape(a['perex'])}</span>
        <span class="rady-date">{cz(a['den'])}</span>
      </a>
"""
    meta = {"title": "Rady o bezpečnostních dveřích – PREMIUM 60",
            "description": "Praktické rady o bezpečnostních dveřích PREMIUM 60 – bezpečnostní třídy, certifikáty, protipožární dveře, údržba a zámky.",
            "nav": "rady"}
    body = f"""<!-- {json.dumps(meta, ensure_ascii=False)} -->

<header class="p-sub">
  <div class="container">
    <span class="p-kicker">Rady</span>
    <h1>Rady o bezpečnostních dveřích</h1>
    <p>Bezpečnostní třídy, certifikáty, protipožární dveře, údržba i zámky – srozumitelně a na jednom místě.</p>
  </div>
</header>

<section class="p-sec">
  <div class="container">
    <div class="rady-grid">
{cards}    </div>
  </div>
</section>
"""
    with open(os.path.join(SRC, "rady.html"), "w", encoding="utf-8") as f:
        f.write(body)

if __name__ == "__main__":
    for a in A:
        article_src(a)
    index_src()
    print(f"Hotovo: {len(A)} článků rady-*.html + rady.html do src/")
