#! usr/bin/python3
# Erstellt: 22/01/21
# Wochenausgaben - Zusatzaufgabe Video1  - Berechnen von Abtastraten

def AbtastfrequenzBerechnen(rate):
    Q = 10
    fY = 2.97E9 / 4
    f = 0
    r1,r2,r3 = [int(z) for z in rate[::2]]
    Ay = fY * r1
    CR = fY * r2
    CB = fY * r3
    return (f"{Ay:.2E}",f"{CR:.2E}", f"{CB:.2E  }")


rate = "4:2:2"
print(AbtastfrequenzBerechnen(rate))