import numpy as np
import matplotlib.pyplot as plt
from pydub.generators import Sine
from pydub.playback import play
import threading

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
def mouse_click(event):
    print("x: {},y: {}".format(event.xdata,event.ydata))
    c_0 = complex(event.xdata,event.ydata)
    period = get_period(c_0,max_iter)
    sound = generate_harmonic_sound(period)
    threading.Thread(target=play_sound,args=(sound,)).start()
    print(period)
    z=0
    for n in range(max_iter):
        z_prev = z
        z = z*z + c_0
        x_values = [z_prev.real,z.real]
        y_values = [z_prev.imag,z.imag]
        if abs(z)<=2:
            plt.plot(x_values,y_values,color="white",linewidth=0.4)
    plt.draw()

def play_sound(sound):
    play(sound)

def get_period(c,max_iter):
    z = 0
    set_mandelbrot = []
    for n in range(max_iter):
        if z in set_mandelbrot:
            return n
        set_mandelbrot.append(z)
        z=z*z+c
    return max_iter
# Define the harmonic sound function
def generate_harmonic_sound(period):
    # Define base frequency (adjust as needed)
    base_frequency = 440  # A4 note

    # Calculate frequency multiplier based on period
    frequency_multiplier = 2 ** (period/12)

    # Calculate duration (adjust as needed)
    duration = 100000  # milliseconds

    # Generate the harmonic sound
    sound = Sine(base_frequency * frequency_multiplier).to_audio_segment(duration=duration)

    return sound

x_min = -2.0
x_max = 1.0
y_min = -1.5
y_max = 1.5
width = 1000
height = 1000
max_iter = 100

mandelbrot_image = mandelbrot_set(x_min,x_max,y_min,y_max,width,height,max_iter)
fig = plt.figure()
cid = fig.canvas.mpl_connect('button_press_event',mouse_click)
plt.imshow(mandelbrot_image,extent=[x_min,x_max,y_min,y_max],cmap='seismic')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.show() 
input("Press Enter to close the plot window...")