import os
import time

getränke = [
    {
        "Getränk": "Kaffee",
        "Preis": 1.00
    },
    {
        "Getränk": "Tee",
        "Preis": 1.50
    },
    {
        "Getränk": "Kakao",
        "Preis": 1.50
    },
    {
        "Getränk": "Cappuccino",
        "Preis": 2.00
    },
    {
        "Getränk": "Espresso",
        "Preis": 2.50
    }
]
münzen = [0.10, 0.20, 0.50, 1.00, 2.00]
preis = 0

#Code zum löschen der Terminalanzeige
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
    
#Begrüßung und Anzeige der Getränkeliste
def beginn():
    Ausgabefluss("Wähle dein Getränk aus\n")
    Ausgabefluss(f"{'Getränke':<15}{'Preis':>6}")
    Ausgabefluss("-" * 21)
    for eintrag in getränke:
        Ausgabefluss(f"{eintrag['Getränk']:<12}: {eintrag['Preis']:>6.2f} €")
    Ausgabefluss("-" * 21)

#Listenausgabe der Münzenauswahl
def münzenauswahl():
    Ausgabefluss("-" * 6)
    for i in münzen:
        Ausgabefluss(f"{i:.2f} €")
    Ausgabefluss("-" * 6)

#Abfrage des Users und Prüfung ob Getränk vorhanden ist
def wählen():
    global preis
    global eintrag
    gefunden = False
    while gefunden == False:
        auswahl = input("\nWähle dein Getränk: ").lower().strip()   #Abfrage des Users
        for eintrag in getränke:    #Prüfung ob Getränk in der Liste vorhanden ist
            if eintrag["Getränk"].lower() == auswahl:
                gefunden = True #Unterbrehung für die Schleife bei Fund
                clear()
                Ausgabefluss(f"{eintrag['Getränk']} kostet {eintrag['Preis']:.2f} €.\n") #Ausgabe des Preises vom Getränk
                break
        if not gefunden: #Ausgabe wenn das Getränk nicht gefunden wurde
            Ausgabefluss("Tut mir Leid, dieses Getränk existiert leider nicht")
    preis = eintrag["Preis"] #Preis vom Getränk in die Variable speichern um berechnen zu können

#Aufforderung zur Zahlung und Prüfung auf korrekte Münzwerte
def bezahlen():
    eingeworfen = 0
    while preis > eingeworfen:
        Ausgabefluss(f"Bisher eingeworfen: {eingeworfen:.2f} €\n") #Ausgabe der bisher eingegeben Münzwerte
        Ausgabefluss(f"Bitte noch {eintrag['Preis']-eingeworfen:.2f} € einwerfen\n")   #Ausgabe vom noch fehlender Betrag
        münzenauswahl()
        einwurf = input("Bitte werfe eine Münze ein: ").replace(",",".").strip()
        clear()
        try:
            einwurf = float(einwurf)    #Umwandlung der Eingabe in einen Float zum rechnen
            if einwurf in münzen:   #Prüfung der Münzwerte
                eingeworfen += einwurf  #Addieren der korrekten Werte
            else:
                Ausgabefluss("\nDieser Münzwert ist nicht zugelassen\n")
        except:
            Ausgabefluss(f"Ungültige Eingabe")
    #Ausgabe bei korrekter Bezahlung
    if preis == eingeworfen:
        Ausgabefluss(f"Zahlung bestätigt. {eintrag['Getränk']} wird ausgegeben.\n")
        Ausgabefluss(f"Du hast passend bezahlt.")
        input()
        clear()
    else:   #Ausgabe bei Überbezahlung und Rückgabe vom Restgeld
        Ausgabefluss(f"Zahlung bestätigt. {eintrag['Getränk']} wird ausgegeben.\n")
        Ausgabefluss(f"{eingeworfen - eintrag['Preis']:.2f} € zuviel bezahlt.\nWechselgeld wird ausgegeben.")
        input()
        clear()

while True:
    beginn()
    wählen()
    bezahlen()