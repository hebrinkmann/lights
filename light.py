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
        self.commands = None

    def init_commands(self):
        self.commands = {}

    def set_color(self, color):
        self._color = color
        self._value = 255
        self.show_color()

    def show_color(self):
        self._led.fillScreen(self.get_color_scaled())

    def get_color(self):
        return self._color

    def get_color_scaled(self):
        return colors.color_scale(self._color, self._value)

    def show_default_color(self):
        self._color = self._defaultColor
        self.show_color()

    def start_anim(self, anim, sleep = None, fps = 25):
        self.anim = anim
        anim.run(threaded = True, sleep = sleep, fps = fps)

    def stop_anim(self):
        if self.anim != None:
            self.anim.stopThread(True)
            self.anim = None

    def increase_value(self):
        self._value = min(255, self._value + 4)
        self.show_color()

    def decrease_value(self):
        self._value = max(0, self._value - 4)
        self.show_color()

    def increase_red(self):
        self._color = (min(255, self._color[0] + 4), self._color[1], self._color[2])
        self.show_color()

    def decrease_red(self):
        self._color = (max(0, self._color[0] - 4), self._color[1], self._color[2])
        self.show_color()

    def increase_green(self):
        self._color = (self._color[0], min(255, self._color[1] + 4), self._color[2])
        self.show_color()

    def decrease_green(self):
        self._color = (self._color[0], max(0, self._color[1] - 4), self._color[2])
        self.show_color()

    def increase_blue(self):
        self._color = (self._color[0], self._color[1], min(255, self._color[2] + 4))
        self.show_color()

    def decrease_blue(self):
        self._color = (self._color[0], self._color[1], max(0, self._color[2] - 4))
        self.show_color()

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = max(0, min(255, value))
        self.show_color()

    def update(self):
        self._led.update()

    def run(self):
        self.init_commands()
        self.show_default_color()

        while True:
            self._led.update()
            c = getch.getch()

            if (c == 'q'):
                break
            else:
                self.stop_anim()

                try:
                    command = self.commands[c]
                    if command:
                        command()
                except KeyError:
                    self.show_default_color()
