from itertools import izip
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
        self._color1 = (255, 212, 125)
        self._color2 = (245, 135, 76)
        self._myadd = lambda xs,ys: tuple(x + y for x, y in izip(xs, ys))

        print "Clock color:" + str(self._color)
        print "Background color:" + str(self._backgroundColor)

    def preRun(self):
        self._led.fillScreen(self._backgroundColor)

    def step(self, amt = 1):
        now = datetime.datetime.now()
        minute = now.minute;
        hour = now.hour + now.minute / 60.0

        if hour < 6.0:
            backgroundColor = self._color2
        elif hour < 18.0:
            backgroundColor = self._backgroundColor
        elif hour < 20.0:
            a = int(math.floor(max(0.0, (hour - 18.0) * 128.0)))
            backgroundColor = self._myadd(colors.color_scale(self._backgroundColor, 255 - a), colors.color_scale(self._color1, a))
        elif hour < 22.0:
            a = int(math.floor(max(0.0, (hour - 20.0) * 128.0)))
            backgroundColor = self._myadd(colors.color_scale(self._color1, 255 - a), colors.color_scale(self._color2, a))
        else:
            backgroundColor = self._color2

        height_f = 6 * minute / 60;
        y = int(math.floor(height_f))
        fraction = height_f - y

        led = self._led
        led.fillScreen(backgroundColor);
        led.drawLine(0, y, led.width - 1, y, self._color)

        self._step += amt
