import pickle
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage

with open('test.p', 'rb') as f:
    data = pickle.load(f)

v_data = np.array(data['vector'])
r_data = np.array(data['raster'])

image_size = (50,50)

def render_rect(rect):
    w,h = image_size
    rect = np.round(np.array(rect))
    im_w, im_h = image_size
    x1, y1, x2, y2 = rect
    im = np.zeros((image_size))

    for i in range(int(y1),int(y2)):
        for j in range(int(x1),int(x2)):
            im[i,j] = 1
    im = np.reshape(im, w*h)
    return im

def loss(yhat, y):
    mean_loss = np.mean(np.sum(abs(yhat - y)*5))
    return mean_loss

def update_params(rectangle):
    #chose which attribute to change
    atr = np.random.randint(0,4);
    direction = np.random.choice([-1,1])
    rectangle[atr] += direction
    return rectangle

def update(vector, truth):
    #update logic, for now just random
    rendered = render_rect(vector)
    ls = loss(rendered, truth)
    if (ls==0):
        print("CONVERGED")
        print(vector)
        return [False, 1]
    nls = ls
    newvec = np.array(vector)
    while (nls >= ls):
        newvec = update_params(newvec)
        rendered = render_rect(newvec)
        nls = loss(rendered, truth)
        if (nls > ls):
            newvec = np.array(vector)
    return [newvec, 0]

test_v = np.array([10,10,40,40])
zz = np.array([25,25,26,26])
test_r = render_rect(test_v)

from matplotlib.pyplot import imread, imshow
import cv2

img = cv2.imread('./playground/data/test2.png',0)
ret,thresh_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
test_circle = np.reshape(thresh_img, (2500,1))
zz = np.array([25,25,26,26])

for i in range(0,2):
    zz, convergence_status = update(zz,test_circle)
    imshow(np.reshape(render_rect(zz),(50,50)))
    if (convergence_status == 1):
        print(zz)
        break

print(zz)

im = np.reshape(test_r,(32,32))
plt.imshow(im)
vhat = np.array([14,14,15,15])


vhat = update(vhat, test_r)
print(vhat)
