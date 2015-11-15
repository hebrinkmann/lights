import bibliopixel.colors as colors
#Load driver for your hardware, visualizer just for example
import time
import math
import pdb
import datetime

from bibliopixel.animation import BaseMatrixAnim
class DigitalClock(BaseMatrixAnim):
    digits = {
    '0': [
    "***",
    "* *",
    "* *",
    "* *",
    "***"
    ],
    '1': [
    "  *",
    "  *",
    "  *",
    "  *",
    "  *"
    ],
    '2': [
    "***",
    "  *",
    "***",
    "*  ",
    "***"
    ],
    '3': [
    "***",
    "  *",
    "***",
    "  *",
    "***"
    ],
    '4': [
    "* *",
    "* *",
    "***",
    "  *",
    "  *"
    ],
    '5': [
    "***",
    "*  ",
    "***",
    "  *",
    "***"
    ],
    '6': [
    "***",
    "*  ",
    "***",
    "* *",
    "***"
    ],
    '7': [
    "***",
    "  *",
    "  *",
    "  *",
    "  *"
    ],
    '8': [
    "***",
    "* *",
    "***",
    "* *",
    "***"
    ],
    '9': [
    "***",
    "* *",
    "***",
    "  *",
    "***"
    ],
    ':': [
    "   ",
    " * ",
    "   ",
    " * ",
    "   "
    ]
    }
    def __init__(self, led, start=0, end=-1, color=colors.White):
        #The base class MUST be initialized by calling super like this
        super(DigitalClock, self).__init__(led, start, end)
        self._color = color

    def step(self, amt = 1):
        self._led.all_off()
        offset = self._led.width - self._step / 3;
        for digit in datetime.datetime.now().strftime("%H:%M"):
            dots = self.digits[digit]

            y = 0
            for row in dots:
                x = offset
                for dot in row:
                    if dot == '*':
                        self._led.set(self._led.width - 1 - x, self._led.height - 1 - y, self._color)

                    x += 1
                y += 1

            offset += 4

        self._step += amt
