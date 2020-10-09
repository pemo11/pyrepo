# Zählen wie wie Zahlen in einer Liste mehfach vorkommen
# Erstellt: 26/09/20

l = [1,2,3,1,2,4,4,4,1]

d = {}

for z in l:
    if d.get(z) == None:
        d[z] = 1
    else:
        d[z] += 1

print(d)

# Eventuell etwas eleganter und pythonischer
d = {}
for z in l:
    d[z] = 1 if d.get(z) == None else d[z] + 1
print(d)


# Mit Lambdas geht es leider nicht, da ein Lambda nur einen Ausdruck bilden und keine Zuweisung durchführen kann
