import numpy as np
import copy
import matplotlib.pyplot as plt
import scipy.ndimage
import sklearn.metrics
from PIL import Image, ImageDraw
from rectangle import Rectangle
from loss_functions import Loss_one
from ellipse import Ellipse

IMAGE_SIZE = (50,50)
FLAT_DIM = IMAGE_SIZE[0] * IMAGE_SIZE[1]
N_ITERATIONS = 1000
N_SHAPES = 5
CONVERGENCE_THRESHOLD = 0.8

loss_function = Loss_one(5).compute_loss

class ImageApproximator():
    ground_truth = []
    loss_fn = None
    shapes = []
    convergence_status = False
    loss = None

    def __init__(self, truth, loss_fn=loss_function):
        self.ground_truth = np.array(truth, dtype=np.int32)
        self.loss_fn = loss_fn
        self.shapes = []

    def pick_centroid(self):
        pixels = np.nonzero(self.ground_truth)
        im = Image.new('1', IMAGE_SIZE)
        draw = ImageDraw.Draw(im)
        if (self.shapes == []): return (np.random.choice(pixels[0]),np.random.choice(pixels[1]))

        for shape in self.shapes:
            if (shape.name == "rectangle"):
                draw.rectangle([shape.x, shape.y, shape.x + shape.w, shape.y + shape.h], 1)
            elif (shape.name =="ellipse"):
                draw.ellipse([shape.x, shape.y, shape.x + shape.w, shape.y + shape.h], 1)
        current_render = np.array(im)
        masked_shape = self.ground_truth - current_render
        masked_shape = masked_shape.clip(min=0)

        pixels = np.nonzero(masked_shape)


        if (pixels[0].size == 0):
            return None
        c = (np.random.choice(pixels[0]), np.random.choice(pixels[1]))
        return c

    def update(self):
        #init centroid
        centroid = self.pick_centroid()
        if(centroid == None):
             return
        #pick shape and init and init at centroid
        shapes = [
            Rectangle([centroid,1,1,0]),
            Ellipse([centroid,2,2])
        ]

        shapes_losses = []

        for shape in shapes:
            current_loss = self.current_loss()
            for i in range(0, N_ITERATIONS):
                old_shape = copy.deepcopy(shape)

                shape.update_params()
                self.shapes.append(shape)
                new_loss = self.current_loss()

                if (new_loss > current_loss):
                    shape = copy.deepcopy(old_shape)
                else:
                    current_loss = new_loss
                del self.shapes[-1]
            shapes_losses.append((shape, current_loss))

        min_shape_idx = np.argmin([x[1] for x in shapes_losses])
        self.shapes.append(shapes_losses[min_shape_idx][0])


    def current_loss(self):
        if (self.shapes == []): return np.Infinity

        im = Image.new('1', IMAGE_SIZE)
        draw = ImageDraw.Draw(im)

        for shape in self.shapes:
            if (shape.name == "rectangle"):
                draw.rectangle([shape.x, shape.y, shape.x + shape.w, shape.y + shape.h], 1)
            elif (shape.name =="ellipse"):
                draw.ellipse([shape.x, shape.y, shape.x + shape.w, shape.y + shape.h], 1)

        rendered_rect = np.array(im, dtype=np.int32)

        return (self.loss_fn(
            np.reshape(self.ground_truth, FLAT_DIM),
            np.reshape(rendered_rect, FLAT_DIM)))


    def show(self):
        im = Image.new('1', IMAGE_SIZE)
        draw = ImageDraw.Draw(im)
        for shape in self.shapes:
            if (shape.name == "rectangle"):
                draw.rectangle([shape.x, shape.y, shape.x + shape.w, shape.y + shape.h], 1)
            elif (shape.name =="ellipse"):
                draw.ellipse([shape.x, shape.y, shape.x + shape.w, shape.y + shape.h], 1)
        plt.imshow(np.array(im))
        plt.show()
