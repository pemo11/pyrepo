# Passwort einer Zip-Datei knacken über eine klassische Wörterbuch-Attacke
import os
import zipfile
from tqdm import tqdm

pyPfad = os.path.dirname(__file__)
txtDocpfad = os.path.join(pyPfad, "rockyou.txt")

zipPfad = os.path.join(pyPfad, "OMI.zip")

zipFile = zipfile.ZipFile(zipPfad)

wordCount = len(list(open(txtDocpfad, "rb")))

print(f"Anzahl Wörter: {wordCount}")

with open(txtDocpfad, "rb") as wortListe:
    for wort in tqdm(wortListe,total=wordCount,unit="word"):
        try:
            zipFile.extractall(pwd=wort.strip())
        except:
            continue
        else:
            print("*** Zip-Datei wurde geknackt !!! ***")
            exit(0)

print("*** Zip-Datei leider nicht geknackt, keine Chance, ich gebe auf!!!")

