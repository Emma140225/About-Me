from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser

#ASCII Bibliothek

buchstaben_muster = {
    "A": [
        "  ###  ",
        " ## ## ",
        "##   ##",
        "#######",
        "##   ##",
        "##   ##",
        "##   ##"
    ],
    "B": [
        "###### ",
        "##   ##",
        "##   ##",
        "###### ",
        "##   ##",
        "##   ##",
        "###### "
    ],
    "C": [
        " ######",
        "##     ",
        "##     ",
        "##     ",
        "##     ",
        "##     ",
        " ######"
    ],
    "D": [
        "#####  ",
        "##  ## ",
        "##   ##",
        "##   ##",
        "##   ##",
        "##  ## ",
        "#####  "
    ],
    "E": [
        "#######",
        "##     ",
        "##     ",
        "#####  ",
        "##     ",
        "##     ",
        "#######"
    ],
    "F": [
        "#######",
        "##     ",
        "##     ",
        "#####  ",
        "##     ",
        "##     ",
        "##     "
    ],
    "G": [
        " ##### ",
        "##     ",
        "##     ",
        "##  ###",
        "##   ##",
        "##   ##",
        " ##### "
    ],
    "H": [
        "##   ##",
        "##   ##",
        "##   ##",
        "#######",
        "##   ##",
        "##   ##",
        "##   ##"
    ],
    "I": [
        "#######",
        "   ##  ",
        "   ##  ",
        "   ##  ",
        "   ##  ",
        "   ##  ",
        "#######"
    ],
    "J": [
        "###### ",
        "    ## ",
        "    ## ",
        "    ## ",
        "##  ## ",
        "##  ## ",
        " ####  "
    ],
    "K": [
        "##   ##",
        "##  ## ",
        "## ##  ",
        "####   ",
        "## ##  ",
        "##  ## ",
        "##   ##"
    ],
    "L": [
        "##     ",
        "##     ",
        "##     ",
        "##     ",
        "##     ",
        "##     ",
        "#######"
    ],
    "M": [
        "##   ##",
        "### ###",
        "#######",
        "## # ##",
        "##   ##",
        "##   ##",
        "##   ##"
    ],
    "N": [
        "##   ##",
        "###  ##",
        "#### ##",
        "## ####",
        "##  ###",
        "##   ##",
        "##   ##"
    ],
    "O": [
        " ##### ",
        "##   ##",
        "##   ##",
        "##   ##",
        "##   ##",
        "##   ##",
        " ##### "
    ],
    "P": [
        "###### ",
        "##   ##",
        "##   ##",
        "###### ",
        "##     ",
        "##     ",
        "##     "
    ],
    "Q": [
        " ##### ",
        "##   ##",
        "##   ##",
        "##   ##",
        "## # ##",
        "##  ## ",
        " ### ##"
    ],
    "R": [
        "###### ",
        "##   ##",
        "##   ##",
        "###### ",
        "## ##  ",
        "##  ## ",
        "##   ##"
    ],
    "S": [
        " ######",
        "##     ",
        "##     ",
        " ##### ",
        "     ##",
        "     ##",
        "###### "
    ],
    "T": [
        "#######",
        "   ##  ",
        "   ##  ",
        "   ##  ",
        "   ##  ",
        "   ##  ",
        "   ##  "
    ],
    "U": [
        "##   ##",
        "##   ##",
        "##   ##",
        "##   ##",
        "##   ##",
        "##   ##",
        " ##### "
    ],
    "V": [
        "##   ##",
        "##   ##",
        "##   ##",
        "##   ##",
        " ## ## ",
        " ## ## ",
        "  ###  "
    ],
    "W": [
        "##   ##",
        "##   ##",
        "##   ##",
        "## # ##",
        "#######",
        "### ###",
        "##   ##"
    ],
    "X": [
        "##   ##",
        " ## ## ",
        "  ###  ",
        "  ###  ",
        "  ###  ",
        " ## ## ",
        "##   ##"
    ],
    "Y": [
        "##   ##",
        " ## ## ",
        "  ###  ",
        "   #   ",
        "   #   ",
        "   #   ",
        "   #   "
    ],
    "Z": [
        "#######",
        "     ##",
        "    ## ",
        "   ##  ",
        "  ##   ",
        " ##    ",
        "#######"
    ],
    "Ä" : [
        " ## ## ",
        "       ",
        "  ###  ",
        " ## ## ",
        "#######",
        "##   ##",
        "##   ##"
    ],
    "Ö" : [
        " ## ## ",
        "       ",
        " ##### ",
        "##   ##",
        "##   ##",
        "##   ##",
        " ##### "
    ],
    "Ü" : [
        " ## ## ",
        "       ",
        "##   ##",
        "##   ##",
        "##   ##",
        "##   ##",
        " ##### "
    ],
    " ": [
        "       ",
        "       ",
        "       ",
        "       ",
        "       ",
        "       ",
        "       "
    ],
    "default" : [
        "       ",
        "       ",
        "   ?   ",
        "   ?   ",
        "   ?   ",
        "       ",
        "       "
    ],
    "0": [
        "  ###  ",
        " ## ## ",
        "##  ###",
        "## # ##",
        "###  ##",
        " ## ## ",
        "  ###  "
    ],
    "1": [
        "   #   ",
        "  ##   ",
        " ###   ",
        "   #   ",
        "   #   ",
        "   #   ",
        " ##### "
    ],
    "2": [
        " ##### ",
        "##   ##",
        "     ##",
        "   ### ",
        "  ##   ",
        " ##    ",
        "#######"
    ],
    "3": [
        " ##### ",
        "##   ##",
        "     ##",
        "  #### ",
        "     ##",
        "##   ##",
        " ##### "
    ],
    "4": [
        "   ### ",
        "  #### ",
        " ## ## ",
        "##  ## ",
        "#######",
        "    ## ",
        "   ####"
    ],
    "5": [
        "#######",
        "##     ",
        "#####  ",
        "     ##",
        "     ##",
        "##   ##",
        " ##### "
    ],
    "6": [
        "  #### ",
        " ##    ",
        "##     ",
        "###### ",
        "##   ##",
        "##   ##",
        " ##### "
    ],
    "7": [
        "#######",
        "     ##",
        "    ## ",
        "   ##  ",
        "  ##   ",
        " ##    ",
        "##     "
    ],
    "8": [
        " ##### ",
        "##   ##",
        "##   ##",
        " ##### ",
        "##   ##",
        "##   ##",
        " ##### "
    ],
    "9": [
        " ##### ",
        "##   ##",
        "##   ##",
        " ######",
        "     ##",
        "    ## ",
        " ####  "
    ]
}

