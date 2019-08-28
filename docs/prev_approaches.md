http://files.is.tue.mpg.de/black/papers/OpenDR.pdf

https://arxiv.org/abs/1503.03167

https://arxiv.org/pdf/1904.02632.pdf

http://files.is.tue.mpg.de/black/papers/OpenDR.pdf



### Learn an Encoding and Decoding function for generating SVG output  of raster input.

f(x) : takes input returns encoding

$g(x|\theta)$: takes encoding and returns SVG output.

- Rendering not differentiable (autodiff)



---

Alternative



The methods proposed in deepprimitive paper  __ref .



- A framework based on the YOLOv2 network thatenables class-wise parameter regression for differentprimitives.
- An RNN model to estimate a sequence of a variable number  of  control  points  representing  a  closed spline curve in a single 2D image.
- A  layered  primitive  detection  model  to  extract relationship information from an image.



Part 1. Implement class-wise parameter regression for different primitives (extension is sline based regression OR bezier curves)

Part 2. Generate Mock Dataset and test model. i.e. (generate random primitive shapes)

Part 3. Apply model to generate Input dataset for GAN.

Part 4. Test GAN on new dataset
