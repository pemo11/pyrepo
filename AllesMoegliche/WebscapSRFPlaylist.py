# Auswerten der gespielten Titel eines Tages beim SRF

from bs4 import BeautifulSoup
import requests

url = "https://www.srf.ch/radio-srf-musikwelle/gespielte-musik"

htmlText = requests.get(url) # , verify=False führt zu einer Warnung, wird aber ausgeführt

# Angabe eines Parsers ist optional, aber empfehlenswert
soup = BeautifulSoup(htmlText.content, "html.parser")

# Die Titel sind offenabr nicht im Hmtl enthalten oder 
print(soup)

# Alternativ die SWR1-Playliste für den ganzen Monat in einem anderen Projekt
# Monat und Uhrzeit sind Teil der URL, also sollte sich die ganze Liste für einen Monat komplet laden lassen
# Das wäre ein nettes Projekt!
url = "https://www.swr.de/swr1/bw/playlist/Die-Musikrecherche-in-der-SWR1-Playlist,musikrecherche-swr1-bw-100.html?time=00%3A00&date=2019-12-02"


