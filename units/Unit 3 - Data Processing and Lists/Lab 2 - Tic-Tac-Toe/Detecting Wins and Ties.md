# Het herkennen van gelijkspel of een overwinning:

Op deze pagina programmeer je jouw Tic Tac Toe zodat deze gelijkspel of een overwinning kan herkennen en doorgeven.

Alle manieren van winnen opslaan:

Om een manier om te winnen op te slaan, moeten we aangeven hoe een overwinning eruitziet. We slaan alle mogelijke manieren op in een lijst van 3 positie nummers voor ons boter, kaas en eieren spel. Een voorbeeld hiervan is: “List 3,5,7” omdat het 3de, 5de en 7de vakje met alledrie een O of een X een overwinning betekend.

Wat je moet doen:
“ Talk with your Partner” a. hoeveel mogelijke overwinningen zijn er? b. schrijf deze op.
Open jouw project “U3L2-TicTacToe.
Creëer een “reporter” die alle mogelijke overwinningen vastlegt, dat ziet er ongeveer zo uit:

Het controleren van een manier om te winnen:

We hebben een manier nodig om te detecteren of iemand heeft gewonnen. We kunnen “map” gebruiken om de positie van de kruisjes en rondjes te checken, dan komen we erachter of er al iemand heeft gewonnen.

je hebt geleert over “map” in “ Unit 3 Lab 1 page 4: Transforming every list item”.
“ map”  voegt de functie in de grijze ring toe aan ieder “item” in de “input list”, en geeft de lijst met resultaten door.

Herinner je dat de lege “input slot” in de functie in de grijze ring wordt gevalt met een “ list item” iedere keer dat de functie uitgevoerd wordt. 

Wat je moet doen:
4.   klik op (…) om een nieuw spel te starten. speel een spel en laat X winnen.
5. maak dit na, en kijk wat hij doorgeeft.            (Hoe werkt “map” hier)
6. “talk with your partner” Wat zegt datgene wat de opstelling doorgeeft over de staat van het spel. (De staat in de zin van: heeft er iemand gewonnen of is er een gelijkspel).
7. Als {1, 2, 3} niet de vakjes zijn in welke combinatie X heeft gewonnen, vervang dan de cijfers in de “list” in “map” naar de vakjes combinatie waarmee X  wel heeft gewonnen.
8.gebruik dit idee om een “status of triple” te maken. Dit blok neemt 1 mogelijke winnende combinatie (zoals:m (…)), als een “input” en geeft een lijst door met welke tekens, X O of empty, er op in deze vakjes staan.
9. Speel nog een spel, en laat O winnen. Test je “ status of triple” blok met de winnende combinatie. verbeter de bugs.

controleer alle manieren om te winnen:

Je hebt net een blok gebouwd die alle winnende vakjes combinaties checkt, of die met dezelfde tekens gevuld zijn; X of O. nu ga je een blok bouwen: “ status of all winning triples”  om diezelfde check uit te voeren voor alle verschillende combinaties, in een keer. daarna gebruik je het blok om te checken of er binnen die mogelijke combinaties ook echt 3 keer een X of 3 keer een O zitten. 

hier beneden zie je een voorbeeld:   Speler O heeft het spel gewonnen, en de “ status of all winning triples” blok geeft aan op welke vakjes een X zit en op welke een O.

De combinatie van de volgorde van de X / O combinatie en de nummering van de posities in jouw project kunnen anders zijn dan het voorbeeld hierboven. Dat is oké, als het verder geen problemen oplevert in de werking van het spel. 

(deze stappen zijn iets te onduidelijk)
Wat je moet doen:
10. gebruik “map” in combinatie met de andere blokken die je hebt gemaakt om de “ status of all winning triples” blok te bouwen. Het moet de status van alle winnende mogelijke combinaties doorgeven zoals hierboven in het voorbeeld; als een lijst met lijsten.
11. nu maak je een blok: “won?” that gebruikt de letter X of O als “ input”, en geeft “true” door als X of O heeft gewonnen.
12. pas je programma zo aan dat als een speler het spel wint, het programma dat laat weten.
13. speel het spel een aantal keer om te checken of het werkt. verbeter bugs. Zorg ervoor dat je voor zowel X als O de mogelijke overwinningen checkt.

controleren op gelijkspel:

de definite van een gelijkspel is: Dat als er geen lege vakjes meer over zijn en er is geen winnende combinatie op het bord te vinden.

(hier moet iets meer hulp bij komen)
wat je moet doen:
14. Ontwikkel een manier zodat je programma herkent als er een gelijkspel is, zoals je het programma eerder hebt geprogrammeerd zodat het overwinningen herkent. Zorg ook dat het programma de spelers laat weten als ze gelijk hebben gespeeld. 
15. speel het spel een aantal keer om te checken of het werkt. verbeter de bugs.
16. waarom maakt het uit in welke volgorde de tests uit worden gevoerd? (eerst testen op een overwinning of op een gelijkspel.)
17. “ Save. You will use this file later.” 

Als er nog tijd  is…
18. Er zijn nog een aantal kleine dingen die je zou kunnen verbeteren. Je zou er bijvoorbeeld voor kunnen zorgen dat zodra een speler wint, je geen nieuwe zetten meer kan doen. Zijn er nog meer dingen die je zou willen veranderen of verbeteren?

Een stap verder gaan
Je programma kan gelijkspel ook eerder herkennen, als er bijvoorbeeld nog maar 1 vakje leeg is en geen van beide spelers kan een winnende combinatie maken. Je zou dan een nieuw “board” moeten aanmaken om dat te kunnen herkennen. 
In plaats van de sprite te laten zeggen dat X wint, kan je ook een streep laten trekken door de winnende combinatie. Dit is wel ingewikkeld omdat zodra het programma heeft herkent dat er iemand heeft gewonnen, weet deze niet meer welke combinatie dit heeft veroorzaakt. Zorg er ook voor dat je code leesbaar blijft voor andere programmeurs.
