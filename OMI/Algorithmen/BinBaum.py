# Binärer Baum

# Wird die Baum-Klasse benötigt?
class Baum:
    def __init__(self, k):
        self.Knoten = k
    def Suche(self, v):
        pass

class Knoten:
    def __init__(self, name, v):
        self.name = name
        self.val = v
        self.left = None
        self.right = None

k7 = Knoten("K7", 70)
k7.left = 7
k7.right = 8

k6 = Knoten("K6", 60)
k6.left = 5
k6.right = 6

k5 = Knoten("K5", 50)
k5.left = 3
k5.right = 4

k4 = Knoten("K4", 40)
k5.left = 21
k5.right = 1

k3 = Knoten("K3", 30)
k3.left = k6
k3.right = k7

k2 = Knoten("K2", 20)
k2.left = k4
k2.right = k5

k1 = Knoten("K1",10)
k1.left = k2
k1.right = k3

# b1 = Baum(k1)

def BaumAusgabe(k):
    print(k.name + ":" + str(k.val))
    if type(k.left) is Knoten:
        BaumAusgabe(k.left)
    else:
        print(k.name + ":" + str(k.left))
    if type(k.right) is Knoten:
        BaumAusgabe(k.right)
    else:
        print(k.name + ":" + str(k.right))

Hoehe = 1

def BaumHoehe(k):
    global Hoehe
    print(f"Aktuelle Höhe: {Hoehe}")
    if type(k.left) is Knoten:
        BaumHoehe(k.left)
        Hoehe += 1
    if type(k.right) is Knoten:
        BaumHoehe(k.left)

# Hängt von der Tiefe des Baums ab
spaceCount = 2

def BaumAusgabe2(b):
    spaces = " " * spaceCount
    print(spaces + str(b.Knoten.val))
    spaces = " " * (spaceCount // 2)
    print(spaces + "/" + spaces + "\\")
    print(spaces + str(b.Knoten.left) + spaces + spaces + str(b.Knoten.right))

BaumAusgabe(k1)
BaumHoehe(k1)
print(f"Baumhöhe: {Hoehe}")