# Beispiel für Html Scraping mit BeautifulSoup4
# https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bildung-Forschung-Kultur/Bildungsstand/Tabellen/bildungsabschluss.html

from bs4 import BeautifulSoup
import requests

url = "https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bildung-Forschung-Kultur/Bildungsstand/Tabellen/bildungsabschluss.html"

htmlText = requests.get(url) # , verify=False führt zu einer Warnung, wird aber ausgeführt

# Angabe eines Parsers ist optional, aber empfehlenswert
soup = BeautifulSoup(htmlText.content, "html.parser")

# print(soup)

# Erste Tabelle selektieren
tMain = soup.find("table")

jahre = []

# Jetzt die Felder der ersten Zeile durchgehen (so genial!)
for td in tMain.find("tr").find_all("th"):
    if td.text.isnumeric():
        jahre.append(int(td.text))

# Ginge natürlich über List Comprehension auch in einer Zeile
# jahre = [int(td.text) for td in tMain.find("tr").find_all("th") if td.text.isnumeric()]

# print(jahre)

# Dictionary anlegen für die Gesamtstatistik
statistik = dict()

# Alle Schlüssel-Spalten besitzen class="Vorspalte-ind2"

# Beispiel über eine VHS-Übung
def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

currentText = ""

# Jetzt noch einmal alle Zeilen durchgehen und alle Spalten
for tr in tMain.find_all("tr"):
    # Alle Spalten durchgehen 
    for td in tr.find_all("td"):
        #try:
        #    print(td['class'][0] == "Vorspalte-ind2")
        #except:
        #    print("Kein class-Attribut")
        if td.has_attr('class') and td['class'][0] == "Vorspalte-ind2":
            currentText = td.text
            statistik[currentText] = list()
        elif td.has_attr('class') and td['class'][0] == "Vorspalte-ind1":
            pass
        else:
            if currentText != "":
                numText = td.text
                if numText.endswith('.') or numText.endswith(','):
                    numText = numText[:-1]
                numText = numText.replace(',','.')
                if is_float(numText):
                    statistik[currentText].append(float(numText))
                else:
                    statistik[currentText].append(0)

print(statistik)

# Insgesamt funktioniert es - ein Problem gibt es mit der vorletzten Zeile, die auch die Zahlen der letzten Zeile enthält
# Lösung: Es dürfen nicht mehr Zahlen aufgenommen werden, als Jahre erfasst wurden
# Nette Idee: "Scrap-Wettbewerb" oder Hackatron im Rahmen des pyClubs

# Fehlermeldung fehlendes SSL-Modul lag daran, dass auch Anaconda installiert war
# so dass die Datei libssl-1_1-x64.dll nicht gefunden wurde, kann über die Path-Variable korrigiert werden
