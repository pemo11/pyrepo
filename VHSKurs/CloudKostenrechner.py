# Übung: Provider oder Cloud-Angebote vergleichen
# Übung für den ersten Abend, die erste Einheit
# Alles noch etwas unbeholfen, aber so fangen die ersten Schritte mit der Programmierung an
# Am Beispiel einer VM, die ein Jahr betrieben werden soll
# Provider - preiswertes VM
# Cloud - 2 Kerne, 2 GiB, Standort Frankfurt

# Kosten pro Monat
ProviderKosten1 = 9.9  # Host Europe
ProviderKosten2 = 5.6  # Microsoft Azure A1, 1 CPU, 2 GiB RAM,10 GB Temp Speicher

# Kosten pro Stunde in USD
CloudKostenAWS1 = 0.012 # 1 GIB
CloudKostenAWS2 = 0.024 # 2 GIB
CloudKostenAz1 = 0.005 # 2 GIB Preis in EUR

USDKurs = 1.14

# Was ist für ganzes Jahr günstiger?

PreisProvider1 = ProviderKosten1 * 12
PreisProvider2 = ProviderKosten2 * 12

PreisCloud1 = CloudKostenAWS1 * 24 * 365 * USDKurs
PreisCloud2 = CloudKostenAWS2 * 24 * 365 * USDKurs
PreisCloud3 = CloudKostenAz1 * 24 * 365

print("Ein Jahr Provider1 kostet %.2f€" % PreisProvider1)
print("Ein Jahr Provider2 kostet %.2f€" % PreisProvider2)
print("Ein Jahr Cloud-Hosting bei AWS mit 1G GiB kostet %.2f€" % PreisCloud1)
print("Ein Jahr Cloud-Hosting bei AWS mit 2G GiB kostet %.2f€" % PreisCloud2)
print("Ein Jahr Cloud-Hosting bei Azure mit 2G GiB kostet %.2f€" % PreisCloud3)
