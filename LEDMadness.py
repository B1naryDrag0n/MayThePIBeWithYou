import RPi.GPIO as GPIO
import time
import readchar

ledPin = 11 # RPI GPIO17 pin

ledOn = "o"
ledOff = "i"
ledBlink = "b"
exitApp = "e"

ledIsOn = False

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, GPIO.LOW)
	print("SETUP COMPLETE")

def turn_on_LED():
	GPIO.output(ledPin, GPIO.HIGH)

def turn_off_LED():
	GPIO.output(ledPin, GPIO.LOW)

def blink_LED():
	print("!!! BLINK BLINK !!!")
	x = 0
	while x < 25:
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(0.05)
		GPIO.output(ledPin, GPIO.LOW)
		time.sleep(0.05)
		x += 1

def loop():
	while True:
		pressedKey = readchar.readchar()
		if pressedKey == ledOn:
			turn_on_LED()
		elif pressedKey == ledOff:
			turn_off_LED()
		elif pressedKey == ledBlink:
			blink_LED()
		elif pressedKey == exitApp:
			destroy()
			break

def destroy():
	GPIO.output(ledPin, GPIO.LOW)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	loop()