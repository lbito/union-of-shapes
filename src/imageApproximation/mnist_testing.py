import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

dat = pd.read_pickle("data/mnist.pkl.gz")
train_set, _ , _ = dat
X,y =  train_set

def show_digit(d):
    imshow(np.reshape(d, (28, 28)))
    plt.show()
