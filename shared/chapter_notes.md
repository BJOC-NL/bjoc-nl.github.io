# Opmerkingen

Voeg toe welke hoofdstukken wat van het nationaal curriculum leren.

Sommige links naar websites zijn vertaald sommige niet, wat te doen? ben zelf tegen omdat het dan een nederlandse pagina lijkt.

commando-blok heet nu opdrachtblok in Snap, moet dit in de tekst + afbeeldingen aanpassen.

uitleggen wat een script is (een groep blokken die aan elkaar vast zitten?)

buur -> partner?

in snap heten nieuwe sprites niet meer Sprite maar Object, overal aanpassen? vooral H1L5 levert dit problemen op.

. en , met getallen moet consistent zijn dus 1.000 is duizend en 1,5 is anderhalf, dit is Nederlandse notatie. In Snap is het helaas andersom, daar gebruiken ze internationale notatie. Daar is 1.5 anderhalf, ik heb het nu zo gedaan dat als ik het over getallen in Snap heb dat ik 1.5 gebruik en voor getallen daarbuiten 1,5.

Handig voor vervangen:
([0-9]),([0-9])
$1.$2

([0-9])\.([0-9])
$1,$2

## Hoofdstuk 1

### Les 3

#### Pagina 1

Titel klinkt heel raar, misschien eerder iets leukers als "De eerste stapjes" wat leuk is omdat het letterlijk en figuurlijk zo is.

Bij Stap 4. staat er "Vergelijk je script...", maar leerlingen bouwen toch allemaal hetzelfde script? Het lijkt me sterk dat ze hier iets anders krijgen.

#### Pagina 3

??? -> "Merk op dat een opmerking die je toevoegt aan een kopblok ook wordt gebruikt voor de helptekst van                zo'n zelfgemaakt blok."

Bij 1. om nou 6x zo'n molen te maken is wel veel, ik denk 1-3 is al genoeg.

#### Pagina 4

`Zorg dat het nieuwe invoerbalkje in het <code>molen</code>blok zich gedraagt zoals je hem hierboven hebt aangepast.`, betekent dit niet gewoon, doe wat hierboven staat?

"backup" is een beetje een vage term. In nederland is dit vooral bekent met data opslaan terwijl het hier voor een soort stapje terug wordt bedoeld.

#### Pagina 6

Persoonlijk vind ik de term "lussen" niet echt goed, gewoon herhalen wordt veel meer gebruikt. Je kan misschien zeggen dat je een lus maakt.

Take it Further, stap A vraagt om een script te maken dat aftelt, maar het is niet echt duidelijk wat het resultaat moet zijn, moet de sprite dit getal zeggen, moet je gewoon een lus hebben waarbij i deze waarde heeft.

Take it Further tap C zegt "met invoer" in het Engels is dit even vaag "with inputs", ik zou het bijna weg willen halen want ik snap niet wat ze bedoelen.

de zin met "je kunt" zou ik iets anders van maken omdat het een hele vage zin is nu. "Het ...-blok bevat een tellervariable, "i", die het aantal herhalingen bijhoudt. Je kan deze tellervariable gebruiken in een herhalend script. Je kan hiermee lange scripts versimpelen, zoals hieronder."

stap 8 in als er nog tijd over is, impliceert dat de leerlingen het onderstaande script na gaan bouwen? als dat zo is, verander teskst naar "voorspel wat dit script doet, bouw het daarna, klopte je verwachting" zo niet, verander het naar "voorspel wat dit script doet zonder het na te bouwen."

Stap D, c (laatste punt), ik heb zelf geen idee hoe dit werkt.

### Les 4

#### Pagina 1

dingen is miss wel heel informeel, gegevens?

#### Pagina 2

HIV is misschien niet zo'n handig voorbeeld. Wellicht, iets als "of je man of vrouw bent"

vereisen van een bevelschrift? wat is dat? wat heeft dat met de macht van de staat te maken

#### Pagina 3

tanya's verhaal, wellicht niet de huidige koers van dollar naar euro bijzetten, die raakt heel snel gedateerd.

