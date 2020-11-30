# Nur ein Test für die dynamische Anzeige von Bildern
# Es sollen nacheinander n Karten mit einer Verzögerung eingeblendet werden
# Erstellt: 22/10/20

from os import path, listdir
from tkinter import *
import random
import time

# Globale Variablen
cardsPath = path.join(path.dirname(__file__), "cards")
logPath = path.join(path.dirname(__file__), "pyblackjack.log")
anzahl = 5

defaultCardname = "green_back.png"
defaultCardpath = path.join(cardsPath, defaultCardname)

cardDic = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,
 "Jack":10,"Queen":10,"King":10,"Ace":1}

cardList = None
imgList = None
scaleFactor = 5

class Card:

    def __init__(self, Name, Path):
        self.ImgPath = Path
        self.Value = cardDic[Name.split("_")[0]]
        self.ValueName = Name.split("_")[0]
        self.Color = Name.split("_")[1]

def ReadCards(DirPath, DefaultCard):
    imgPaths = [path.join(cardsPath, f) for f in listdir(DirPath) if path.splitext(f)[1] == ".png" and f != DefaultCard]
    cardList = []
    for imgPath in imgPaths:
        cardName = path.splitext(path.basename(imgPath))[0]
        cardList.append(Card(cardName, imgPath))
    return cardList

def ReadImages(Cards):
    imgList = []
    for card in Cards:
        imgList.append(PhotoImage(file=card.ImgPath).subsample(scaleFactor))
    return imgList

# Definiert das Fenster der Anwendung
class Window(Frame):

    def nextCard(self):
        exitFlag = False
        while not exitFlag:
            z = random.randint(0, len(cardList) - 1)
            if z not in self.currentDeck:
                self.currentDeck.append(z)
                exitFlag = True
        cavPic = Canvas(self.frmCards,width=160,height=220)
        cavPic.pack(side=LEFT)
        img = PhotoImage(file=cardList[z].ImgPath).subsample(scaleFactor)
        cavPic.create_image(0,0,anchor=NW,image=img)
        # Ohne diesen Anker bleibt die Bitmap unsichtbar
        self.imgList.append(img)
        self.cavList.append(cavPic)

    def start(self):
        # Durch das Leeren der Liste vermeide ich einen 
        # TclError: invalid command name ".!frame.!canvas"
        self.currentDeck.clear()
        self.cavList.clear()
        self.imgList.clear()
        for widget in self.frmCards.winfo_children():
            widget.destroy()
        for _ in range(0, anzahl):
            # Damit werden in diesem Fall alle Aufrufe verzögert und dann auf einmal angezeigt
            # self.after(1000, self.nextCard())
            self.nextCard()
            time.sleep(0.4)
            # Ohne update() wird der Canvas nicht sofort aktualisiert
            self.update()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.imgList = []
        self.cavList = []
        self.currentDeck = []
        # Behelfslösung mit einem Frame
        fraButtons = Frame()
        btnStart = Button(fraButtons,text="Start",width=16,command=self.start)
        btnStart.pack(side=LEFT,padx=10,pady=10)
        fraButtons.grid(row=0,column=0,sticky=NW)

        self.frmCards = Frame(master)
        self.frmCards.grid(row=1,sticky=W)

        ReadImages(cardList)
        # Höhe der ersten beiden Reihen wird vergrößert
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)

cardList = ReadCards(cardsPath,defaultCardname)

root = Tk()
root.title("Bitmaps zeitverzögert anzeigen")
root.geometry("800x400")
win = Window(root)
win.mainloop()