#Liste der Funktionen

#Aktion die beim Ändern Button ausgeführt wird
def reset_action():
    eingabe_name.delete(0, 'end')
    eingabe_zeichen.delete(0, 'end')
    ausgabe.config(text="")

def button_action():
    name = eingabe_name.get().upper()
    zeichen = eingabe_zeichen.get()
    if(name == ""):
        ausgabe.config(text="Gib einen Namen ein")
    else:
        ascii_lines = []
        for zeile in range(7):
            line = ""
            for buchstabe in name:
                line += buchstaben_muster.get(buchstabe, buchstaben_muster["default"])[zeile].replace("#", zeichen) + " "
            ascii_lines.append(line)
        ausgabe.config(text="\n".join(ascii_lines), fg=button_action.farbe)

# Standardfarbe initialisieren
button_action.farbe = "black"

def farb_wahl():
    farbe_tuple = colorchooser.askcolor()
    if farbe_tuple and farbe_tuple[1]:
        button_action.farbe = farbe_tuple[1]
        # Optional: Zeige die neue Farbe direkt an
        ausgabe.config(fg=button_action.farbe)


def action_get_info_dialog():
    m_text = "\
*********************\n\
Autor: Emma Paulus\n\
Datum: 01.08.2025\n\
Version: 1.1\n\
*********************"
    messagebox.showinfo(message=m_text, title="Info")

# Erstellt das Fenster
fenster = Tk()

#Label nach Bestätigung vom Namen
ausgabe = Label(fenster, font=("Courier", 10), justify="left")                                #ASCII Ausgabe

#Die verschiedenen Button hinzufügen
exit_button = Button(fenster, text="Beenden", command=fenster.quit)                                  #Beenden
bestätigung_button = Button(fenster, text="Bestätigen", command=button_action)
eingabe_name = Entry(fenster, bd=5, width=40)                                                        #Eingabe vom Namen
eingabe_zeichen = Entry(fenster, bd=5, width=40)                                                     #Eingabe vom gewünschten Zeichen
farbe = Button(fenster, text="Farbe", command=farb_wahl)

#Textzeilen hinzufügen
anweisung_label = Label(fenster, text="Gib hier bitte einen Namen ein.")
zeichen_label = Label(fenster, text="Gib hier das Zeichen ein das benutzt werden soll.")
info_label = Label(fenster, text="Der Beenden Button schließt das Programm")

#Der Titel vom Fenster
fenster.title("ASCII-Bild Generator")

#Menüleiste erstellen
menulist = Menu(fenster)

#Menü Info erstellen
datei_menu= Menu(menulist, tearoff=0)
help_menu = Menu(menulist, tearoff=0)

#Die Menüleiste ins Fenster einfügen
fenster.config(menu=menulist)

#Die Menübuttons einfügen
menulist.add_cascade(label="Datei", menu=datei_menu)
menulist.add_cascade(label="Help", menu=help_menu)

#Dropdown hinzufügen
datei_menu.add_command(label="Löschen", command=reset_action)
help_menu.add_command(label="Info", command=action_get_info_dialog)

#Button und Text in Fenster hinzufügen
anweisung_label.grid(row=0, column=0, pady=20)
eingabe_name.grid(row=0, column=1)
zeichen_label.grid(row=1, column=0)
eingabe_zeichen.grid(row=1, column=1)
farbe.grid(row=2, column=0)
bestätigung_button.grid(row=2, column=1)
ausgabe.grid(row=3)
info_label.grid(row=4, column=0)
exit_button.grid(row=4, column=1)


#Hauptschleife um auf Eingabe zu warten
fenster.mainloop()


