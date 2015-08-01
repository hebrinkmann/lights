import bibliopixel.colors as colors
#Load driver for your hardware, visualizer just for example
import time
import math

from bibliopixel.animation import BaseMatrixAnim
class FadeDown(BaseMatrixAnim):
    def __init__(self, led, start=0, end=-1, color = colors.White, duration = 5):
        #The base class MUST be initialized by calling super like this
        super(FadeDown, self).__init__(led, start, end)
        self._color = color
        self._duration = duration
        self._startTime = time.time()

    def preRun(self):
        self._led.fillScreen(self._color)

    def step(self, amt = 1):
        passedTime = time.time() - self._startTime
        height_f = 6 - 6 * (passedTime) / self._duration
        y = int(math.floor(height_f))
        fraction = height_f - y
        fraction_255 = int(255 * fraction)

        led = self._led
        led.drawLine(0, y, led.width - 1, y, colors.color_scale(self._color, fraction_255))

        self._step += amt
