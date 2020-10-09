# Übungsaufgabe VHS-Kurs
# Erstellt: 03/09/20

import getpass
import os
import hashlib
import datetime

userliste = {"Admin":"!@pqxabc","Adam":"demo+123","Bernd":"Hallo1234","Chris":"passwort","Dieter":"Spidermann"}

user = input("Benutzer?")
# Ist eine verdeckte Eingabe möglich?
# Pw = input("Passwort?")
pw = getpass.getpass("Passwort?")

# Schritt 1: Ist der Benutzer authentiziert?
if userliste.get(user) != None:
    if userliste[user] == pw:
        print("*** User ist authentifiziert ***")
        success = True
    else:
        print("!!! Das Passwort stimmt nicht !!!")
        success = False
else:
    print("!!! Unbekannter Benutzername !!!")
    success = False

# Schritt 2: Loggen des Anmeldeversuches
logPfad = os.path.join(os.path.dirname(__file__), "pylogin.log")

# w für write und t für text - t kann aber weggelassen werden, da es immer der Default ist
with open(logPfad, mode="a", encoding="Utf-8") as fh:
    uhrzeit = datetime.datetime.today().strftime("%H:%M")
    if success:
        logMsg = f"{uhrzeit}: *** Erfolgreiche Anmeldung von {user} ***"
    else:
        logMsg = f"{uhrzeit}: !!! Nicht erfolgreiche Anmeldung von {user} !!!"
    fh.write(logMsg + "\n")

# Schritt 3: Bei Anmeldung als Admin - Ausgabe der Anmeldestatistik
if user.lower() == "admin" and success:
    with open(logPfad, mode="rt", encoding="Utf-8") as fh:
        # Geht erst ab Python 3.8 (:= ist der Wallroß-Operator - wallruss)
        # while (line := fh.readline()) != "":
        for line in fh:
            print(line)

# Schritt 4: Eingegebenes Kennwort wird in einen MD5-Hash umgewandelt und mit dem MD5-Hash der Userliste verglichen

# So viele Punkte in einem Befehl;)
md5Pw = hashlib.md5(pw.encode()).hexdigest()

print(f"*** Der Hashwert des Passworts als Hex-Zahl: {md5Pw} ***")