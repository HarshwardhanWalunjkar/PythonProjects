import numpy as np
import matplotlib.pyplot as plt
import tempfile
from pydub import AudioSegment
from pydub.playback import play
from pydub.playback import _play_with_simpleaudio as play_audio
#import the sound file
sound = AudioSegment.from_file("do.mp3")

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
    print("x: {}, y: {}".format(event.xdata, event.ydata))
    c_0 = complex(event.xdata, event.ydata)
    z = 0
    pitch_increment = 0.1
    
    x_values = []
    y_values = []
    
    for n in range(max_iter):
        z_prev = z
        z = z * z + c_0
        x_values.append(z_prev.real)
        y_values.append(z_prev.imag)
        if abs(z) <= 2:
            if len(x_values) >= 2 and len(y_values) >= 2:
                # Draw the line connecting the previous and current points
                plt.plot([x_values[-2], z.real], [y_values[-2], z.imag], color="white", linewidth=0.4)
            # calculate the line length
            line_length = np.sqrt((x_values[-1] - z.real) ** 2 + (y_values[-1] - z.imag) ** 2)
            # map the line length to an octave change the divider to change the type of sound
            octaves = line_length / 10
            # convert the octave to a chromatic scale
            note = int(line_length * 12) % 12
            # Adjust the pitch according to the note
            new_sample_rate = int(sound.frame_rate * (2 ** (note / 12)))
            # alter the original sound changing its sample rate its pitch
            altered_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
            # Convert altered sound to a standard sample rate
            standard_sample_rate = 22050  # You can adjust this value as needed
            altered_sound = altered_sound.set_frame_rate(standard_sample_rate)
            # Play the altered sound
            play_audio(altered_sound)
            
    plt.show()

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