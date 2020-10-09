# An- und Verkauf von Divisen
# Verkaufkurs immer höher als Ankaufkurs
# Provision von 2.5% + "Handling fee" bis 1000€ 3€ > 5€
# Erstellt 02/08/20
# Endloswiederholung, die per Q verlassen wird
# Soll Übungsaufgabe im VHS-Kurs bzw. in einem Python-Übungsbuch sein

USDVerkauf = float(1.25)
USDAnkauf = float(1.21)
ProvisionKlein = 3
ProvisionGross = 5

def AuswahlMenue():
    print("1) US$ ankaufen")
    print("12 US$ verkaufen")
    print("Q) Ende")
    antwort = input("")
    return int(antwort[0])

while True:
    antwort = AuswahlMenue()
    if antwort == 1:
        USBetrag = float(input("Gewünschter Betrag in USD?"))
        EURBetrag = USBetrag * USDVerkauf
        EURBetrag += EURBetrag / 100 * 2.5
        EURBetrag += ProvisionGross if USBetrag > 1000 else ProvisionKlein
        print(f"{USBetrag:.2f}$ kosten {EURBetrag:.2f}€")
        antwort = input("Weiterer An- oder Verkauf? (J/N)")
        if antwort != "J":
            break
    elif antwort == 2:
        USBetrag = float(input("Zu verkaufender Betrag in USD?"))
        EURBetrag = USBetrag * USDAnkauf
        EURBetrag -= EURBetrag / 100 * 2.5
        EURBetrag += ProvisionGross if USBetrag > 1000 else ProvisionKlein
        print(f"Für {USBetrag:.2f}$ erhalten Sie {EURBetrag:.2f}€")
        antwort = input("Weiterer An- oder Verkauf? (J/N)")
        if antwort != "J":
            break
    else:
        break