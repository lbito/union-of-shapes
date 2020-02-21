import numpy as np
from shape import Shape


NUM_ANGLES = 4

class Triangle(Shape):
    name = "triangle"
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    x3 = 0
    y3 = 0

    def __init__(self, args):
        self.x1, self.y1 = args[0]
        self.x2, self.y2 = args[1]
        self.x3, self.y3 = args[2]

    def update_params(self):
        atr = np.random.randint(0, 6)
        direction = np.random.choice([-1, 1])
        if (atr) == 0: self.x1 = abs(self.x1 + direction)
        if (atr) == 1: self.y1 = abs(self.y1 + direction)
        if (atr) == 2: self.x2 = abs(self.x2 + direction)
        if (atr) == 3: self.y2 = abs(self.y2 + direction)
        if (atr) == 4: self.x3 = abs(self.x3 + direction)
        if (atr) == 5: self.y3 = abs(self.y3 + direction)

    # 2d array bitmap rendering
    def render(self, imdraw):
        imdraw.polygon([(self.x1,self.y1),(self.x2,self.y2),(self.x3,self.y3)], 1)
        return

    def __str__(self):
        return "{0}{1}{2}{3}{4}{5}".format(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)
