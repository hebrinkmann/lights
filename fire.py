import bibliopixel.colors as colors
import random

from bibliopixel.animation import BaseMatrixAnim
class Fire(BaseMatrixAnim):
    def __init__(self, led, start=0, end=-1):
        #The base class MUST be initialized by calling super like this
        super(Fire, self).__init__(led, start, end)
        self._buffer = [[[0.0 for x in range(led.height)] for x in range(led.width)] for x in range(2)]
        self._led = led

    def step(self, amt = 1):
        led = self._led
        if self._step % 5 == 0:
            index0 = (self._step / 10) % 2
            index1 = ((self._step / 10) + 1) %2
            for y in range(led.height):
                for x in range(led.width):
                    p = 0
                    n = 0
                    if x - 1 >= 0:
                        p += self._buffer[index0][x - 1][y]
                        n += 1
                    if x + 1 < led.width:
                        p += self._buffer[index0][x + 1][y]
                        n += 1

                    if y - 1 >= 0:
                        p += self._buffer[index0][x][y - 1]
                        n += 1

                    if y + 1 < led.height:
                        p += self._buffer[index0][x][y + 1]
                        n += 1

                    p = p / n - random.uniform(0.0, 0.2)
                    if p < 0:
                        p = 0

                    if y + 1 < led.height:
                        self._buffer[index1][x][y + 1] = p
            for x in range(led.width):
                self._buffer[index1][x][0] = random.uniform(0.75, 1.0)

            for y in range(led.height):
                for x in range(led.width):
                    value = int(self._buffer[index1][x][y] * 255)
                    led.setRGB(x, y, value, value, value)

        self._step += amt
