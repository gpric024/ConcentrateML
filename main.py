import time
import winsound
import ctypes
import threading

SLEEP_TIME = 1200  # 20 minutes in seconds = 1200s
BEEP_FREQUENCY = 1000
BEEP_DURATION = 3000


def Mbox(title, text, style=0):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


if __name__ == "__main__":
    while True:
        for i in range(100):
            threading.Thread(target=Mbox, args=["Get Back To Work", "It's been 20 minutes,"
                                                                    " get off your phone!"]).start()
        winsound.Beep(BEEP_FREQUENCY, BEEP_DURATION)
        time.sleep(SLEEP_TIME)
