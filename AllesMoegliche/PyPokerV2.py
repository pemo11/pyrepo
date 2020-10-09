# Ein Poker Casino Automat mit TkInter
# Erstellt: 24/09/20, 25/09/20 - läuft!
# V2: Mit Auswahloption

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

    def keepButton(self, i):
        i -= 1
        # Markierung umdrehen
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
        self.lblTitel = Label(master, text="PyPoker 0.2")
        self.lblTitel.pack()
        self.btnList = []
        self.selectList = []
        self.cardList = [0 for _ in range(0,5)]

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
        self.btnKeep1 = Button(self.frmCard1, text="Keep", width=12, command= lambda: self.keepButton(1))
        self.btnKeep1.pack(side=TOP)
        self.btnList.append(self.btnKeep1)

        self.frmCard2 = Frame(self.frmCards)
        self.frmCard2.pack(side=LEFT,padx=10)
        self.cavPic2 = Canvas(self.frmCard2,width=160,height=220)   
        self.cavPic2.pack(side=TOP)
        self.btnKeep2 = Button(self.frmCard2, text="Keep", width=12, command= lambda: self.keepButton(2))
        self.btnKeep2.pack(side=BOTTOM)
        self.btnList.append(self.btnKeep2)

        self.frmCard3 = Frame(self.frmCards)
        self.frmCard3.pack(side=LEFT,padx=10)
        self.cavPic3 = Canvas(self.frmCard3,width=160,height=220)   
        self.cavPic3.pack(side=TOP)
        self.btnKeep3 = Button(self.frmCard3, text="Keep", width=12, command= lambda: self.keepButton(3))
        self.btnKeep3.pack(side=BOTTOM)
        self.btnList.append(self.btnKeep3)

        self.frmCard4 = Frame(self.frmCards)
        self.frmCard4.pack(side=LEFT,padx=10)
        self.cavPic4 = Canvas(self.frmCard4,width=160,height=220)   
        self.cavPic4.pack(side=TOP)
        self.btnKeep4 = Button(self.frmCard4, text="Keep", width=12, command= lambda: self.keepButton(4))
        self.btnKeep4.pack(side=BOTTOM)
        self.btnList.append(self.btnKeep4)

        self.frmCard5 = Frame(self.frmCards)
        self.frmCard5.pack(side=LEFT,padx=10)
        self.cavPic5 = Canvas(self.frmCard5,width=160,height=220)   
        self.cavPic5.pack(side=TOP)
        self.btnKeep5 = Button(self.frmCard5, text="Keep", width=12, command= lambda: self.keepButton(5))
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
        self.bntStartDemo = Button(root, text="Start Demo", command=self.startDemoButton)
        self.bntStartDemo.pack()
        self.bntStopDemo = Button(root, text="Stop Demo", command=self.stopDemoButton)
        self.bntStopDemo.pack()

root = Tk("PyPoker 0.2")
root.geometry("900x600")
win = Window(root)
win.mainloop()

# Aktuell wird nur die letzte Karte angezeigt ???
# Problem gelöst: Das PhotoImage-Objekt muss in einer Liste abgelegt werden, sonst wird es überschrieben
# Nächstes Problem: Skalierung - Lösung: zoom() oder besser Pillow per PIP installieren