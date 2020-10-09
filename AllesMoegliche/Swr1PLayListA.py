# Auswerten der SWR1-Playlist für einen Monat - Teil 1
import requests
import os

# Monat und Uhrzeit sind Teil der URL, also sollte sich die ganze Liste für einen Monat komplet laden lassen
# https://www.swr.de/swr1/bw/playlist/Die-Musikrecherche-in-der-SWR1-Playlist,musikrecherche-swr1-bw-100.html?time=00%3A00&date=2019-12-02

basisUrl = "https://www.swr.de/swr1/bw/playlist/Die-Musikrecherche-in-der-SWR1-Playlist,musikrecherche-swr1-bw-100.html?"

anzahlTage = 8
jahr = 2019
monat = 12
anzahlDateien = 0

for tag in range(1, anzahlTage):
    for std in range(0,23):
        query = f"time={std}%3A00&date={jahr}-{monat:02}-{tag:02}"
        url = basisUrl + query
        # response = requests.get(url)
        htmlPfad = os.environ.get("userprofile")
        htmlPfad = os.path.join(htmlPfad, "documents")
        htmlPfad = os.path.join(htmlPfad, "SWR1-Playlist")
        if not os.path.exists(htmlPfad):
            os.makedirs(htmlPfad)
        htmlPfad = os.path.join(htmlPfad, f"SWR1Playlist_{std:02}_{tag:02}{monat:02}{jahr}.html")
        webResponse = requests.get(url)
        with open(htmlPfad, "wb") as fh:
            fh.write(webResponse.content)
        anzahlDateien += 1
        print(f"Datei {anzahlDateien:000} - {htmlPfad} mit {os.path.getsize(htmlPfad)} Bytes geschrieben.")
        anzahlDateien += 1
        # open('c:/users/LikeGeeks/downloads/PythonImage.png', 'wb').write(myfile.content)


