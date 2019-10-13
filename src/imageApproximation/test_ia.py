import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
import sklearn.metrics
from PIL import Image, ImageDraw
from loss_functions import Loss_one

from rectangle import Rectangle
from ellipse import Ellipse
from triangle import Triangle
from image_approximator import ImageApproximator

IMAGE_SIZE = (50,50)


im = Image.new('1', IMAGE_SIZE)
draw = ImageDraw.Draw(im)
# #
# r1 = Rectangle([(5,5),15,15,0])
# draw.rectangle([r1.x,r1.y,r1.x+r1.w, r1.y + r1.h],1)
# r1 = Ellipse([(15,15),20,20,0])
# draw.ellipse([r1.x,r1.y,r1.x+r1.w, r1.y + r1.h],1)
t1 = Triangle([(5,5),(30,20),(5,30)])
t2 = draw.polygon([(t1.x1,t1.y1), (t1.x2,t1.y2), (t1.x3,t1.y3)], fill=1)

plt.imshow(im)
plt.show()


truth = np.asarray(im)

ia = ImageApproximator(truth, Loss_one(30).compute_loss)
# ia = ImageApproximator(truth)

ia.update()
ia.show()
# ia.update()
# ia.update()
# ia.update()

# ia.show()

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
