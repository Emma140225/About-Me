import os
import time

münzen = [0.10, 0.20, 0.50, 1.00, 2.00]
zonen = [
    {
        "Zone": "A",
        "Nummer": 1
    },
    {
        "Zone": "B",
        "Nummer": 2
    },
    {
        "Zone": "C",
        "Nummer": 3
    },
    {
        "Zone": "D",
        "Nummer": 4
    },
    {
        "Zone": "E",
        "Nummer": 5
    },
]
rabattgruppen = [
    {
        "Auswahl": 1,
        "Art": "Schüler",
        "Rabatt": "50 %",
        "Wert": 0.5
    },
    {
        "Auswahl": 2,
        "Art": "Senioren",
        "Rabatt": "30 %",
        "Wert": 0.3
    },
    {
        "Auswahl": 3,
        "Art": "Gruppe (ab 3 Personen)",
        "Rabatt": "20 %",
        "Wert": 0.2
    },
]
start = ""
ziel = ""
anzahl = 0
preis = 0
rabatt = 0

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

#Tabellarische Anzeige aller Münzarten
def münzarten():
    Ausgabefluss("-" * 6)
    for i in münzen:
        Ausgabefluss(f"{i:.2f} €")
    Ausgabefluss("-" * 6)

#Startanzeige der Tarife
def tarife_anzeigen():
    Ausgabefluss(f"{'Zone'}")
    Ausgabefluss("-" * 4)
    for eintrag in zonen:
        Ausgabefluss(f"{eintrag['Zone']:<8}")
    Ausgabefluss("-" * 4)
    Ausgabefluss("1 Zone = 2,00 €, jede weitere Zone + 1,00 €\n")

#Überprüfung der Zonenauswahl
def zonen_prüfung(eingabe):
    for eintrag in zonen:
            if eintrag['Zone'] == eingabe:
                return True

#Auswahl der Start- und Zielzone
def zonenauswahl():
    global start, ziel
    while True: #Startauswahl
        start = input("Bitte gib deine Startzone ein: ").upper()
        if zonen_prüfung(start):
            clear()
            Ausgabefluss(f"Gewählte Zone: {start}")
            break
        else:
            Ausgabefluss("Unbekannte Zone. Bitte eine korrekte Zone auswählen.\n")
            continue
    while True: #Zielauswahl
        tarife_anzeigen()
        ziel = input("Bitte gib deine Zielzone ein: ").upper()
        if zonen_prüfung(ziel):
            clear()
            Ausgabefluss(f"Gewählte Zone: {ziel}")
            break
        else:
            Ausgabefluss("Unbekannte Zone. Bitte eine korrekte Zone auswählen.\n")
            continue

#Anzahl der Fahrgäste ermitteln
def anzahl():
    global anzahl
    while True: #Anzahl der Tickets
        try:
            anzahl = int(input("Bitte gib die Anzahl der Tickets ein: "))
            break
        except:
            Ausgabefluss("Üngültige Eingabe.")

#Nummer der Zone über die Eingabe finden
def zone_nummer(zone):
    for z in zonen:
        if z['Zone'] == zone:
            return z['Nummer']

#Standardpreis ohne Rabatte berechnen
def berechne_preis(start, ziel):
    global preis
    start_num = zone_nummer(start)
    ziel_num = zone_nummer(ziel)
    anzahl_zonen = abs(ziel_num - start_num) + 1
    preis = (2 + (anzahl_zonen - 1) * 1)*anzahl

#Zuordnugn de Rabattgruppen auf den jeweiligen Rabattwert
def rabattgruppe_zuordnen(auswahl):
    global rabatt
    for r in rabattgruppen:
                if r['Auswahl'] == auswahl:
                    rabatt = r['Wert']

#Userabfrage der Rabattzone
def rabatt_auswählen():
    Ausgabefluss(f"{'Rabatte'}")
    Ausgabefluss("-" * 4)
    for eintrag in rabattgruppen:
        Ausgabefluss(f"{eintrag['Auswahl']}. {eintrag['Art']:<23}: {eintrag['Rabatt']:>6}")
    Ausgabefluss("-" * 4)
    Ausgabefluss("Drücke 0 für keinen Rabatt")
    while True:
        auswahl = input("Rabattstufe auswählen: ")
        clear()
        try:
            auswahl = int(auswahl)
            break
        except:
            Ausgabefluss("Ungültige Eingabe")
    if auswahl == 0:
        Ausgabefluss("Keine Rabattstufe gewählt.\n")
        return
    elif auswahl == 3:
        if anzahl < 3:
            Ausgabefluss("Gruppenrabatt ist erst ab 3 Tickets möglich.")
            rabatt_auswählen()
        else:
            rabattgruppe_zuordnen(auswahl)
    else:    
        rabattgruppe_zuordnen(auswahl)

#Berechnung des Endpreis inkl. Rabatt
def endpreis():
    global preis
    preis = preis * (1-rabatt)
    Ausgabefluss(f"Ticketpreis beträgt {preis:.2f} €\n")

#Aufforderung zur Zahlung des Tickets
def bezahlung():
    global preis
    eingeworfen = 0
    while preis > eingeworfen:
        Ausgabefluss(f"Bisher eingeworfen: {eingeworfen:.2f} €\n")
        Ausgabefluss(f"Bitte noch {preis-eingeworfen:.2f} € einwerfen\n")
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
        Ausgabefluss(f"Zahlung bestätigt.\nTicket wird ausgegeben.")
        input()
    else:
        Ausgabefluss(f"Zahlung bestätigt.\nTicket wird ausgegeben.")
        Ausgabefluss(f"{eingeworfen - preis:.2f} € zuviel bezahlt.\nWechselgeld wird ausgegeben.")
        input()
        
tarife_anzeigen()
zonenauswahl()
anzahl()
berechne_preis(start, ziel)
rabatt_auswählen()
endpreis()
bezahlung()

