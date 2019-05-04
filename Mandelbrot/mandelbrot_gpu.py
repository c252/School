import numpy as np
import matplotlib.pyplot as plt
import torch

def mandelbrot(h, w, max_iter, threshold=2.0):
    x = torch.linspace(-2, 2, h, dtype=torch.float64)
    y = torch.linspace(-1.25, 1.25, w, dtype=torch.float64)

    c_x, c_y = torch.meshgrid([x, y])

    pxl = torch.zeros((w,h), dtype=torch.float64)
    x_z = torch.zeros(w*h, dtype=torch.float64)
    y_z = torch.zeros(w*h, dtype=torch.float64)

    for i in range(max_iter):
        infty = x_z**2 + y_z**2 > 4
        pxl[infty] = i

        x_z = x_z**2 + c_x
        y_z = 2*x_z*y_z + c_y

    return pxl.T

m = mandelbrot(500,500,512)
m = m.T #transpose the matrix
plt.imshow(m,cmap="nipy_spectral")
plt.axis("off")
plt.show()