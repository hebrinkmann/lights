from flask import Flask
from bibliopixel.drivers.LPD8806 import DriverLPD8806
from bibliopixel.drivers.driver_base import ChannelOrder
import light

driver = DriverLPD8806(num = 60, c_order = ChannelOrder.BRG)

#load the LEDMatrix class
from bibliopixel.led import *
#change rotation and vert_flip as needed by your display
led = LEDMatrix(driver, width=10, height=6, serpentine = False, rotation = MatrixRotation.ROTATE_0, vert_flip = False)

app = Flask(__name__)
app.debug = True

light = light.Light(led, (255, 192, 128))

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/showDefaultColor", methods = ["PUT"])
def showDefaultColor():
    light.showDefaultColor()
    light.update()
    return repr(light.getColor())

@app.route("/off", methods = ["PUT"])
def off():
    light.setValue(0)
    light.update()
    return repr(light.getColor())

@app.route('/value/<int:value>', methods = ["PUT"])
def setValue(value):
    light.setValue(value)
    light.update()
    return repr(light.getColor())


if __name__ == "__main__":
    app.run(host="0.0.0.0")

led.all_off()
led.update()
