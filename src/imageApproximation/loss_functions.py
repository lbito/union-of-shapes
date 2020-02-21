import numpy as np
from sklearn.metrics import mean_squared_error
from abc import ABC, abstractmethod

class Loss_Function(ABC):
    @abstractmethod
    def compute_loss(self): pass

class Loss_one(Loss_Function):
    alpha = 1

    def __init__(self, alpha):
        self.alpha = alpha

    def compute_loss(self, yhat, y):
        difference = y - yhat
        loss = 0
        for pixel in difference:
                if (pixel < 0 ):
                loss += abs(pixel) * self.alpha
            elif(pixel==0):
                loss -= self.alpha
            else:
                pixel += abs(pixel)
        return loss

class MSE(Loss_Function):
    alpha = 1

    def __init__(self):
        return
    def compute_loss(self, yhat, y):
        return mean_squared_error(y, yhat)
