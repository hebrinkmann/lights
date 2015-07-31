import bibliopixel.colors as colors
#Load driver for your hardware, visualizer just for example
from bibliopixel.drivers.LPD8806 import DriverLPD8806
driver = DriverLPD8806(num = 60)

#load the LEDStrip class
from bibliopixel.led import *
led = LEDStrip(driver)

from bibliopixel.animation import BaseStripAnim
class StripTest(BaseStripAnim):
    def __init__(self, led, start=0, end=-1):
        #The base class MUST be initialized by calling super like this
        super(StripTest, self).__init__(led, start, end)

    def step(self, amt = 1):
	for i in range(self._led.numLEDs):
		color = colors.color_scale(self._led.get(i), 245)
		
		if i == (self._step % self._led.numLEDs):
			color = colors.color_blend(color, colors.hue2rgb_spectrum(self._step % 127))

		self._led.set(i, color);
        #Increment the internal step by the given amount
        self._step += amt


class StripLamp(BaseStripAnim):
	def __init__(self, led, start=0, end=-1, color=colors.White):
		super(StripLamp, self).__init__(led, start, end)
		self._color = color

	def step(self, amt = 1):
		self._led.fill(self._color)
		self._step += amt

#load channel test animation
#from bibliopixel.animation import StripChannelTest
anim = StripLamp(led, color = colors.hsv2rgb((64, 64, 128)))

try:
	anim.run(sleep = 10)
except KeyboardInterrupt:
	led.all_off()
	led.update()

