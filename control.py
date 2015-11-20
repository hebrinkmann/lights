import bibliopixel.colors as colors
#Load driver for your hardware, visualizer just for example
from bibliopixel.drivers.LPD8806 import DriverLPD8806
from bibliopixel.drivers.driver_base import ChannelOrder
import light
import leuchtturm
import fadedown
import digitalclock
import stripeclock

driver = DriverLPD8806(num = 60, c_order = ChannelOrder.BRG)

#load the LEDMatrix class
from bibliopixel.led import *
#change rotation and vert_flip as needed by your display
led = LEDMatrix(driver, width=10, height=6, serpentine = False, rotation = MatrixRotation.ROTATE_0, vert_flip = False)


class MyLight(light.Light):
    def __init__(self, led, defaultColor):
        super(MyLight, self).__init__(led, defaultColor)

    def initCommands(self):
        self._commands = {
            '1': lambda: self.startAnim(leuchtturm.Leuchtturm(self._led, period = 5)),
            '2': lambda: self.startAnim(fadedown.FadeDown(self._led, color = self.getColorScaled(), duration = 30)),
            '3': lambda: self.startAnim(digitalclock.DigitalClock(self._led, color = self.getColorScaled())),
            '4': lambda: self.startAnim(stripeclock.StripeClock(self._led, backgroundColor = self.getColorScaled())),
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