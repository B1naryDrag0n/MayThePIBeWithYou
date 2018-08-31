import RPi.GPIO as GPIO
import time
import readchar

ledPin = 11 # RPI GPIO17 pin

ledOn = "o"
ledOff = "i"
ledBlinkLowSpeed = "1"
ledBlinkMediumSpeed = "2"
ledBlinkHighSpeed = "3"
ledBlinkUltraSpeed = "4"
exitApp = "e"

lowSpeed = 1
mediumSpeed = 0.5
highSpeed = 0.2
ultraSpeed = 0.05

ledIsOn = False

def show_ui():
	print("      *** SETUP COMPLETE ***")
	print("       ********************\n")
	print("=#=#=#=#  KEY  BINDINGS  #=#=#=#=#=")
	print("|                                 |")
	print("| Press o : Turn LED on           |")
	print("|       i : Turn LED off          |")
	print("|                                 |")
	print("|       1 : Low Speed Blink       |")
	print("|       2 : Medium Speed Blink    |")
	print("|       3 : High Speed Blink      |")
	print("|       4 : Ultra Speed Blink     |")
	print("|                                 |")
	print("|       e : Exit App              |")
	print("|                                 |")
	print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=\n")

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, GPIO.LOW)
	show_ui()

def turn_on_LED():
	GPIO.output(ledPin, GPIO.HIGH)
	global ledIsOn
	if not ledIsOn:
		ledIsOn = True
		print("LED ON")

def turn_off_LED():
	GPIO.output(ledPin, GPIO.LOW)
	global ledIsOn
	if ledIsOn:
		ledIsOn = False
		print("LED OFF")

def blink_LED(speed):
	print("!!! BLINK BLINK !!!")
	x = 0
	while x < 10:
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(speed)
		GPIO.output(ledPin, GPIO.LOW)
		time.sleep(speed)
		x += 1
	if ledIsOn:
		GPIO.output(ledPin, GPIO.HIGH)
	else:
		GPIO.output(ledPin, GPIO.LOW)

def loop():
	while True:
		pressedKey = readchar.readchar()
		if pressedKey == ledOn:
			turn_on_LED()
		elif pressedKey == ledOff:
			turn_off_LED()
		elif pressedKey == ledBlinkLowSpeed:
			blink_LED(lowSpeed)
		elif pressedKey == ledBlinkMediumSpeed:
			blink_LED(mediumSpeed)
		elif pressedKey == ledBlinkHighSpeed:
			blink_LED(highSpeed)
		elif pressedKey == ledBlinkUltraSpeed:
			blink_LED(ultraSpeed)
		elif pressedKey == exitApp:
			destroy()
			break

def destroy():
	GPIO.output(ledPin, GPIO.LOW)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	loop()