tanyas verhaal nog eens goed doorheen, veel zinnen lopen niet lekker. duurt wel lang, dus nog bewaren voor later

## Hoofdstuk 2

### Les 2

#### Pagina 2

Er staat dat er 2 bugs in zitten, er wordt niet verteld wat deze zijn. Ik geloof dat ik ze weet.

    * Aan het einde van het tekenenen van de A moet hij weer terug naar het beginpunt. Anders is de onderkant van de linkerpoot open.
    * Aan het begin staat de Sprite nog op locatie (0,0) als hij daarna naar de eerste coördinaat gaat komt er een extra lijn te staan. Je moet dus pas beginnen met tekenen als hij bij de eerste coordinaat is.

Bij punt 6 staan er 3 vragen en ik weet niet echt het antwoord op deze vragen. Wellicht bij de tweede vraag "om alleen stippen neer te zetten" en de derde "omdat ga naar sneller is".

#### Pagina 3

Ik weet niet wat ze bedoelen met "ghost effect resetten". Ik kan me niet herinneren wat dit deed.

### Les 3

#### Pagina 1

Ik vind dat er niet goed uitgelegd wordt wat leerlingen moeten maken bij Aan De Slag. Er staat iets met ga naar muis x en muis y, maar dat je bijvoorbeeld pen neer en verander pen kleur moet gebruiken staat er niet. Ik zou zelf zoiets toevoegen van "deze 2 blokken zal je ten minste nodig hebben".

### Les 4

#### Pagina 4

In het engels heet deze les Building a Tic-Tac-Toe Board, dus niet "boter kaas en eieren bouwen", ik weet nog geen goeie vertaling hiervoor.

Er stond eerst "in dit project dat een jaar duurt ..." dat heb ik al weggehaald want dat is wel heel specifiek, maar ik vind nog steeds het hele "in dit project"stuk ( de eerste zin) niet echt nodig.

### Les 5

#### Pagina 3

Deze pagina gaat puur over de Amerikaanse grondwet, wat een beetje raar is in Nederland. Pagina 2 ging ook al over de Amerikaanse wet, misschien goed om uit te zoeken wat hiervan klopt voor de Nederlandse versie.

### Optionele Projecten

#### Pagina 4

Er is een Import Tools stap, maar er wordt niet gezegd wat je moet importeren, Voor nu weggelaten.

## Hoofdstuk 4

### Les 1

#### Pagina 1

Er staat een link naar <http://bjc.berkeley.edu/website/privacy.html>, die website bestaat niet meer.

### Les 4

#### Pagina 1

Niet blij met de eerste 2 zinnen, gemeenschappen en saamhorigheid zijn in het Engels "community".

## Hoofdstuk 5

### Les 1

#### Pagina 1

Ik weet niet goed hoe je als je de sprite kan laten wachten tot een blok is aageklikt. ik heb nu een variabele aangemaakt die staat normaal op 0, als een blok aangeklikt wordtword die variabele op 1 gezet. de sprite wacht met werken tot die variabele op 1 staat en zodra dat gebeurt gaat ie door. Zie project H5L1-RaadHetGetal-oefen. Het is me daar gelukt om de strategie te implementeren maar dit voelt niet als de bedoelde manier...

### Les 2

#### Pagina 2

Er is een "test-project" dat eerst alleen uitgevoerd kon worden zonder de code te zien. voor een of andere reden werkt dit niet meer, dus heb nu gewoon het project gelinkt waarbij je wel de code kan zien.  Je kan het testen door "&hideControls" aan de URL te plakken. Het is niet echt handig dat hierdoor leerlingen "het antwoord" al kunnen zien.

Bij H5L2P3 werkt dit wel??

### Les 3

#### Pagina 1

Er staat dat combineer met - dubbelzinnig is, er wordt geimpliceerd dat dit slecht is, maar ik zou graag uitleggen waarom dit slecht is.

### Les 4

#### Pagina 1

Namen zijn beetje ouderwets, Adam, Eva, Dominiek.
