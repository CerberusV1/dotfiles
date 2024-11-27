import time
from pynput.mouse import Button, Controller

mouse = Controller()

try:
    while True:
        mouse.click(Button.left, 2)  # Simulates left-click
        time.sleep(0.1)              # Adjust the interval
except KeyboardInterrupt:
    print("Autoclicker stopped.")
