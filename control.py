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

r = 64
g = 64
b = 64
anim = None

led.fillScreen((r, g, b))
led.update()

while True:
    print "r: " + repr(r) + ", g: " + repr(g) + ", v: " + repr(b)
    c = getch.getch()
    print c

    if anim != None:
        anim.stopThread(True)
        anim = None

    if c == 'q':
        break
    elif c == 'w':
        r = min(255, r + 4)
    elif c == 'x':
        r = max(0, r - 4)
    elif c == 'e':
        g = min(255, g + 4)
    elif c == 'c':
        g = max(0, g - 4)
    elif c == 'r':
        b = min(255, b + 4)
    elif c == 'v':
        b = max(0, b - 4)
    elif c == '1':
        anim = leuchtturm.Leuchtturm(led, period = 1)
        anim.run(threaded = True)

    if anim == None:
        led.fillScreen((r, g, b))
        led.update()

led.all_off()
led.update()