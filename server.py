from flask import Flask
from bibliopixel.drivers.LPD8806 import DriverLPD8806
from bibliopixel.drivers.driver_base import ChannelOrder
import json
import light
import leuchtturm
import stripeclock

driver = DriverLPD8806(num = 60, c_order = ChannelOrder.BRG)

#load the LEDMatrix class
from bibliopixel.led import *
#change rotation and vert_flip as needed by your display
led = LEDMatrix(driver, width=10, height=6, serpentine = False, rotation = MatrixRotation.ROTATE_0, vert_flip = False)

app = Flask(__name__)
app.debug = True

light = light.Light(led, (255, 192, 128))

light.showDefaultColor()
light.update()

anims = {
    "leuchtturm": leuchtturm.Leuchtturm(led, period = 5),
    "stripeclock": stripeclock.StripeClock(led, backgroundColor = light.getColor())
}

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/showDefaultColor", methods = ["PUT"])
def showDefaultColor():
    light.stopAnim()
    light.showDefaultColor()
    light.update()
    return repr(light.getColor())

@app.route("/off", methods = ["PUT"])
def off():
    light.stopAnim()
    light.setValue(0)
    light.update()
    return repr(light.getColor())

@app.route('/value/<int:value>', methods = ["PUT"])
def setValue(value):
    light.stopAnim()
    light.setValue(value)
    light.update()
    return repr(light.getColor())

@app.route('/anim/<string:value>', methods = ["PUT"])
def anim(value):
    light.stopAnim()
    anim = None
    try:
        anim = anims[value]
        light.stopAnim()
        light.startAnim(anim)
    except KeyError:
        light.showDefaultColor
        light.update()

    return value

@app.route('/light', methods = ["GET"])
def getLight():
    return json.JSONEncoder().encode({ "light": { "color": "green"}})


if __name__ == "__main__":
    app.run()

led.all_off()
led.update()
