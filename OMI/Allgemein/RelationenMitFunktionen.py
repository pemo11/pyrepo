# Eigenschaften von Relationen
# Hilfsprogramm für Relationen und Funktionen, OMI SS19

# Das Kartesische Produkt bilden mit List Comprehenions
# Genial!!! Auch das habe ich fast ohne "Spiken" hinschreiben können
# Es müssten 24 sein und sind es auch!
def KartProdukt(m1, m2):
    kp = [(x,y) for x in m1 for y in m2 ]
    return kp

# Prüfen auf linkstotal
# Wirklich elegant diese Syntax, die ich fast ohne Internet-Recherche runter geschrieben hatte
def IstLinkstotal(f, m1, m2):
    okFlag = True
    for z in m1:
        if f(z) not in m2:
            okFlag = False
    return okFlag

# Prüfen auf Rechtstotal
def IstRechtstotal(f, m1, m2):
    okFlag = True
    for z in m2:
        if f1(z) not in m1:
           okFlag = False
    return okFlag

# Prüfen auf Linkseindeutig
def IstLinkseindeutig(f, m1, m2):
    # Prüfen auf linkseindeutig
    okFlag = True
    numDic = {}
    for z in m1:
        if f(z) in m2:
            if numDic.get(f(z)) == None:
               numDic[f(z)] = 1
            else:
               numDic[f(z)] += 1

    for k in numDic.keys():
        if numDic[k] > 1:
           okFlag = False
    return okFlag

# Prüfen auf Rechtseindeutig
def IstRechtseindeutig(f, m1, m2):
    # Prüfen auf rechtseindeutig
    okFlag = True
    numDic = {}
    for z in m2:
        if f(z) in m1:
            if numDic.get(f(z)) == None:
               numDic[f(z)] = 1
            else:
               numDic[f(z)] += 1

    for k in numDic.keys():
        if numDic[k] > 1:
           okFlag = False
    return okFlag

def IstFunktion(f, m1, m2):
        okFlag = True
        okFlag = okFlag and IstLinkstotal(f1, m1, m2)
        okFlag = okFlag and IstRechtseindeutig(f, m1, m2)
        return okFlag

def IstInjektiv(f, m1, m2):
        okFlag = True
        okFlag = okFlag and IstFunktion(f1, m1, m2)
        okFlag = okFlag and IstLinkseindeutig(f, m1, m2)
        return okFlag

def IstSurjektiv(f, m1, m2):
        okFlag = True
        okFlag = okFlag and IstFunktion(f1, m1, m2)
        okFlag = okFlag and IstRechtstotal(f, m1, m2)
        return okFlag

def IstBijektiv(f, m1, m2):
        okFlag = True
        okFlag = okFlag and IstInjektiv(f1, m1, m2)
        okFlag = okFlag and IstSurjektiv(f, m1, m2)
        return okFlag

# Für die Linksprüfung
def f(x):
    return x * 2

# Die Umkehrfunktion für die Rechtsprüfung
def f1(x):
    return x // 2

# ===============================================
# Hier geht es los
# ===============================================
m1 = [2,4,5,6,8,10,2]
m2 = [4,8,12,16]

ergebnis = KartProdukt(m1,m2)
print(ergebnis)
print("%d Tupel bilden das kartesische Produkt" % len(ergebnis))

# 1) Prüfen auf Linkstotal
ergebnis = IstLinkstotal(f, m1, m2)
ausgabe = "Die Relation ist" + ("" if ergebnis == True else " nicht") + " linktstotal"
print(ausgabe)

# 2) Prüfen auf Rechtstotal
ergebnis = IstRechtstotal(f1, m1, m2)
ausgabe = "Die Relation ist" + ("" if ergebnis == True else " nicht") + " rechtstotal"
print(ausgabe)

# 3) Prüfen auf Linkseindeutig
ergebnis = IstLinkseindeutig(f, m1, m2)
ausgabe = "Die Relation ist" + ("" if ergebnis == True else " nicht") + " linkseindeutig"
print(ausgabe)

# 4) Prüfen auf Rechtseindeutig
ergebnis = IstRechtseindeutig(f1, m1, m2)
ausgabe = "Die Relation ist" +  ("" if ergebnis == True else " nicht") + " rechtseindeutig"
print(ausgabe)

# 5) Prüfen auf Funktion
ergebnis = IstFunktion(f1, m1, m2)
ausgabe = "Die Relation ist " +  ("eine" if ergebnis == True else "keine") + " Funktion"
print(ausgabe)

# 6) Prüfen auf injektiv
ergebnis = IstInjektiv(f1, m1, m2)
ausgabe = "Die Relation ist " +  ("eine" if ergebnis == True else "keine") + " injektive Funktion"
print(ausgabe)

# 7) Prüfen auf surjektiv
ergebnis = IstSurjektiv(f1, m1, m2)
ausgabe = "Die Relation ist " +  ("eine" if ergebnis == True else "keine") + " surjektive Funktion"
print(ausgabe)

# 8) Prüfen auf Bijektiv
ergebnis = IstBijektiv(f1, m1, m2)
ausgabe = "Die Relation ist " +  ("eine" if ergebnis == True else "keine") + " bijektive Funktion"
print(ausgabe)
