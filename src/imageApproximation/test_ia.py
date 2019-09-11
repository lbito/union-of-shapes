import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
import sklearn.metrics
from PIL import Image, ImageDraw

from rectangle import Rectangle
from image_approximator import ImageApproximator

IMAGE_SIZE = (50,50)


im = Image.new('1', IMAGE_SIZE)
draw = ImageDraw.Draw(im)

r1 = Rectangle([(5,5),15,15,0])
draw.rectangle([r1.x,r1.y,r1.x+r1.w, r1.y + r1.h],1)
r1 = Rectangle([(15,15),20,20,0])
draw.rectangle([r1.x,r1.y,r1.x+r1.w, r1.y + r1.h],1)


# plt.imshow(im)
# plt.show()

# truth = np.asarray(im)
# ia = ImageApproximator(truth, sklearn.metrics.mean_squared_error)
# ia.update()
# ia.update()
# ia.show()


im2 = Image.open('test.png')
im2 = im2.convert('1',dither=0)
im2 = im2.resize(IMAGE_SIZE)

truth = np.asarray(im2)
ia = ImageApproximator(truth, sklearn.metrics.mean_squared_error)
ia.update()
ia.update()
ia.update()


ia.show()