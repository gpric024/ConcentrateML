import time
import winsound
SLEEP_TIME = 1200  # 20 minutes in seconds = 1200s
BEEP_FREQUENCY = 1000
BEEP_DURATION = 1000


if __name__ == "__main__":
    while True:
        print("GET BACK TO WORK!")
        winsound.Beep(BEEP_FREQUENCY, BEEP_DURATION)
        time.sleep(SLEEP_TIME)