#!/usr/bin/python3
import pigpio
import time
from gpiozero import Button

# Servo parameter
servo = 12
pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_PWM_frequency( servo, 50 )

# Button parameter
button = Button(18, bounce_time=1)

# state
state = -1 #-1 for stop, and 1 for move the servo

while True:
    if button.is_pressed: 
        state = state * -1 #change the state 
        print("button pressed, change servo state")
        time.sleep(1)
    
    if state == 1: 
        pwm.set_PWM_dutycycle( servo,15)
    elif state == -1: 
        pwm.set_PWM_dutycycle( servo,0)
