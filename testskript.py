import time
import RPi.GPIO as GPIO
# Zählweise der Pins festlegen
GPIO.setmode(GPIO.BOARD)
# Pin 22 (GPIO 25) als Ausgang festlegen
GPIO.setup(22, GPIO.OUT)
# Ausgang 3 mal ein-/ausschalten

while True:
    
    x = GPIO.input(22) == GPIO.HIGH:
    print(x)
    # eine Sekunden warten
    time.sleep(0.5)

# Ausgänge wieder freigeben
GPIO.cleanup()