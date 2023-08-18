# Here is the configuration:
# Button:
# Connect your button NO pin to GPIO 18 (pin 12)
# Connect your button COM pin to GND
# Servo: 
# Connect the servo voltage pin to Rpi 5v
# Connect the servo GND pin to Rpi GND
# Connect the servo signal pin to GPIO17 (pin 11)

from gpiozero import Button
import RPi.GPIO as GPIO
import time

# button configuration
button = Button(18, bounce_time=1)

# servo configuration
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.ChangeDutyCycle(5)

# door state
# 1st test, on/off servo only
# the rule is, -1 for stop, and 1 for move
# initially we set the servo to stop moving
door_state = -1 

while True: 
    # check whether the button is pressed
    if button.is_pressed: 
        door_state = door_state * -1
        print("button pressed, door state is:" + str(door_state))
        time.sleep(1) #enough delay which act as debouncer
    
    if door_state == 1: #slowly move the servo
        p.start(6.7)
    else: #stop the servo
        p.start(7) 
