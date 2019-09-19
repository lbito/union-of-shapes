import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
import sklearn.metrics
from PIL import Image, ImageDraw

from rectangle import Rectangle
from ellipse import Ellipse
from image_approximator import ImageApproximator

IMAGE_SIZE = (50,50)


im = Image.new('1', IMAGE_SIZE)
draw = ImageDraw.Draw(im)
#
r1 = Rectangle([(5,5),15,15,0])
draw.rectangle([r1.x,r1.y,r1.x+r1.w, r1.y + r1.h],1)
r1 = Ellipse([(25,25),20,20,0])
draw.ellipse([r1.x,r1.y,r1.x+r1.w, r1.y + r1.h],1)
draw.rectangle([15,15,40,17],1)
draw.rectangle([5,5,40,7],1)
draw.rectangle([5,40,40,44],1)

# plt.imshow(im)
# plt.show()
#
truth = np.asarray(im)
#
# ia = ImageApproximator(truth, sklearn.metrics.mean_squared_error)
ia = ImageApproximator(truth)

ia.update()
# ia.show()
ia.update()
ia.update()
ia.update()

ia.show()

#-------------------------------------------------------------------------------

#
# im2 = Image.open('../../t2.png')
# im2 = im2.convert('1',dither=0)
# im2 = im2.resize(IMAGE_SIZE)
# im2.transpose(Image.FLIP_TOP_BOTTOM)
# truth = np.asarray(im2)
# #
# plt.imshow(im2)
# plt.show()
#
# ia = ImageApproximator(truth)
# ia.update()
# ia.show()
