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

while True:
    command = int(input("command (0 for left, 1 for right):"))
    print(type(command))
    while command == 0:
        pwm.set_PWM_dutycycle( servo,15)
        if button.is_pressed: 
            pwm.set_PWM_dutycycle( servo,0)
            command = 3
            time.sleep(1)
    while command == 1:
        pwm.set_PWM_dutycycle( servo,30)
        if button.is_pressed: 
            pwm.set_PWM_dutycycle( servo,0)
            command = 3
            time.sleep(1)
