**Image Approximator**

The goal of the image approximation step is to take an Image and return a set of geometric primitives (roughly in SVG format) that, when rendered, approximately reconstruct that image (according to some loss function).

1. Given an image, find highest density clusters in the image minus already accounted for pixels, use these as the initialisation point for the algorithm.
2. For a given centroid, intialise each shape at the centroid and run update until convergence or termination. Chose the shape which yields the lowest loss for that centroid.
3. Repeat the steps above until the desired loss or number of shapes has been reached. at each step removing the newly rendered shape when calculating the next initialisation point.



Parameters:

threshold:: If the approximation reaches this value terminate early.
n_shapes:: Indicate how many shapes to use for reconstruction.
loss_fn:: The loss function to use for reconstruction loss.

Methods:

*loss(approximation_vec, ground_truth, loss_fn='mse'):*  
Returns the reconstruction loss of the approximation vector using loss_fn.

*render(image, approximation_vec):*  
renders the approximation vector on top of the existing image.

*update(approximation_vec, ground_truth, loss_fn, threshold, shape):*  
Performs one iteration of the algorithm to update the parameters of a single shape to better approximate the image. Returns the updated vector and the reconstruction loss.
