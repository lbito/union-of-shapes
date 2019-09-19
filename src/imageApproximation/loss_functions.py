import numpy as np

class Loss_one:
    alpha = 1

    def __init__(self, alpha):
        self.alpha = alpha

    def compute_loss(self, yhat, y):
        difference = y - yhat
        loss = sum(list(map(lambda x: (
            abs(x*self.alpha) if (x<0) else abs(x)
        ), difference)))
        return loss
