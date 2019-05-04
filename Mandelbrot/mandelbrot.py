import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(max_iter, width, height, threshold=2.0):
    """
    Generates a mandelbrot set
    """
    x = np.linspace(-2.5, 1, width)
    y = np.linspace(-1.5, 1.5, height)
    c = x[:,np.newaxis] + 1j*y[np.newaxis,:]
    z = c

    for _ in range(max_iter):
        z = z**2 + c
    result = (abs(z) < threshold)
    return result

m = mandelbrot(1024, 1000, 750).transpose(1,0)
plt.imshow(m)
plt.axis("off")
plt.savefig("mandelbrot.png", dpi=1000)
