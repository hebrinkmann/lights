import bibliopixel.colors as colors
#Load driver for your hardware, visualizer just for example
from bibliopixel.drivers.LPD8806 import DriverLPD8806
from bibliopixel.drivers.visualizer import DriverVisualizer
from bibliopixel.drivers.driver_base import ChannelOrder
import light
import leuchtturm
import fadedown
import digitalclock
import stripeclock
import fire

#driver = DriverLPD8806(num = 60, c_order = ChannelOrder.BRG)
driver = DriverVisualizer(width=10, height=6, pixelSize=20, stayTop = True)

#load the LEDMatrix class
from bibliopixel.led import *
#change rotation and vert_flip as needed by your display
#led = LEDMatrix(driver, width=10, height=6, serpentine = False, rotation = MatrixRotation.ROTATE_0, vert_flip = False)
led = LEDMatrix(driver, width=10, height=6, rotation = MatrixRotation.ROTATE_180)


class MyLight(light.Light):
    def __init__(self, led, defaultColor):
        super(MyLight, self).__init__(led, defaultColor)

    def init_commands(self):
        self.commands = {
            '1': lambda: self.start_anim(leuchtturm.Leuchtturm(self._led, period = 5)),
            '2': lambda: self.start_anim(fadedown.FadeDown(self._led, color = self.get_color_scaled(), duration = 30)),
            '3': lambda: self.start_anim(digitalclock.DigitalClock(self._led, color = self.get_color_scaled())),
            '4': lambda: self.start_anim(stripeclock.StripeClock(self._led, backgroundColor = self.get_color_scaled())),
            '5': lambda: self.start_anim(fire.Fire(self._led, color = self.get_color_scaled())),
            'o': lambda: self.set_value(0),
            'O': lambda: self.set_value(255),
            'r': lambda: self.decrease_red(),
            'R': lambda: self.increase_red(),
            'g': lambda: self.decrease_green(),
            'G': lambda: self.increase_green(),
            'b': lambda: self.decrease_blue(),
            'B': lambda: self.increase_blue(),
            'w': lambda: self.set_color(colors.White),
            '+': lambda: self.increase_value(),
            '-': lambda: self.decrease_value()
        }

light = MyLight(led, (255, 192, 128))
light.run()

led.all_off()
led.update()