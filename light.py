import getch
import bibliopixel.colors as colors
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
        self._led.fillScreen(self.getColorScaled())

    def getColor(self):
        return self._color

    def getColorScaled(self):
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

    def update(self):
        self._led.update()

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
