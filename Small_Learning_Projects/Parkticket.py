import os
import time

tarife = [
    {
        "Dauer": 1,
        "Einheit": "Stunde ",
        "Preis": 2.00
    },
    {
        "Dauer": 2,
        "Einheit": "Stunden",
        "Preis": 3.50
    },
    {
        "Dauer": 3,
        "Einheit": "Stunden",
        "Preis": 5.00
    }
]
münzen = [0.10, 0.20, 0.50, 1.00, 2.00]
auswahl = 0
preis = 0

#Einfacher Command um die Konsole zu reinigen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Reduziert die Ausgabegeschwindigkeit
def Ausgabefluss(text):
    words = text.split(" ")
    for word in words:
        print(word, end=" ", flush=True)
        time.sleep(0.05)
        if word.endswith((".", "!", "?")):
            time.sleep(0.05*4)
    print()

#Startanzeige der Tarife
def tarife_anzeigen():
    Ausgabefluss("Bitte wähle die gewünschte Parkdauer aus.")
    Ausgabefluss(f"{'Dauer':<15}{'Preis':>6}")
    Ausgabefluss("-" * 21)
    for eintrag in tarife:
        Ausgabefluss(f"{eintrag['Dauer']} {eintrag['Einheit']:<8} : {eintrag['Preis']:>6.2f} €")
    Ausgabefluss("-" * 21 + "\n")

#Übernimmt die Eingabe der Parkdauer und überprüft sie auf Gültigkeit
def parkdauer_wählen():
    global auswahl
    while True:
        try:
            auswahl = float(input("Bitte Parkdauer wählen: "))
            if auswahl == 0:
                clear()
                Ausgabefluss("0 Ist nicht zulässig, bitte eine gültige Parkdauer auswählen.\n")
                tarife_anzeigen()
                continue
            elif auswahl > 3:
                clear()
                Ausgabefluss("Maximale Parkdauer beträgt 3 Stunden, bitte eine neue Auswahl treffen.\n")
                tarife_anzeigen()
                continue

            clear()
            break
        except:
            clear()
            Ausgabefluss("Ungültige Eingabe, bitte eine gültige Parkdauer eingeben.\n")
            tarife_anzeigen()

def münzarten():
    Ausgabefluss("-" * 6)
    for i in münzen:
        Ausgabefluss(f"{i:.2f} €")
    Ausgabefluss("-" * 6)

def bezahlung():
    global preis
    for eintrag in tarife:
        if eintrag['Dauer'] == auswahl:
            Ausgabefluss(f"Gewählte Parkdauer: {eintrag['Dauer']} {eintrag['Einheit']}, Kosten: {eintrag['Preis']:.2f} €\n")
            preis = eintrag['Preis']
            
    Ausgabefluss("Bitte Münzen einwerfen\nFolgende Münzarten sind möglich")
    münzarten()
    eingeworfen = 0
    while preis > eingeworfen:
        Ausgabefluss(f"Bisher eingeworfen: {eingeworfen:.2f} €\n")
        Ausgabefluss(f"Bitte noch {eintrag['Preis']-eingeworfen:.2f} € einwerfen\n")
        münzarten()
        einwurf = input("Bitte werfe eine Münze ein: ").replace(",",".").strip()
        clear()
        try:
            einwurf = float(einwurf)
            if einwurf in münzen:
                eingeworfen += einwurf
            else:
                Ausgabefluss("\nDieser Münzwert ist nicht zugelassen\n")
        except:
            Ausgabefluss(f"Ungültige Eingabe") 
    if preis == eingeworfen:
        Ausgabefluss(f"Zahlung bestätigt.\n")
        input()
    else:
        Ausgabefluss(f"Zahlung bestätigt. \n")
        Ausgabefluss(f"{eingeworfen - eintrag['Preis']:.2f} € zuviel bezahlt.\nWechselgeld wird ausgegeben.")
        input()

tarife_anzeigen()
parkdauer_wählen()
bezahlung()





