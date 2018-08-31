import RPi.GPIO as GPIO

ledPin = 11
switchPin = 12

ledIsOn = False

def setup():
	print("Program is starting...\n")
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.output(ledPin, GPIO.LOW)
	print("Setup completed successfully")

def loop():
	global ledIsOn
	while True:
		if GPIO.input(switchPin) == GPIO.LOW:
			GPIO.output(ledPin, GPIO.HIGH)
			if not ledIsOn:
				print("LED on...")
				ledIsOn = True
		else:
			GPIO.output(ledPin, GPIO.LOW)
			if ledIsOn:
				print("LED off...")
				ledIsOn = False

def destroy():
	GPIO.output(ledPin, GPIO.LOW)
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()