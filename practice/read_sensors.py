from sense_hat import SenseHat
import time

sense = SenseHat()
sense.low_light = True

try:
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    print(f"Temperature: {temp:.2f} C")
    print(f"Relative humidity: {humidity:.2f} %")
    print(f"Pressure: {pressure:.2f} hPa")
    sense.show_letter("W")
    input("Look for a W on the matrix. Press Enter to finish. ")
    
finally:
    sense.clear()




