import RPi.GPIO as GPIO
import time

ledPin = 17
digitalPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(digitalPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

# Function to read alcohol level
def readAlcoholLevel():
    return GPIO.input(digitalPin)

# Function to control LED based on alcohol level
def controlLed(alcoholLevel):
    if alcoholLevel == 1:
        # Sober
        GPIO.output(led_pin, GPIO.HIGH)
    else:
        # Drunk
        for _ in range(5):  # Blink 5 times
            GPIO.output(led_pin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(led_pin, GPIO.LOW)
            time.sleep(0.5)

# Runing in loop - Main loop
try:
    while True:
        alcoholLevel = readAlcoholLevel()
        controlLed(alcoholLevel)
        time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    


