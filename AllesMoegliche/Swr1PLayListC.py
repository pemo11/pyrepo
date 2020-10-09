# Auswerten einer einzelnen SWR1-Playlist-Datei
# Funktioniert !

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
datei = "SWR1Playlist_01_01122019.html"
htmlPfad = os.path.join(basisPfad, datei)

with open(htmlPfad, encoding="Utf-8") as fh:
    htmlContent = fh.read()
    soup = BeautifulSoup(htmlContent, "html.parser")

for plItem in soup.find_all("div",  class_="list-playlist-item"):
    zeitpunkt = plItem.find_next("time")["datetime"]
    titel = plItem.find_next("dl").find_next("dt", text="Titel").find_next("dd").string
    interpret = plItem.find_next("dl").find_next("dt", text="Interpret").find_next("dd").string
    if titel != None and interpret != None:
        titelGespielt.append(PlaylistTitel(titel, interpret, zeitpunkt))

print(titelGespielt)