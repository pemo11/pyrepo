# Regelbasierte Prüfung darauf wie sicher ein Passwort ist
# Ein weiteres Beispiel für flexible Python-Programmierung
# Erstellt: 04/07/20

def Mindestlaenge(Passwort):
    maxScore = 2
    return (maxScore if len(Passwort) >= 8 else 0, maxScore)

def SonderzeichenEnthalten(Passwort):
    maxScore = 4
    return (maxScore if len([c for c in Passwort if c in ("?","!","@")]) > 0 else 0, maxScore)

def BeginntMitGroßbuchstabe(Passwort):
    maxScore = 1
    return (maxScore if Passwort[0] == Passwort[0].upper() else 0, maxScore)

regeln = [Mindestlaenge, SonderzeichenEnthalten,BeginntMitGroßbuchstabe]
score = 0
maxScore = 0

passwort = "HalloWelt123"

for regel in regeln:
    # score, maxScore += regel(passwort) geht leider nicht
    s1,s2 = regel(passwort)
    score += s1
    maxScore += s2
    

print("Das Kennwort %s hat einen Score %d von %d" % (passwort, score, maxScore))