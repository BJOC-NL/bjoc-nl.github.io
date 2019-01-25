# De zetten onthouden:

In deze les vervolg je het jouw Tic-Tac-Toe project van “Unit” 2, zodat het programma het spelbord kan analyseren en gelijkspel en een overwinning kan herkennen.
Op deze pagina maak je het mogelijk voor je programma om de zetten die worden gemaakt te registreren.

Toen je begon met het schrijven van Tic Tac Toe, was het makkelijk om valse zetten te herkennen, op een vak waar al een X of O instaat. Je sprite kan dit namelijk achter komen door alleen het gekozen vakje te testen. Maar om overwinningen en gelijkspel te herkennen, moet je programma de staat van het hele spelbord kunnen testen, niet alleen de staat van 1 vakje. Dus we gebruiken een globale variabele,  “BOARD”   , zodat we kunnen bijhouden welk vakje gevuld is met een X of O en welk vakje leeg is. 

Over globale variabele heb je geleerd in Deel 2 les 1 pagina 3: De score bijhouden met globale variabele.

Elke sprite moet zijn eigen positie weten op het bord, zodat we het “Item of” blok kunnen gebruiken om het vakje te vullen met een X of O. Dus we maken een “sprite-local variabele”, “position number”, en elke kloon zijn eigen versie heeft van deze variabele.

## Wat je moet doen:
Open jouw: “U2L4-TicTacToe” project, en sla het op als: “U3L2-TicTacToe” zodat je je oude versie bewaard voordat je deze aan gaat passen.
Maak een globale variabele aan, die je: “board” noemt, die aan het begin van het spel een lijst van 9 punten met het woord: “empty” bevat.
Creëer een  (…)    : “Position number” 
        Een “local variable” maak je bijna hetzelfde als hoe je een globale variabele maakt:
      - Click op : “Make a variable” in het variabele palet
      - Daarna, als je de naam aanmaakt, selecteer “ for this sprite only” om het een “local                
        (sprite) variable” te maken.
4. Als je de kloons aan het maken bent, verander voor elk individu de “Position number” naar         
    een van waardes: 1-9

Klik voor een hint die uitlegt hoe je het “Position number” aanpast.

zorg ervoor dat het “Position number” van de originele sprite die gekloond word niet een nummer tussen de 1 en de 9 is, zodat het niet voor problemen zorgt bij de kloons.


5. Wanneer je een vakje hebt aangeklikt, vervang dan het bijbehorende element van dat vakje     
     in de “ board” list met X of O.
6. kijk naar de waarden die opgeslagen zijn in de “ Board” variabele terwijl je het spel speelt.    
    Zorg ervoor dat de lijst update zoals jouw bedoeling was, verbeter de bugs.
    Een bug is een fout in het geschreven programma, waardoor het spel mogelijk niet goed     
    werkt.
7.  “Save. You will use this later.”
