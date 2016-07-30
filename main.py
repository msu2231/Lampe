import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

curState = 0            # 0: deactivated; 1: activated

GPIO.setup(11, GPIO.input)  # switch

GPIO.setup(10, GPIO.output) # LED

while 1:
    if GPIO.input(11) ==GPIO.HIGH:
        GPIO.output(10,GPIO.HIGH)
    else:
        GPIO.output(10,GPIO.LOW)
    
