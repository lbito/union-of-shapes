import numpy as np



class Ellipse:
    name = "ellipse"
    x = 0
    y = 0
    w = 1
    h = 1
    
    def __init__(self, args):
        self.x, self.y = args[0]
        self.w = args[1]
        self.h = args[2]

    def update_params(self):
        atr = np.random.randint(0, 4)
        direction = np.random.choice([-1, 1])
        if (atr) == 0: self.x += direction
        if (atr) == 1: self.y += direction
        if (atr) == 2: self.w = abs(self.w + direction)
        if (atr) == 2: self.h = abs(self.h + direction)
