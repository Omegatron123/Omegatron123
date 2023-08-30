# Here is the configuration:
# Connect your button NO pin to GPIO 18 (pin 12)
# Connect your button COM pin to GND

from gpiozero import Button
import time

button2 = Button(18, bounce_time=1)

while True: 
    if button1.is_pressed: 
        print("button is pressed")
        time.sleep(1)
