# Eine einfache Ausgabenstatistik
# Jedes Tupel enthält Betrag und eine Zahl, die die Wichtigkeit der Ausgabe angibt
# 1 - für Lebensnotwendig, 2 - Wichtig, 3 - Verzichtbar

import pandas as pd
import matplotlib.pyplot as plt

ausgaben =  [('Kino',10,3), ('Telefon',20,1), ('Socken',8,2),('Comic-Heft',3.95,2)]

ausgabenDic = {}

for ausgabe in ausgaben:
    if not ausgabenDic.get(ausgabe[2]):
        ausgabenDic[ausgabe[2]] = list()
        ausgabenDic[ausgabe[2]].append(((ausgabe[0],ausgabe[1])))
    else:
        ausgabenDic[ausgabe[2]].append(((ausgabe[0],ausgabe[1])))

print(ausgabenDic)

kategorien = {1:"Notwendig",2:"Optional",3:"Luxus"}

# Jetzt fehlt noch die Ausgabe über pylot
# Das war bereits eine etwas härtere Nuss für mich;)
# Für den Anfängerkurs ist eine for-Schleife die bessere Alternative, so pythonisch muss es nicht sein
ausgabenBetraege = [sum(b) for b in [[t1[1] for t1 in t] for t in list(ausgabenDic.values())]]
plt.bar(range(len(ausgabenBetraege)), ausgabenBetraege, align='center')

# plt.xticks(range(len(ausgaben)), list(ausgabenDic.keys()))
plt.xticks(range(len(ausgaben)), [kategorien[k] for k in ausgabenDic.keys()])
# Namen statt Zahlen
plt.show()