# icon-generation-svg

**Introduction**  

The aim of this project is to generate vector graphic representations of icons. To achieve this goal we propose a preprocessing step of detecting bounded vector approximations of raster images using only geometric primitives. This vectorised dataset will become the training set for the discriminator component of the GAN for generating new icons. This form of dimensionality reduction may help improve the stability of the GAN during training. Another benefit of leveraging this preprocessing step is that it easier to control variations or condition the GAN by modifying the encoded input. i.e. color scheme.
