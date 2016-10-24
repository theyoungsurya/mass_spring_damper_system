import csv
import mass_spring_damper_system as msds
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import os


with open(os.path.join(".", "input.csv"), 'r') as f:
    inputfile = csv.reader(f, delimiter=",")
    next(inputfile)
    input_data = next(inputfile)
    m, k, c, t, dt, x0, v0, F = [float(str.strip(i)) for i in input_data]
if not os.path.exists('../output'):
    os.mkdir('../output')
mass = msds.body(m,k,c)
mass.plots(t, dt, x0, v0, F,True)
time, displacement, velocity = mass.cal_pos_n_vel(t, dt, x0, v0)
fig = plt.figure(0)
ax1 = plt.axes(xlim=(0.0, 10), ylim=(-5, 5))
ax1.set_title('Animation of a horizontal Mass-Spring-Damper-System')
ax1.set_xlabel('Ground')
ax1.set_ylabel('Wall')
line = ax1.plot([], [])[0]
wall2 = ax1.plot([],[])[0]
xwall2 = np.linspace(0.0,10.0)
ywall2 = np.ones(len(xwall2))*(-0.5) 
pts = [[0,0],[0,0],[0,0],[0,0]]
patch = plt.Polygon(pts)
ax1.add_patch(patch)
def get_mass(length):
    x= np.linspace(0.0,length+3.0)
    y= np.zeros(len(x))
    return x,y
    

def animate(i):
    """ Function that is called at each iteration of the animation.
    Sets the current position of the line
    """
    x,y = get_mass(displacement[i])
    line.set_data(x,y)
    wall2.set_data(xwall2,ywall2)
    patch.set_xy([[x[-1],y[-1]-0.5],[x[-1],y[-1]+0.5],[x[-1]+1.0,y[-1]+0.5],[x[-1]+1.0,y[-1]-0.5]])
    return line,patch,wall2
def init():
    """initialize animation"""
    line.set_data([], [])
    return line,
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(time), blit=True,
                               interval=dt)

if not os.path.exists('../output'):
    os.mkdir('../output')
anim.save('../output/Mass-Spring-Animation.mp4', fps=30,
          extra_args=['-vcodec', 'libx264'])

