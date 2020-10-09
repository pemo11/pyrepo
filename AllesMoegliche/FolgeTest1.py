# Feststellen, ob keine Liste eine Folge von Zahlen enthält
# Erstellt: 26/09/20

# Geht eventuell noch etwas kürzer
def IstFolge(l):
    okFlag = True
    z1 = l[0]
    for z in l[1:]:
        okFlag = okFlag and abs(z - z1) == 1
        z1 = z
    return okFlag

l1 = [1,2,3,4,5]
print(IstFolge(l1))

l2 = [1,2,3,5]
print(IstFolge(l2))

l3 = [31,30,29,28]
print(IstFolge(l3))