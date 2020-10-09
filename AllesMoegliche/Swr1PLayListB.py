# Auswerten der SWR1-Playlist für einen Monat - Teil 2

from bs4 import BeautifulSoup
import os

basisPfad = os.environ.get("userprofile")
basisPfad = os.path.join(basisPfad, "documents")
basisPfad = os.path.join(basisPfad, "SWR1-Playlist")

class PlaylistTitel:

    def __init__(self, Titel,Interpret,Zeitpunkt):
        self.Titel = Titel
        self.Interpret = Interpret
        self.Zeitpunkt = Zeitpunkt

titelGespielt = []
anzahlTitel = 0

for datei in os.listdir(basisPfad):
    htmlPfad = os.path.join(basisPfad, datei)
    with open(htmlPfad, encoding="Utf-8") as fh:
        htmlContent = fh.read()
        soup = BeautifulSoup(htmlContent, "html.parser")
        for dl in soup.find_all('dl'):
            # Liefert den Titel, aber noch zu ungenau
            ddElemente = dl.find_all("dd")
            if not ddElemente == None and len(ddElemente) > 1:
                titel =  ddElemente[0].text
                interpret = ddElemente[1].text
                zeitpunkt = 0
                titelGespielt.append(PlaylistTitel(titel, interpret, zeitpunkt))
                print(f"Titel: {titel} Interpret: {interpret}")
                anzahlTitel += 1


print("%d Titel erfasst" % anzahlTitel)

