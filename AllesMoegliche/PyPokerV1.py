# Ein Poker Casino Automat mit TkInter
# Erstellt: 13/09/20
# V1: Kann nur Karten anzeigen, ohne Auswahloptio

from os import path, listdir
from tkinter import *
import random
import time

cardsPath = path.join(path.dirname(__file__), "PokerCards")
# defaultCardname = "PokercardBack.png"
defaultCardname = "green_back.png"
sampleFactor = 5

class PokerCard:

    def __init__(self, Name, Path):
        self.ImgPath = Path
        self.Color = Name.split("_")[0]
        self.Value = Name.split("_")[1]

def ReadPokerCards(DirPath, DefaultCard):
    imgPfade = [path.join(cardsPath, f) for f in listdir(DirPath) if path.splitext(f)[1] == ".png" and f != DefaultCard]
    imgList = []
    for imgPfad in imgPfade:
        cardName = path.splitext(imgPfad)[0]
        imgList.append(PokerCard(cardName, imgPfad))
    return imgList

class Window(Frame):

    def Kartenmix(self):
        self.cardIndexList = []
        # 5 einzelne Zufallszahlen erzeugen
        for _ in range(0, len(self.cavPicListe) + 1):
            while True:
                z = random.randint(0, len(self.cards)-1)
                if z not in self.cardIndexList:
                    self.cardIndexList.append(z)
                    break

    #  Den aktuellen Kartenset anhand von cardIndexList anzeigen
    def KartenAnzeigen(self):
        self.cardList = []
        for i in range(0, len(self.cavPicListe)):
            self.cavPic = self.cavPicListe[i]
            self.card = self.cards[self.cardIndexList[i]]
            self.imgCard = PhotoImage(file=self.card.ImgPath)
            # Dauert "ewig" bzw. Out of memory
            ## self.imgCard = self.imgCard.zoom(100)
            # subsample() als Alternative - geht gut, muss aber int sein, so dass
            # nur eine grobe Skalierung möglich ist
            # Am besten geht es vermutlich mit PIL (Pillow)
            # self.imgCard = self.imgCard.subsample(2, 2)
            self.imgCard = self.imgCard.subsample(sampleFactor)
            self.cardList.append(self.imgCard)
            self.cavPic.create_image(0,0,anchor=NW,image=self.imgCard)

    # Neues Spiel
    def playButton(self):
        self.Kartenmix()
        self.KartenAnzeigen()

    # Im Dauermodus 5er-Paare anzeigen
    def startDemoButton(self):
        Window.runDemo = True
        while Window.runDemo:
            self.Kartenmix()
            self.KartenAnzeigen()
            # Erforderlich, damit die Anzeige "refresht" wird
            root.update()
            time.sleep(1)

    def stopDemoButton(self):
        Window.runDemo = False

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # self.pack(fill=BOTH, expand=1)
        self.lblTitel = Label(master, text="PyPoker 0.1")
        self.lblTitel.pack()

        self.frmCards = Frame(master)
        self.frmCards.pack()

        self.cavPic1 = Canvas(self.frmCards,width=160,height=240)   
        self.cavPic1.pack(side=LEFT)
        self.cavPic2 = Canvas(self.frmCards,width=160,height=240)   
        self.cavPic2.pack(side=LEFT)
        self.cavPic3 = Canvas(self.frmCards,width=160,height=240)   
        self.cavPic3.pack(side=LEFT)
        self.cavPic4 = Canvas(self.frmCards,width=160,height=240)   
        self.cavPic4.pack(side=LEFT)
        self.cavPic5 = Canvas(self.frmCards,width=160,height=240)   
        self.cavPic5.pack()

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
        self.bntStartDemo = Button(root, text="Start Demo", command=self.startDemoButton)
        self.bntStartDemo.pack()
        self.bntStopDemo = Button(root, text="Stop Demo", command=self.stopDemoButton)
        self.bntStopDemo.pack()

root = Tk("PyPoker 0.1")
root.geometry("800x600")
win = Window(root)
win.mainloop()

# Aktuell wird nur die letzte Karte angezeigt ???
# Problem gelöst: Das PhotoImage-Objekt muss in einer Liste abgelegt werden, sonst wird es überschrieben
# Nächstes Problem: Skalierung - Lösung: zoom() oder besser Pillow per PIP installieren