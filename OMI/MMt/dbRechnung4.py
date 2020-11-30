# Berechnen der Verstärkung
import math

# Ein Mikrofonverstärker wird so eingestellt, dass er eine Eingangsspannung Uin = 20mV auf Uout=1V verstärkt.
# Bestime das Verstärkungsmaß in dB

uIn = 0.02
uOut = 1
VdB = 20 * math.log10(uOut/uIn)
print("Die Verstärkung beträgt %.f dB" % VdB)

# Das Verstärkungsmaß beträgt VdB = 54Db. Um welchen Verstärkungsfaktor V wird ein Signal verstärkt?

# Die obige Formel muss nach U1/U0 aufgelöst werden

VdB = 54

VF = math.pow(10, VdB / 20)
print("Der Verstärkungsfaktor beträgt %.f" % VF)
