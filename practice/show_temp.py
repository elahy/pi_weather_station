from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    temp = sense.get_temperature()
    sense.show_message(f"{temp:.1f} C", scroll_speed=0.1)
    time.sleep(2)