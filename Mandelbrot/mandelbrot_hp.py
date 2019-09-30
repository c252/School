import numpy as np
import matplotlib.pyplot as plt
from math import e, log10

def mandelbrot(c, max_iter,threshold=2.0):
    z = c
    for i in range(max_iter):
        if abs(z) > threshold:
            return i
        z = z**2 + c
    return 0 #return 0 if element of mandelbrot set

def julia(z, max_iter, threshold=2.0, n=3.0, a=1.0):
    #c = -0.835 - 0.2321j
    #c = 0.285 - 0.01j
    c = -0.7269 + 0.1889j
    #c = 0.45 * 0.1428*e**(a*1j)
    #c = -1.476 + 0j
    for i in range(max_iter):
        if abs(z) > threshold:
            return i
        z = z**n + c
    return 0

def generate(w, h, max_iter, n=2.0):
    x = np.linspace(-2, 2, w)
    y = np.linspace(-1.25, 1.25, h)
    pxl = np.zeros((w,h))
    for i in range(w):
        for j in range(h):
            pxl[i][j] = julia(x[i] + 1j*y[j], max_iter, n=n)
    
    return pxl

def generate_animation(w, h, max_iter, v, n):
    x = np.linspace(-2, 2, w)
    y = np.linspace(-1.25, 1.25, h)
    pxl = np.zeros((w,h))
    for i in range(w):
        for j in range(h):
            pxl[i][j] = julia(x[i] + 1j*y[j], max_iter, a=v, n=n)
    
    return pxl

def main():
    m = generate(1000,1000, 512,n=2.0)
    m = m.T #transpose the matrix
    plt.imshow(m,cmap="gnuplot2")
    plt.axis("off")
    plt.savefig("julia_wallpaper.png", dpi=500)
    # for i in range(75):
    #     m = generate_animation(150,150,68, i/12, n=5.0)
    #     m = m.T #transpose the matrix
    #     plt.imshow(m,cmap="hot")
    #     plt.axis("off")
    #     fname = "/home/cb/numerical/mandelbrot/animation/" + str(i) + ".png"
    #     plt.savefig(fname, dpi=350)
    #     print(f"Fractal: {i}/75 Completed")

main()