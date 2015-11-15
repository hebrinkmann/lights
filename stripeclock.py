import bibliopixel.colors as colors
#Load driver for your hardware, visualizer just for example
import datetime
import math

from bibliopixel.animation import BaseMatrixAnim
class StripeClock(BaseMatrixAnim):
    def __init__(self, led, start=0, end=-1, backgroundColor = colors.White, clockColor = colors.Red):
        #The base class MUST be initialized by calling super like this
        super(StripeClock, self).__init__(led, start, end)
        self._backgroundColor = backgroundColor
        self._color = colors.color_blend(colors.color_scale(backgroundColor, 128), clockColor)
        print "Clock color:" + str(self._color)
        print "Background color:" + str(self._backgroundColor)

    def preRun(self):
        self._led.fillScreen(self._backgroundColor)

    def step(self, amt = 1):
        minute = datetime.datetime.now().minute;
        height_f = 6 * minute / 60;
        y = int(math.floor(height_f))
        fraction = height_f - y

        led = self._led
        led.fillScreen(self._backgroundColor);
        led.drawLine(0, y, led.width - 1, y, self._color)

        self._step += amt
