import time
from pynput.mouse import Button, Controller

mouse = Controller()

try:
    while True:
        mouse.click(Button.left, 1)  # Simulates left-click
        time.sleep(1.0)              # Adjust the interval
except KeyboardInterrupt:
    print("Autoclicker stopped.")
