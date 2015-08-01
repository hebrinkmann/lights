import getch
import bibliopixel.colors as colors
#Load driver for your hardware, visualizer just for example
from bibliopixel.drivers.LPD8806 import DriverLPD8806
from bibliopixel.drivers.driver_base import ChannelOrder

driver = DriverLPD8806(num = 60, c_order = ChannelOrder.BRG)

#load the LEDMatrix class
from bibliopixel.led import *
#change rotation and vert_flip as needed by your display
led = LEDMatrix(driver, width=10, height=6, serpentine = False, rotation = MatrixRotation.ROTATE_0, vert_flip = False)

import leuchtturm
import fadedown
import matrix_animations

class Light(object):
    def __init__(self, led, defaultColor):
        self.anim = None
        self._led = led
        self._defaultColor = defaultColor
        self._color = defaultColor
        self._value = 255

    def initCommands(self):
        self._commands = {}

    def setColor(self, color):
        self._color = color
        self._value = 255
        self.showColor()

    def showColor(self):
        self._led.fillScreen(self.getColor())

    def getColor(self):
        return colors.color_scale(self._color, self._value)

    def showDefaultColor(self):
        self._color = self._defaultColor
        self.showColor()

    def startAnim(self, anim, sleep = None, fps = 25):
        self.anim = anim
        anim.run(threaded = True, sleep = sleep, fps = fps)

    def stopAnim(self):
        if self.anim != None:
            self.anim.stopThread(True)
            self.anim = None

    def increaseValue(self):
        self._value = min(255, self._value + 4)
        self.showColor()

    def decreaseValue(self):
        self._value = max(0, self._value - 4)
        self.showColor()

    def increaseRed(self):
        self._color = (min(255, self._color[0] + 4), self._color[1], self._color[2])
        self.showColor()

    def decreaseRed(self):
        self._color = (max(0, self._color[0] - 4), self._color[1], self._color[2])
        self.showColor()

    def increaseGreen(self):
        self._color = (self._color[0], min(255, self._color[1] + 4), self._color[2])
        self.showColor()

    def decreaseGreen(self):
        self._color = (self._color[0], max(0, self._color[1] - 4), self._color[2])
        self.showColor()

    def increaseBlue(self):
        self._color = (self._color[0], self._color[1], min(255, self._color[2] + 4))
        self.showColor()

    def decreaseBlue(self):
        self._color = (self._color[0], self._color[1], max(0, self._color[2] - 4))
        self.showColor()

    def setValue(self, value):
        self._value = max(0, min(255, value))
        self.showColor()

    def run(self):
        self.initCommands()
        self.showDefaultColor()

        while True:
            self._led.update()
            c = getch.getch()

            if (c == 'q'):
                break
            else:
                self.stopAnim()

                try:
                    command = self._commands[c]
                    if command:
                        command()
                except KeyError:
                    self.showDefaultColor()

class MyLight(Light):
    def __init__(self, led, defaultColor):
        super(MyLight, self).__init__(led, defaultColor)

    def initCommands(self):
        self._commands = {
            '1': lambda: self.startAnim(leuchtturm.Leuchtturm(self._led, period = 5)),
            '2': lambda: self.startAnim(fadedown.FadeDown(self._led, color = self.getColor(), duration = 3)),
            'o': lambda: self.setValue(0),
            'O': lambda: self.setValue(255),
            'r': lambda: self.decreaseRed(),
            'R': lambda: self.increaseRed(),
            'g': lambda: self.decreaseGreen(),
            'G': lambda: self.increaseGreen(),
            'b': lambda: self.decreaseBlue(),
            'B': lambda: self.increaseBlue(),
            'w': lambda: self.setColor(colors.White),
            '+': lambda: self.increaseValue(),
            '-': lambda: self.decreaseValue()
        }

light = MyLight(led, (255, 192, 128))
light.run()

led.all_off()
led.update()