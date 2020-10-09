# Abrufen der aktuellen Corona-Zahlen von der amtlichen Webseite
# Mit BeautifulSoup
# Erstellt: 13/09/20

# https://www.geeksforgeeks.org/corona-virus-live-updates-for-india-using-python/?ref=leftbar-rightbar

from bs4 import BeautifulSoup

# RKI-Zahlen für ganz Deutschland
url = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html"
