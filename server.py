from flask import Flask
from flask import request
from flask import Response
from flask import json
from bibliopixel.drivers.LPD8806 import DriverLPD8806
from bibliopixel.drivers.driver_base import ChannelOrder
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

light.show_default_color()
light.update()

anims = {
    "leuchtturm": leuchtturm.Leuchtturm(led, period = 5),
    "stripeclock": stripeclock.StripeClock(led, backgroundColor = light.get_color_scaled())
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

@app.route('/anim', methods = ["GET"])
def getAnim():
    return anim.__name__

@app.route('/list/anim', methods = ["GET"])
def listAnims():
    return json.JSONEncoder().encode(anims.keys())

@app.route('/light', methods = ["GET"])
def getLight():
    return Response(
        json.dumps({
            "light": {
                "color": light.getColor(),
                "value": light.getValue()
            }
        }),
        mimetype = 'application/json'
    )

@app.route('/color', methods = ["GET"])
def getColor():
    return Response(json.dumps(light.getColor()), mimetype = 'application/json')

@app.route('/color', methods = ["PUT"])
def setColor():
    oldColor = light.getColor()
    data = json.JSONDecoder().decode(request.data)
    color = data['color']
    light.setColor(color)

    return json.JSONEncoder().encode(oldColor)

@app.route('/help', methods = ["GET"])
def help():
    return str(app.url_map)

if __name__ == "__main__":
    app.run()

led.all_off()
led.update()
