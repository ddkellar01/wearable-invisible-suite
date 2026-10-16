# Edge Perspective Warping Documentation

## Mathematical Principles
To achieve seamless active camouflage, the system maps background lighting and geometry relative to the observer's viewing angle. 

Homography matrix estimation is computed via:
$$H = K \cdot (R - \frac{t \cdot n^T}{d}) \cdot K^{-1}$$

Where $K$ represents camera intrinsics, $R$ and $t$ represent relative rotation and translation, and $n, d$ define the background plane equation.
