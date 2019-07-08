# Lijst van verbetervoorstellen voor Snap (tzt in te dienen als pull request)
## TO CHECK: 
* is "initialize" verandert in "initialiseren" ? 
* spreken we bij Booleans over "booleanen" en "waar" en "onwaar" ? 
* zijn alle "loops" vertaald in "lussen" (loop = lus)
* Predicates vertaald in "predikaten"  ? 

## ALGEMEEN
* Belangrijke to-do: waar ik (Sabine) mogelijk niet meer bij kan zijn is het nalopen en verwisselen van afbeeldingen. Er worden vaak blokken als voorbeelden gegeven, maar dit is allemaal nog vanuit de Engelse Snap! versie.
* In H2L1P3 <a href="http://snap.berkeley.edu/snapsource/help/SnapManual.pdf"   Manual vertalen?

## 14/05 SVT
* In U2L2P4 wordt er over een 'For each' code gepraat, maar die vind ik niet noch in de Eng noch in NL
* Link veranderen in H2L3P1
* In H2L2P2 hebben ze het over een 'point'  blok, maar in de NL Snap! versie zie ik niks wat daar op lijkt.

# Casper 03/07/19

## Glossary toevoegingen
* Discuss -> Bespreek
* partner -> klasgenoot
* event -> gebeurtenis

## Vragen over Glossary
* Cloud blijft Cloud? (H1L4P1)
* Privacy blijft Privacy? (H1L4)
* Section -> gedeelte? miss paragraaf ?(H1L4P4)
* For You To Do -> Voor Jou Om Te Doen? klinkt niet heel lekker.

## Andere vragen/opmerkingen
* H1L4P3, Verhaal in The Guardian, wat doen we hier mee? Ook lezen uit boek Blown to Bits, hoe hiermee omgaan nu?
* de "Take It Further" werkt niet meer in H1L4P1, ook in de Engelse. weghalen?
* aantal pagina's hebben een raar <head> blok, ik denk dat we deze gewoon kunnen aanpassen naar die van de meeste pagina's.
* Icons moeten ook vertaald gaan worden, geloof dat het lettertype Arial is.
* overal staat nog <html lang="en">.
* weghalen van tekst die niet weergegeven is? todos en comments, voegen nisk toe en maken vertalen lastiger.
* vertalen van blown to bits?

## Stappen mm de layout te fixen
* verander alle paths van /bjc-r etc. naar ../../bjc-r. dan is de styling gefixt. GEDAAN VOOR U1, MAAR AANTAL PAGINA'S ZIJN RAAR.
* <html lang="en"> naar <html lang="nl">. kan je beter via replace all op het eind doen wss

##Images 
creeër file structure zodat alles bij de general afbeeldingen makkelijk kan en zorg dat bloks gesorteerd zijn en miss identificeerbaar.
Folder voor alle afbeeldingen: afb
Daarin:  icons, voor afbeeldingen zoals Pair Programming Swap, Etc, sommigen hiervan moeten dus vertaald worden.

*afb
**icons
**H1
***blocks
***H1L1
****blocks
****overig
***H1L2
****blocks
****overig
***H1L3
****blocks
****overig
***H1L4
****blocks
****overig
***H1L5
****blocks
****overig
**H2
...

