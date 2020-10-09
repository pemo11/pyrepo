# Ein Poker Casino Automat mit TkInter
# Erstellt: 29/09/20
# V4: Mit Einsatz (Chips)

# Grundsätzlich funktioniert es
# Optisch noch nicht optimal
# Variablen wie einsatz oder hand als Instanzenvariablen?
# Abfrage, ob Anzahl der Chips für einen Einsatz reicht
# Spielende bei 0 Chips

from os import path, listdir
from tkinter import *
from tkinter import messagebox
import random
import time

cardsPath = path.join(path.dirname(__file__), "PokerCards")

# defaultCardname = "PokercardBack.png"
defaultCardname = "green_back.png"
sampleFactor = 5
jettons = 25

# Jeder Hand ist ein Tupel mit der Anzahl der Jettons für 1-5 Jettons zugeordnet
pokerMatrix = {
    "Nichts":(0,0,0,0,0),
    "Ein Paar":(1,2,3,4,5),
    "Zwei Paare":(2,4,6,8,10),
    "Dreier":(3,6,9,12,15),
    "Kleine Strasse":(4,8,12,16,20),
    "Grosse Strasse":(5,10,15,20,24),
    "Flush":(6,12,18,24,30),
    "Full House":(9,18,27,36,45),
    "Vierer":(25,50,75,100,125),
    "Straight Flush":(50,100,150,200,250),
    "Royal Flush":(250,500,750,1000,4000)
}

cardDic = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,
 "Jack":11,"Queen":12,"King":13,"Ace":14}

def IstReihe(Cards):
    okFlag = True
    c1 = Cards[0]
    for c in Cards[1:]:
        okFlag = okFlag and abs(c.Value - c1.Value) == 1
        c1 = c
    return okFlag

# Gibt an, ob ein Kartensatz eine Straße ist
# 0 - keine Straße, 1 - kleine Straße, 2 - große Straße
def StrassenTyp(Cards):
    # Karten zuerst sortieren
    sortedCards = sorted(Cards, key=lambda c: c.Value)
    if IstReihe(sortedCards):
        if Cards[4].Value == cardDic["Ace"]:
            return 2
        else:
            return 1
    else:
        return 0

# Gibt die Gruppen in einer Zahlenfolge zurück
def WertGruppen(Cards):
    d = {}
    for c in Cards:
        d[c.Value] = 1 if d.get(c.Value) == None else d[c.Value] + 1
    return d

# Teil das Kartenset in Gruppen nach den Farben ein
def FarbGruppen(Cards):
    d = {}
    for c in Cards:
        d[c.Color] = 1 if d.get(c.Color) == None else d[c.Color] + 1
    return d

# Gibt an, ob alle Karten die gleiche Farbe besitzen
def GleicheFarbe(Cards):
    # Jedes Element als Objekt mit dem Attribut Farbe vergleichen
    alleGleich = True
    for c in Cards:
        alleGleich = alleGleich and (True if [c1 for c1 in Cards if c1.Color != c.Color] == [] else False)
    return alleGleich

def AnzahlGruppen(Gruppe,Laenge):
    # Gibt es eine Gruppe mit n Elementen?
    r = len([g for g in Gruppe.items() if g[1] == Laenge])
    return r

# Definiert die Eigenschaften einer Karte
class PokerCard:

    def __init__(self, Name, Path):
        self.ImgPath = Path
        # Der Value ist eine Zahl von 1 bis 14, die sich aus dem zweiten Namensbestandteil der Datei ableitet
        self.Value = cardDic[Name.split("_")[0]]
        self.Color = Name.split("_")[1]
 
# Liest alle Bitmapdateien aus einem Verzeichnis ein und gibt eine Liste mit PokerCard-Objekten zurück
def ReadPokerCards(DirPath, DefaultCard):
    imgPfade = [path.join(cardsPath, f) for f in listdir(DirPath) if path.splitext(f)[1] == ".png" and f != DefaultCard]
    cardList = []
    for imgPfad in imgPfade:
        cardName = path.splitext(path.basename(imgPfad))[0]
        cardList.append(PokerCard(cardName, imgPfad))
    return cardList

