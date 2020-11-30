# Berechnen der y-Werte nach der Kreisgleichung, für den 2. Oktanden
# Formel aus Fellner Buch Seite 93, Ergebnisse scheinen nicht ganz zu stimmen
# Erstellt: 17/10/20
import math
r  = 10
x = 0
xEnde = 10

while x<xEnde-1:
    x+=1
    y = round(math.sqrt(r*r - (x+1)*(x+1)),1)
    # y = r*r - (x+1)*(x+1)
    print(x, y)
