# Übung Nr. 1 - Ein- und Ausschalten eines PINs
# Gute Referenz: https://blog.withcode.uk/wp-content/uploads/2016/10/RPi_GPIO_python_quickstart_guide.pdf

# Module importieren
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

def getStatus(Pin):
  output = GPIO
# GPIO Nr. 3 auf Out setzen
GPIO.setup(3, GPIO.OUT)

# GPIO Nr. 3 einschalten
GPIO.output(3, GPIO.HIGH)

# Kurz warten
sleep(3)

# GPIO Nr. 3 wieder ausschalten
GPIO.output(3, GPIO.LOW)

