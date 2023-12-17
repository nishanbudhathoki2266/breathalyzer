import RPi.GPIO as GPIO
import time

ledPin = 17
digitalPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(digitalPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)


alcoholLevel = GPIO.input(digitalPin)

if alcoholLevel == 1:
        # Sober
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        # Drunk
        for _ in range(5):  # Blink 5 times
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.5)