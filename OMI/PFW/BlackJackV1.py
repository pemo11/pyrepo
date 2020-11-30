# Ein BlackJack-Spiel gegen den Computer mit tkinter
# Erstellt: 18/10/20, Letzte Aktualisierung: 21/10/20

# Funktioniert grundsätzlich:)
# TODO: Einsatz

from os import path, listdir
from tkinter import *
from tkinter import messagebox
import random
import time
from datetime import datetime

# Globale Variablen
cardsPath = path.join(path.dirname(__file__), "Cards")
logPath = path.join(path.dirname(__file__), "pyblackjack.log")

defaultCardname = "green_back.png"
defaultCardpath = path.join(cardsPath, defaultCardname)

# Vergrößerungsfaktor für die Spielkarten-Bitmaps (nur provisorisch)
cardList = None
scaleFactor = 5
valueDealer = 0
valuePlayer = 0
gameOver = False

# Der Wert des Ass wird "situativ" berechnet
cardDic = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,
 "Jack":10,"Queen":10,"King":10,"Ace":10}

# Definiert die Eigenschaften einer Karte
class Card:

    def __init__(self, Name, Path):
        self.ImgPath = Path
        # Der Value ist eine Zahl von 1 bis 10, die sich aus dem zweiten Namensbestandteil der Datei ableitet
        self.Value = cardDic[Name.split("_")[0]]
        self.ValueName = Name.split("_")[0]
        self.Color = Name.split("_")[1]

