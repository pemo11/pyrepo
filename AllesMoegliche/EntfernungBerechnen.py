# Entfernung zwischen zwei Punkten (sehr kompliziert)
# Quelle: https://www.dbwiki.net/wiki/VBA_Tipp:_Distanz_Luftlinie_berechnen
import math

class cord:
    
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

DMINUS = 45

sin2f = 0
cos2f = 0
sin2g = 0
cos2g = 0
sin2lam = 0
cos2lam = 0

# Diese def soll die anderen provisorischen defs ersetzen!
def sincos2(w, x, y):
    x = math.sin(w)
    y = math.cos(w)
    return (x,y)

def sincos2f(x):
    global sin2f, cos2f
    s = math.sin(x)
    c = math.cos(x)
    sin2f = s * s
    cos2f = c * c

def sincos2g(x):
    global sin2g, cos2g
    s = math.sin(x)
    c = math.cos(x)
    sin2g = s * s
    cos2g = c * c

def sincos2lam(x):
    global sin2lam, cos2lam
    s = math.sin(x)
    c = math.cos(x)
    sin2lam = s * s
    cos2lam = c * c

def getDistance(c1, c2):
    dr2 = math.pi / 1000                        # Umrechnungsfaktor
    er = 6378.14                                # Elipsoid-Typ EARTH76 
    fl = 1 / 298.257                            # 1 soll Long Int sein
    f = (c1.lat + c2.lat) / 2
    g = (c1.lat - c2.lat) / 2
    lam = (c1.lon - c2.lon) / 2                 # Im VBA-Code heißt die Variable lambda
    sincos2f(f * dr2)
    sincos2g(g * dr2)
    sincos2lam(lam * dr2)

    s = sin2g * cos2lam + cos2f * sin2lam
    c = cos2g * cos2lam + sin2f * sin2lam

    omega = math.atan(math.sqrt(c/2))

    d = 2 * omega * er
    t = math.sqrt(s * c) / omega

    h1 = (3 * t - 1) / (2 * c)
    h2 = (3 * t + 1) / (2 * s)

    return d * (1 + fl * (h1 * sin2f + cos2g - h2 * cos2f * sin2g))

Berlin = cord(52, 13)
Tokio = cord(35, 139)

print(getDistance(Berlin, Tokio))