import bibliopixel.colors as colors
#Load driver for your hardware, visualizer just for example
from bibliopixel.drivers.LPD8806 import DriverLPD8806
from bibliopixel.drivers.driver_base import ChannelOrder
import math
import time
import pdb

driver = DriverLPD8806(num = 60, c_order = ChannelOrder.BRG)

#load the LEDMatrix class
from bibliopixel.led import *
#change rotation and vert_flip as needed by your display
led = LEDMatrix(driver, width=10, height=6, serpentine = False, rotation = MatrixRotation.ROTATE_0, vert_flip = False)

from bibliopixel.animation import BaseMatrixAnim
class Leuchtturm(BaseMatrixAnim):
    def __init__(self, led, start=0, end=-1, period = 20):
        #The base class MUST be initialized by calling super like this
        super(Leuchtturm, self).__init__(led, start, end)
        self._period = period
        #Create a color array to use in the animation
        redColor = colors.color_scale(colors.Red, 140)
        whiteColor = colors.color_scale(colors.White, 100)
        self._colors = [ redColor, whiteColor, redColor, whiteColor, redColor, colors.Off]

    def lightToX(self, x):
        direction = time.time() / self._period * self._led.width % self._led.width

        if 2 * (direction - x) > self._led.width:
            direction -= self._led.width

        if 2 * (x - direction) > self._led.width:
            direction += self._led.width

        intensity = int(255 - max(0, min(255, 128 * ((x - direction)) ** 2)))
        return colors.color_scale(colors.Orange, intensity)

    def step(self, amt = 1):
        for i in range(6):
            self._led.drawLine(0, i, self._led.width - 1, i, self._colors[i])

        for i in range(self._led.width):
            self._led.set(i, 5, self.lightToX(i))

        self._step += amt
