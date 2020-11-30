# Berechnung der Dämpfung
# Formel: DdB = -20 log (Uout/Uin) = 20 log (Uin/Uout)
import math

# Bestimme für den Verstärkungsfaktor Vu = 0.5 das Verstärkungs- und Dämpfungsmaß in dB

uOut = 4
uIn = 2

vDb = 20 * math.log10(uOut/uIn)
dDb = 20 * math.log10(uIn/uOut)
print("Verstärkung = %.f Dämpfung = %.f" % (vDb, dDb))

# Am Anfang der Leitung liegt ein Testsignal von Utest = 1V. Am Leitungsende wird U0 = 0.707 gemessen.
# Welche Verstärkung muss eingestellt werden?

uIn = 1
uOut = 0.707
dDb = 20 * math.log10(uIn/uOut)
print("Die Verstärkung muss auf %.f dDb eingestellt werden" % dDb)


