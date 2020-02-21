import pickle
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage

from matplotlib.pyplot import imread, imshow
import cv2

image_size = (36,36)
width,height = image_size
from rectangle import Rectangle
rect = Rectangle(((0,0),10,10,0))
print(rect)

# def render_rect(rect):
#     w,h = image_size
#     rect = np.round(np.array(rect))
#     x1, y1, x2, y2 = rect
#     im = np.zeros((image_size))

#     for i in range(int(y1),int(y2)):
#         for j in range(int(x1),int(x2)):
#             im[i,j] = 1
#     im = np.reshape(im, w*h)
#     return im

# def loss(yhat, y):
#     mean_loss = np.mean(np.sum(abs(yhat - y)*5))
#     return mean_loss

# def update_params(rectangle):
#     #chose which attribute to change
#     atr = np.random.randint(0,4)
#     direction = np.random.choice([-1,1])
#     rectangle[atr] += direction
#     return rectangle

# def update(vector, truth):
#     #update logic, for now just random
#     rendered = render_rect(vector)
#     ls = loss(rendered, truth)
#     if (ls==0):
#         print("CONVERGED")
#         print(vector)
#         return [False, 1]
#     nls = ls
#     newvec = np.array(vector)
#     while (nls >= ls):
#         newvec = update_params(newvec)
#         rendered = render_rect(newvec)
#         nls = loss(rendered, truth)
#         if (nls > ls):
#             newvec = np.array(vector)
#     return [newvec, 0]


# img = cv2.imread('../../data/test/2.png', cv2.IMREAD_UNCHANGED)
# b,g,r,alpha = cv2.split(img)
# img = alpha

# ret,thresh_img = cv2.threshold(img,125,255,cv2.THRESH_BINARY)
# test_circle = np.reshape(thresh_img, (width*height,1))

# zero_mat = np.zeros((36,36),dtype=np.int32)
# print(np.shape(zero_mat))
# for i in range(0,2):
#     zz, convergence_status = update(zero_mat,test_circle)
#     imshow(np.reshape(render_rect(zz),(36,36)))
#     if (convergence_status == 1):
#         print(zz)
#         break
#     cv2.imshow(zz)


