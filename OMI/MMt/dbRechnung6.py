# Serienschaltung von Verstärkern
import math

def Verstaerkung(PIn, POut):
    return 20 * math.log10(POut/PIn)

P1 = (0.5,2)
P2 = (2, 3.5)

for p in (P1,P2):
    v = Verstaerkung(p[0],p[1])
    print("Die Verstärkung beträgt %.f" % v)
