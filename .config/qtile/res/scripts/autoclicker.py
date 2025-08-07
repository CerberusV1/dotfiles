import time
import subprocess
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController, Button


keyboard = KeyboardController()
mouse = MouseController()

# Intervall für Rechtsklick in Sekunden
rechtsklick_intervall = 0.01


def shift_spam_mit_rechtsklick():
    letzter_klick = time.time()
    try:
        while True:
            # Shift drücken und loslassen
            # keyboard.press(Key.shift)
            # time.sleep(0.05)
            # keyboard.release(Key.shift)

            # Kurze Pause zwischen den Shift-Spams
            # time.sleep(0.1)

            # Zeit für Rechtsklick?
            jetzt = time.time()
            if jetzt - letzter_klick >= rechtsklick_intervall:
                mouse.click(Button.left)
                letzter_klick = jetzt

    except KeyboardInterrupt:
        print("Skript beendet.")


if __name__ == "__main__":
    shift_spam_mit_rechtsklick()
