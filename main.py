import mass_spring_damper_system as msds
import os
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np

with open(os.path.join(".", "input.csv"), 'r') as f:
    inputfile = csv.reader(f, delimiter=",")
    next(inputfile)
    input_data = next(inputfile)
    m, k, c, t, dt, x0, v0, F = [float(str.strip(i)) for i in input_data]
mass = msds.body(m,k,c)
mass.plots(t, dt, x0, v0, F,True)
time, displacement, velocity = mass.cal_pos_n_vel(t, dt, x0, v0)
fig = plt.figure(0)
ax1 = plt.axes(xlim=(-5, 5), ylim=(-5, 5))
line = ax1.plot([], [])[0]
def get_mass(length):
    x= np.linspace(0.0,length+3.0)
    y= np.ones(len(x))
    return x,y
    

def animate(i):
    """ Function that is called at each iteration of the animation.
    Sets the current position of the line
    """
    x,y = get_mass(displacement[i])
    line.set_data(x,y)
    return line,
def init():
    """initialize animation"""
    line.set_data([], [])
    return line,
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(time), blit=True,
                               interval=dt)
if not os.path.exists('../output'):
    os.mkdir('../output')

anim.save('../output/vanderpol_animation.mp4', fps=30,
          extra_args=['-vcodec', 'libx264'])

