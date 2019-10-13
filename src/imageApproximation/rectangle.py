import numpy as np

NUM_ANGLES = 4


class Rectangle:
    name = "rectangle"
    x = 0
    y = 0
    w = 0
    h = 0
    theta = 0

    def __init__(self, args):
        self.x, self.y = args[0]
        self.w = args[1]
        self.h = args[2]
        self.theta = args[3]

    def update_params(self):
        atr = np.random.randint(0, 5)
        direction = np.random.choice([-1, 1])
        if (atr) == 0: self.x = abs(self.x + direction)
        if (atr) == 1: self.y = abs(self.y + direction)
        if (atr) == 2: self.w = abs(self.w + direction)
        if (atr) == 3: self.h = abs(self.h + direction)
        if (atr) == 4: self.theta += (direction * NUM_ANGLES) / 360

    # 2d array bitmap rendering
    def render(self, image_size):
        pass

    def __str__(self):
        return "{0}{1}{2}{3}".format(self.x, self.y, self.w, self.h)
