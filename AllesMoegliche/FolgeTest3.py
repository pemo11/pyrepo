# Feststellen, ob eine Liste aus identischen Elementen besteht
# Erstellt: 27/09/20

def AlleGleich1(l):
    # Jedes Element, mit jedem anderen per List Comprehension vergleichen
    alleGleich = True
    for z in l:
        alleGleich = alleGleich and (True if [z1 for z1 in l if z1 != z] == [] else False)
    return alleGleich

def AlleGleich2(l):
    # Jedes Element, mit jedem anderen vergleichen
    alleGleich = True
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            alleGleich = alleGleich and (l[i] == l[j])
    return alleGleich

def AlleGleich3(l):
    # Jedes Element als Objekt mit dem Attribut Farbe vergleichen
    alleGleich = True
    for z in l:
        alleGleich = alleGleich and (True if [z1 for z1 in l if z1.Farbe != z.Farbe] == [] else False)
    return alleGleich

l1 = [11,11,22,11,11,11]
print(AlleGleich1(l1))

l2 = [11,11,11,11,11,11]
print(AlleGleich1(l2))

l1 = [11,11,22,11,11,11]
print(AlleGleich2(l1))

l2 = [11,11,11,11,11,11]
print(AlleGleich2(l2))

class Element():

    def __init__(self,Farbe):
        self.Farbe = Farbe

l3 = [Element("Rot"),Element("Rot"),Element("Gelb"),Element("Rot")]
print(AlleGleich3(l3))

l4 = [Element("Rot"),Element("Rot"),Element("Rot"),Element("Rot")]
print(AlleGleich3(l4))

