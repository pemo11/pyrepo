# Ausgabe aller Zahlenfolge einer Liste
# Eine etwas anspruchsvollere Aufgabe für den VHS-Kurs bzw. meine codekiste-Webseite
# Erstellt: 26/09/20

def HoleFolge(l,MinLaenge=3):
    z1 = l[0]
    folge = []
    folgeListe = []
    ersteZahl = True
    for z in l[1:]:
        if abs(z-z1) == 1:
            # Nur einmal hinzufügen (nicht sehr elegant)
            if ersteZahl:
                folge.append(z1)
                ersteZahl = False
            folge.append(z)
        else:
            if len(folge) >= MinLaenge:
                folgeListe.append(folge)
            folge = []
            ersteZahl = True
        z1 = z
    if len(folge) >= MinLaenge:
        folgeListe.append(folge)
    return folgeListe

l1 = [1,3,5,6,7,8,10,11]
print(HoleFolge(l1))

l2 = [1,3,4,5,7,8,10,11,12]
print(HoleFolge(l2))
