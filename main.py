import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

RELAY_OUTPUT = 10
SWITCH_INPUT = 11

curState = 0            # 0: deactivated; 1: activated
switchActivated = 0     # 0: deactivated; 1: activated
wifiActivated = 0       # 0: light deactivated via Wifi; 1: light activated via Wifi
stateChanged = 0        # 0: false; 1: true

GPIO.setup(SWITCH_INPUT, GPIO.input)  # switch

GPIO.setup(RELAY_OUTPUT, GPIO.output) # LED

while 1:
    lightStateFile = ("/var/www/light.txt", "r")

    lightStateFromFile = lightStateFile.read()

    if GPIO.input(SWITCH_INPUT) == GPIO.HIGH:
        if switchActivated = 0:
            stateChanged = 1

        switchActivated = 1
    else:
        if switchActivated = 1:
            stateChanged = 1

        switchActivated = 0

    if lightStateFromFile == 1:
        if wifiActivated = 0:
            stateChanged = 1

        wifiActivated = 1
    else:
        if wifiActivated = 1:
            stateChanged = 1

        wifiActivated = 0

    if stateChanged == 1:
        stateChanged = 0

        if curState == 1:
            GPIO.output (RELAY_OUTPUT, GPIO.LOW)
            curState = 0
        else:
            GPIO.output (RELAY_OUTPUT, GPIO.HIGH)
            curState = 1

    lightStateFile.close()
    time.sleep(.25)
