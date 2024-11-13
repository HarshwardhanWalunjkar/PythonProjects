import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        z = z*z + c
        if abs(z)>2:
            return n
    return max_iter

def mandelbrot_set(x_min,x_max,y_min,y_max,width,height,max_iter):
    x = np.linspace(x_min,x_max,width)
    y = np.linspace(y_min,y_max,height)
    mset = np.zeros((height,width))
    for i in range(width):
        for j in range(height):
            c = complex(x[i],y[j])
            mset[j,i] = mandelbrot(c,max_iter)
    return mset


x_min = -2.0
x_max = 1.0
y_min = -1.5
y_max = 1.5
width = 10000
height = 10000
max_iter = 200

mandelbrot_image = mandelbrot_set(x_min,x_max,y_min,y_max,width,height,max_iter)
plt.imshow(mandelbrot_image,extent=[x_min,x_max,y_min,y_max],cmap='seismic')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.show()