# Definiert das Fenster der Anwendung
class Window(Frame):

    # Set von 0-5 Karten zusammenstellen und als Tupel (position,cardIndex) in cardList ablegen
    def Kartenmix(self):
        # 5 einzelne Zufallszahlen erzeugen
        # for _ in range(0, len(self.cavPicListe) + 1):
        # Gehe nur die Karten durch, die nicht selektiert sind
        self.cardIndexList = []
        # Geniale Syntax
        # Liste aller Tupels mit Index und Werte, die nicht gehalten werden
        self.keepList1 = [(i,v) for i,v in enumerate(self.selectList) if v == False]
        # Liste aller Kartennummern, die gehalten werden und damit nicht erneut gezogen werden dürfen
        self.keepIndex = [i for i,v in enumerate(self.selectList) if v == True]
        self.keepCards = [self.cardList[i][1] for i in self.keepIndex] 
        for t in self.keepList1:
            while True:
                z = random.randint(0, len(self.cards) - 1)
                # Ebenfalls geniale Syntax: Testen ob z in einem der Tupel als zweiter Wert vorkommt
                if z not in self.cardIndexList and z not in self.keepCards:
                    # cardListIndex enthält die Kartennummer für alle Cards
                    # cardList enthält Tupels mit der Position der Karte und dem Kartenindex
                    self.cardIndexList.append(z)
                    self.cardList[t[0]] = (t[0],z)
                    break

    #  Den aktuellen Kartenset anhand von cardIndexList anzeigen
    def KartenAnzeigen(self):
        # Liste wird nur benötigt, damit alle Bilder "am Leben bleiben"
        self.cardpicList = []
        for t in self.cardList:
            self.cavPic = self.cavPicListe[t[0]]
            self.card = self.cards[t[1]]
            self.imgCard = PhotoImage(file=self.card.ImgPath)
            # Dauert "ewig" bzw. Out of memory
            ## self.imgCard = self.imgCard.zoom(100)
            # subsample() als Alternative - geht gut, muss aber int sein, so dass
            # nur eine grobe Skalierung möglich ist
            # Am besten geht es vermutlich mit PIL (Pillow)
            # self.imgCard = self.imgCard.subsample(2, 2)
            self.imgCard = self.imgCard.subsample(sampleFactor)
            self.cardpicList.append(self.imgCard)
            self.cavPic.create_image(0,0,anchor=NW,image=self.imgCard)

    # Bewerten der Hand
    def Bewerten(self):
        hand = ""
        cardSet = [self.cards[t[1]] for t in self.cardList]
        werte = WertGruppen(cardSet)
        # farben = FarbGruppen(cardSet)
        # Testen auf Royal Flush
        if GleicheFarbe(cardSet) and StrassenTyp(cardSet) == 2:
            hand = "Royal Flush"
        elif GleicheFarbe(cardSet)  and StrassenTyp(cardSet) == 1:
            hand = "Straight Flush"
        elif GleicheFarbe(cardSet):
            hand = "Flush"
        elif AnzahlGruppen(werte, 4) == 1:
            hand = "Vierer"
        elif AnzahlGruppen(werte,2) == 1 and AnzahlGruppen(werte,3) == 1:
            hand = "Full House"
        elif StrassenTyp(cardSet) == 2:
            hand = "Grosse Strasse"
        elif StrassenTyp(cardSet) == 1:
            hand = "Kleine Strasse"
        elif AnzahlGruppen(werte,3) == 1:
            hand = "Dreier"
        elif AnzahlGruppen(werte,2) == 2:
            hand = "Zwei Paare"
        # TODO: Kartenwert muss Bube, Dame, König oder Ass sein
        elif AnzahlGruppen(werte,2) == 1:
            hand = "Ein Paar"
        else:
            hand = "Nichts"
        return hand

    # Neues Spiel
    def playButton(self):
        global jettons
        # Wurden mehr als 5 Jettons gesetzt?
        einsatz = int(self.tbEinsatz.get("1.0",END))
        if einsatz <= 0 or einsatz > 5:
            messagebox.showinfo(master=self, title="Hinweis", message="Dein Einsatz muss 1,2,3,4 oder 5 Jettons betragen")
            return
        self.ErsteRunde = not self.ErsteRunde
        if self.ErsteRunde:
            self.selectList = [False for _ in range(0,5)]
            for btn in self.btnList:
                btn.configure(bg = "SystemButtonFace")
            self.lblHand["text"] = "Halte 1-5 Karten"
        self.Kartenmix()
        self.KartenAnzeigen()
        if not self.ErsteRunde:
            # nicht ganz sauber mit lokalen Variablen
            hand = self.Bewerten()
            # Einsatz von den vorhandenen Chips abziehen
            jettons -= einsatz
            jettons += pokerMatrix[hand][einsatz-1]
            self.lblChips["text"] = jettons
            self.lblHand["text"] = hand
            for btn in self.btnList:
                btn.configure(bg = "SystemButtonFace")

    def keepButton(self, i):
        i -= 1
        # Markierung umdrehen in der ersten Runde
        if not self.ErsteRunde:
            return
        self.selectList[i] = not self.selectList[i]
        if self.btnList[i]["bg"] == "red":
            # genial: SystemButtonFace
            self.btnList[i].configure(bg = "SystemButtonFace")
        else:
            self.btnList[i].configure(bg = "red")
                            
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # self.pack(fill=BOTH, expand=1)
        self.lblTitel = Label(master, text="PyPoker 0.4")
        self.lblTitel.pack()
        self.btnList = []
        self.selectList = []
        self.cardList = [0 for _ in range(0,5)]
        self.ErsteRunde = False

        # Nur prosivorisch
        self.selectList = [False for _ in range(0,5)]

        # Ein Frame für alle Karten
        self.frmCards = Frame(master)
        self.frmCards.pack(side=TOP)

        # Für jede Kombination aus Canvas und Button ein eigenes Frame
        self.frmCard1 = Frame(self.frmCards)
        self.frmCard1.pack(side=LEFT,padx=10)
        self.cavPic1 = Canvas(self.frmCard1,width=160,height=220)   
        self.cavPic1.pack(side=TOP)
        self.btnKeep1 = Button(self.frmCard1, text="Halten", width=12, command= lambda: self.keepButton(1))
        self.btnKeep1.pack(side=TOP)
        self.btnList.append(self.btnKeep1)

        self.frmCard2 = Frame(self.frmCards)
        self.frmCard2.pack(side=LEFT,padx=10)
        self.cavPic2 = Canvas(self.frmCard2,width=160,height=220)   
        self.cavPic2.pack(side=TOP)
        self.btnKeep2 = Button(self.frmCard2, text="Halten", width=12, command= lambda: self.keepButton(2))
        self.btnKeep2.pack(side=BOTTOM)
        self.btnList.append(self.btnKeep2)

        self.frmCard3 = Frame(self.frmCards)
        self.frmCard3.pack(side=LEFT,padx=10)
        self.cavPic3 = Canvas(self.frmCard3,width=160,height=220)   
        self.cavPic3.pack(side=TOP)
        self.btnKeep3 = Button(self.frmCard3, text="Halten", width=12, command= lambda: self.keepButton(3))
        self.btnKeep3.pack(side=BOTTOM)
        self.btnList.append(self.btnKeep3)

        self.frmCard4 = Frame(self.frmCards)
        self.frmCard4.pack(side=LEFT,padx=10)
        self.cavPic4 = Canvas(self.frmCard4,width=160,height=220)   
        self.cavPic4.pack(side=TOP)
        self.btnKeep4 = Button(self.frmCard4, text="Halten", width=12, command= lambda: self.keepButton(4))
        self.btnKeep4.pack(side=BOTTOM)
        self.btnList.append(self.btnKeep4)

        self.frmCard5 = Frame(self.frmCards)
        self.frmCard5.pack(side=LEFT,padx=10)
        self.cavPic5 = Canvas(self.frmCard5,width=160,height=220)   
        self.cavPic5.pack(side=TOP)
        self.btnKeep5 = Button(self.frmCard5, text="Halten", width=12, command= lambda: self.keepButton(5))
        self.btnKeep5.pack(side=BOTTOM)
        self.btnList.append(self.btnKeep5)

        # Mit Hintergrund initialisieren
        self.imgPath = path.join(cardsPath, defaultCardname)
        self.img1 = PhotoImage(file=self.imgPath).subsample(sampleFactor)
        self.img2 = PhotoImage(file=self.imgPath).subsample(sampleFactor)  
        self.img3 = PhotoImage(file=self.imgPath).subsample(sampleFactor)  
        self.img4 = PhotoImage(file=self.imgPath).subsample(sampleFactor)
        self.img5 = PhotoImage(file=self.imgPath).subsample(sampleFactor)
        self.imgListe = [self.img1, self.img2, self.img3, self.img4, self.img5]

        self.cavPic1.create_image(0,0,anchor=NW,image=self.img1)
        self.cavPic2.create_image(0,0,anchor=NW,image=self.img2)
        self.cavPic3.create_image(0,0,anchor=NW,image=self.img3)
        self.cavPic4.create_image(0,0,anchor=NW,image=self.img4)
        self.cavPic5.create_image(0,0,anchor=NW,image=self.img5)

        self.cavPicListe = [self.cavPic1,self.cavPic2,self.cavPic3,self.cavPic4,self.cavPic5]

        self.cards = ReadPokerCards(cardsPath, defaultCardname)

        # Schritt: Refaktorisierung, also Auslagern einer Befehlsfolge in eine Function

        # Gibt eine Liste mit 5 Zahlen ohne "Doppelte" zurück

        self.bntPlay = Button(root, text="Play", command=self.playButton)
        self.bntPlay.pack()

        self.lblHand = Label(root, text="Ergebnis")
        self.lblHand.pack()

        # Ausgabe der eigenen Chips
        self.lblChipsCap = Label(root, text="Deine Jettons")
        self.lblChipsCap.config(font=("Arial", 24))
        self.lblChipsCap.pack()

        self.lblChips = Label(root, width=5, text=jettons)
        self.lblChips.config(font=("Arial", 24))
        self.lblChips.configure(bg = "lightgreen")
        self.lblChips.pack()

        self.lblEinsatz = Label(root, text="Dein Einsatz (1-5 Jettons)")
        self.lblEinsatz.config(font=("Arial", 24))
        self.lblEinsatz.pack()

        # Textbox für die Eingabe des Einsatzes
        self.tbEinsatz = Text(root, height=1,width=4)
        self.tbEinsatz.config(font=("Arial", 24))
        self.tbEinsatz.insert(END,"5")
        self.tbEinsatz.pack()



root = Tk()
root.title("PyPoker 0.4")
root.geometry("900x600")
win = Window(root)
win.mainloop()
