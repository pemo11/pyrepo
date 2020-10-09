# Base64-Kodierung und Dekodierung
# Vollständige Übersicht https://docs.python.org/3/library/codecs.html#standard-encodings
import base64
import os

# Ein PowerShell-Befehl als Beispiel
s = "Get-Process | Where-Object WS -gt 100MB"
s = "Get-Process | Where-Object WS -gt 100MB | Sort-Object WS | Select-Object Name,WS,StartTime"

# Soetwas ginge auch;)
s1 ="記者 鄭啟源 羅智堅"

# "utf-8" ist default - soll Unicode sein

# Wichtig: Es funktioniert nur mit utf_16_le???
bString = s.encode("utf_16_le")

b64 = base64.b64encode(bString)

s64 = b64.decode("utf-8")
print(s64)

# Jetzt PowerShell mit der Befehlsfolge ausführen
poshArgs = "-noprofile -encodedCommand " + s64
print(poshArgs)
os.system("powershell " + poshArgs)