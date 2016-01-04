import RPi.GPIO as GPIO
import time
# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)
count = 0
while count < 2:
    GPIO.output(18,GPIO.HIGH)
    print("LED on")

    time.sleep(2)

    GPIO.output(18,GPIO.LOW)
    print("LED off")

    time.sleep(2)

    count = count + 1
else:
    print("Done")