# Definiert das Fenster der Anwendung
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # Alle Listen an einer Stelle initialisieren
        # Eventuell genügt die Variable currentDeck mit einem Dealer/Player-Flag => tupel
        self.cavDealerList = []
        self.cavPlayerList = []
        self.imgDealerList = []
        self.imgPlayerList = []
        self.dealerCards = []
        self.playerCards = []
        self.currentDeck = []
        self.dealerCards = []
        self.playerCards = []

        lblTitel = Label(master, text="BlackJack-Casino v0.3",font = "Helvetica 36 bold",fg="red")
        # Nummerierung der Zeilen, Spalten beginnt bei 0
        lblTitel.grid(row=0,column=0)
        fraButtons = Frame(master)
        fraButtons.grid(row=1,column=0)
        btnDeal = Button(fraButtons, text="Deal", width=16, command=self.deal)
        btnDeal.pack(side=LEFT)
        btnHit = Button(fraButtons, text="Hit", width=16, command=self.hit)
        btnHit.pack(side=LEFT)
        btnStand = Button(fraButtons, text="Stand", width=16, command=self.stand)
        btnStand.pack(side=LEFT)
        btnQuit = Button(fraButtons, text="Quit", width=16, command=self.quit)
        btnQuit.pack(side=LEFT)
        
        self.frmDealerCards = Frame(master)
        self.frmDealerCards.grid(row=2, column=0,sticky=W)

        self.frmPlayerCards = Frame(master)
        self.frmPlayerCards.grid(row=3, column=0,sticky=W)

        self.lblDealerValue = Label(master, text="0", font="Helvetica 20",fg="green")
        self.lblDealerValue.grid(row=4, column=0,sticky=SW)

        self.lblPlayerValue = Label(master, text="0", font="Helvetica 20",fg="blue")
        self.lblPlayerValue.grid(row=4, column=1,sticky=SW)

        # Spalten und Zeilen sollen mehr Platz bekommen
        # Bei nur einer Spalte nicht erforderlich?
        master.columnconfigure(0, weight=1)
        # master.rowconfigure(1, weight=1)
        master.rowconfigure(2, weight=1)
        master.rowconfigure(3, weight=1)

    # Berechnet den Wert eines Kartenstapels
    def calculate(self,cards):
        value = 0
        for card in cards:
            value += cardDic[card.ValueName]
        # Müssen die Asse anders gezählt werden?
        if value > 21:
            asse = [c for c in cards if c.ValueName == "Ace"]
            for _ in asse:
                # Pro Ass 9 Punkte abziehen, aus Ass+König+9 = 29 wird so 20
                value -= 9
        return value

    def deal(self):
        global gameOver, playerValue
        gameOver = False
        # Alle angezeigten Karten als Canvas-Widgets des Dealers und des Players entfernen
        self.currentDeck.clear()
        self.cavDealerList.clear()
        self.cavPlayerList.clear()
        self.imgDealerList.clear()
        self.imgPlayerList.clear()
        self.dealerCards.clear()
        self.playerCards.clear()
        self.currentDeck.clear()
        self.dealerCards.clear()
        self.playerCards.clear()
        # Alle Widgets aus den beiden Frames entfernen
        for widget in self.frmDealerCards.winfo_children() + self.frmPlayerCards.winfo_children():
            widget.destroy()
        # Ist das auch erfoerderlich? Kann wahrscheinlich wieder raus
        for cav in self.cavDealerList + self.cavPlayerList:
            # cav.pack_forget()
            cav.destroy()

        # Zwei Karten für den Dealer, eine wird verdeckt angezeigt
        for _ in range(0,2):
            exitFlag = False
            while not exitFlag:
                z = random.randint(0, len(cardList) - 1)
                if z not in self.currentDeck:
                    self.currentDeck.append(z)
                    self.dealerCards.append(cardList[z])
                    exitFlag = True
            cavPic = Canvas(self.frmDealerCards,width=160,height=220)
            cavPic.pack(side=LEFT)
            self.cavDealerList.append(cavPic)
            imgNeu = PhotoImage(file=cardList[z].ImgPath).subsample(scaleFactor)
            self.imgDealerList.append(imgNeu)
            if _ == 0:
                # Das erste Image muss für die spätere Anzeige zwischengespeichert werden
                imgNeu = PhotoImage(file=defaultCardpath).subsample(scaleFactor)
                self.backcardImage = imgNeu
            cavPic.create_image(0,0,anchor=NW,image=imgNeu)
        # Eine Karte für den Spieler
        cavPic = Canvas(self.frmPlayerCards,width=160,height=220)   
        cavPic.pack(side=LEFT)
        self.cavPlayerList.append(cavPic)
        exitFlag = False
        while not exitFlag:
            z = random.randint(0, len(cardList) - 1)
            if z not in self.currentDeck:
                self.currentDeck.append(z)
                self.playerCards.append(cardList[z])
                exitFlag = True
        img = PhotoImage(file=cardList[z].ImgPath).subsample(scaleFactor)
        cavPic.create_image(0,0,anchor=NW,image=img)
        self.imgPlayerList.append(img)
        # Aktuellen Wert der Dealer-Karten berechnen
        dealerValue = self.calculate(self.dealerCards)
        self.lblDealerValue["text"] = "Dealer: " + str(dealerValue)
        # Hat der Dealer bereits gewonnen oder verloren?
        if dealerValue == 21:
            messagebox.showinfo(title="PyBlackJack", message="BlackJack - die Bank gewinnt!")
            gameOver = True
        elif dealerValue > 21:
            messagebox.showinfo(title="PyBlackJack", message="Die Bank verloren!")
            gameOver = True
        if gameOver:
            # Verzögerung über sleep() nicht ganz optimal, da blockierend
            time.sleep(0.4)
            self.onUpdate()
            # Verdeckte Karte aufdecken
            cav = self.cavDealerList[0]
            img = self.imgDealerList[0]
            # Optional
            cav.delete(ALL)
            # mit itemconfig geht es einfach nicht?
            # cav.itemconfig(imgBack,image=img)
            cav.create_image(0,0,anchor=NW,image=img)

        # Aktuellen Wert der Player-Karten berechnen
        playerValue = self.calculate(self.playerCards)
        self.lblPlayerValue["text"] = "Player: " + str(playerValue)

    # Eine weitere Karte für den Spieler
    def hit(self):
        global gameOver, playerValue
        # Eine Karte für den Spieler
        cavPic = Canvas(self.frmPlayerCards,width=160,height=220)   
        cavPic.pack(side=LEFT)
        self.cavPlayerList.append(cavPic)
        exitFlag = False
        while not exitFlag:
            z = random.randint(0, len(cardList) - 1)
            if z not in self.currentDeck:
                self.currentDeck.append(z)
                self.playerCards.append(cardList[z])
                exitFlag = True
        img = PhotoImage(file=cardList[z].ImgPath).subsample(scaleFactor)
        cavPic.create_image(0,0,anchor=NW,image=img)
        self.imgPlayerList.append(img)
        # Aktuellen Wert der Player-Karten berechnen
        playerValue = self.calculate(self.playerCards)
        self.lblPlayerValue["text"] = "Player: " + str(playerValue)
        # Hat der Player gewonnen oder verloren?
        if playerValue == 21:
            messagebox.showinfo(title="PyBlackJack", message="BlackJack - der Spieler hat gewonnen!")
            gameOver = True
        elif playerValue > 21:
            messagebox.showinfo(title="PyBlackJack", message="Der Spieler hat verloren!")
            gameOver = True
        if gameOver:
            # Verzögerung über sleep() nicht ganz optimal, da blockierend
            time.sleep(0.4)
            self.onUpdate()
            img = self.imgDealerList[0]
            cav = self.cavDealerList[0]
            cav.create_image(0,0,anchor=NW,image=img)

    def onUpdate(self):
        self.after(1000, self.onUpdate)

    # Player ist fertig, der Dealer ist an der Reihe 
    def stand(self):
        global gameOver, playerValue
        # Weitere Karten ziehen bis das Spiel zu Ende ist
        while not gameOver:
            exitFlag = False
            while not exitFlag:
                z = random.randint(0, len(cardList) - 1)
                if z not in self.currentDeck:
                    self.currentDeck.append(z)
                    self.dealerCards.append(cardList[z])
                    exitFlag = True
            cavPic = Canvas(self.frmDealerCards,width=160,height=220)
            cavPic.pack(side=LEFT)
            self.cavDealerList.append(cavPic)
            img = PhotoImage(file=cardList[z].ImgPath).subsample(scaleFactor)
            cavPic.create_image(0,0,anchor=NW,image=img)
            self.imgDealerList.append(img)
            # Aktuellen Wert der Dealer-Karten berechnen
            dealerValue = self.calculate(self.dealerCards)
            self.lblDealerValue["text"] = "Dealer: " + str(dealerValue)
            # Hat der Dealer gewonnen oder verloren?
            if dealerValue == 21:
                messagebox.showinfo(title="PyBlackJack", message="BlackJack - die Bank gewinnt!")
                gameOver = True
            elif dealerValue > 21:
                messagebox.showinfo(title="PyBlackJack", message="Die Bank verloren!")
                gameOver = True
            elif dealerValue > playerValue:
                messagebox.showinfo(title="PyBlackJack", message="Die Bank gewinnt!")
                gameOver = True
            # Verzögerung über sleep() nicht ganz optimal, da blockierend
            time.sleep(0.4)
            self.onUpdate()
        # Verdeckte Dealer-Karte aufdecken
        cav = self.cavDealerList[0]
        img = self.imgDealerList[0]
        # Optional
        cav.delete(ALL)
        cav.create_image(0,0,anchor=NW,image=img)
        # Verzögerung über sleep() nicht ganz optimal, da blockierend
        time.sleep(0.4)
        self.onUpdate()

    # Spiel beenden
    def quit(self):
        self.master.destroy()

# Liest alle Bitmapdateien aus einem Verzeichnis ein und gibt eine Liste mit Card-Objekten zurück
def ReadCards(DirPath, DefaultCard):
    imgPaths = [path.join(cardsPath, f) for f in listdir(DirPath) if path.splitext(f)[1] == ".png" and f != DefaultCard]
    cardList = []
    for imgPath in imgPaths:
        cardName = path.splitext(path.basename(imgPath))[0]
        cardList.append(Card(cardName, imgPath))
    return cardList

# Alle Karten als Card-Objekte einlesen
cardList = ReadCards(cardsPath, defaultCardname)

root = Tk()
root.title("BlackJack 0.3")
root.geometry("900x600")
win = Window(root)
win.mainloop()
