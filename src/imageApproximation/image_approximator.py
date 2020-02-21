import numpy as np
import copy
import matplotlib.pyplot as plt
import scipy.ndimage
import sklearn.metrics

from PIL import Image, ImageDraw
from rectangle import Rectangle
from loss_functions import Loss_one
from ellipse import Ellipse
from triangle import Triangle


IMAGE_SIZE = (32,32)
FLAT_DIM = IMAGE_SIZE[0] * IMAGE_SIZE[1]
N_ITERATIONS = 500
N_SHAPES = 5
CONVERGENCE_THRESHOLD = 0.8

loss_function = sklearn.metrics.mean_squared_error

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
            shape.render(draw)
        current_render = np.array(im)
        masked_shape = self.ground_truth - current_render
        masked_shape = masked_shape.clip(min=0)

        pixels = np.nonzero(masked_shape)
        if (pixels[0].size == 0):
            return None
        c = (np.random.choice(pixels[0]), np.random.choice(pixels[1]))
        return c

    
    def update(self):
        """
        performs update of all single shape until convergence or termination 
        picks shape that minimises loss
        """
        #init centroid
        centroid = self.pick_centroid()
        if(centroid == None):
             return
        #pick shape and init and init at centroid
        shapes = [
            Rectangle([centroid,1,1,0]),
            Ellipse([centroid,3,3]),
            Triangle([centroid,(centroid[0]+2,centroid[1]), ((centroid[0]+1,centroid[1]+2))])
        ]

        shapes_losses = []
        old_loss = self.current_loss()
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
        min_loss = shapes_losses[min_shape_idx][1]
        print(min_loss)
        if ((min_loss >= old_loss) and (len(self.shapes)>0)):
            return
        else:             
            self.shapes.append(shapes_losses[min_shape_idx][0])


    def current_loss(self):
        if (self.shapes == []): return np.Infinity

        im = Image.new('L', IMAGE_SIZE)
        draw = ImageDraw.Draw(im)

        for shape in self.shapes:
            shape.render(draw)
        rendered_rect = np.array(im, dtype=np.int32)

        return (self.loss_fn.compute_loss(
            np.reshape(self.ground_truth, FLAT_DIM),
            np.reshape(rendered_rect, FLAT_DIM)))


    def show(self):
        im = Image.new('1', IMAGE_SIZE)
        draw = ImageDraw.Draw(im)
        for shape in self.shapes:
            shape.render(draw)
        plt.imshow(np.array(im))
        plt.show()
