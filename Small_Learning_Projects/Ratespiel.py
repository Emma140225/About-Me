import random

print("\nIch hab ein kleines Ratespiel für dich.\n\
Der Computer wählt eine Zahl zwischen 0 und 1000\n\
und du musst sie erraten.\n\
Wie viele Versuche brauchst du dafür?\n")

#Zählt die Anzahl der Versuche mit, wird bei jeder Runde resetet
versuche = 0

#Einfache Bool-Variable um die doppelte Schleife einfach beenden zu können
ende = False

#Erste Schleife generiert für jedes Spiel eine neue Zufallszahl
while ende != True:
    computer_zahl  = random.randint(0, 1000) #Generiert die Zufallszahl

    #Zweite Schleife frägt nach dem Userinput und überprüft ob die Zahl größer, kleiner oder identisch ist
    while ende != True:
        geratene_zahl = input("Gib eine Zahl zwischen 0 und 1000 ein: ")

        #Umwandeln vom Userinput in einen Integer und Fehlerprüfung
        try:
            geratene_zahl = int(geratene_zahl)
        except:
            print("Du hast einen ungültigen Wert eingegeben")
            continue
        
        versuche += 1 #Zählt die Versuche

        #Erste Prüfung ob die Zahlen identisch sind
        if geratene_zahl == computer_zahl:
            print(f"Glückwunsch, die Zahl war Richtig. Du hast {versuche} Versuche gebraucht.")

            #Frage ob das Spiel neu gestartet werden soll oder beendet werden soll
            kill = input("Möchtest du noch einmal spielen? Drücke j für Neues Spiel. Jede andere Taste beendet das Programm. ")

            #Bei Neustart Versuche auf 0 zurück setzen und zweite Schleife unterbrechen um neue Zufallszahl zu bekommen
            if kill.lower() == "j":
                versuche = 0
                break
            
            #Beim Beenden wird die Bool-Variable einfach auf True gesetzt was verhindert
            #das die erste Schleife erneut starten kann
            else:
                ende = True

        #Prüfungen ob die eingegebenen Zahlen größer oder kleiner sind als die Zufallszahlen
        #und wiederholen der zweiten Schleife    
        elif geratene_zahl < computer_zahl:
            print("Die Zahl des Computer ist größer als deine Zahl.")
        elif geratene_zahl > computer_zahl:
            print("Die Zahl des Computer ist kleiner als deine Zahl.")

