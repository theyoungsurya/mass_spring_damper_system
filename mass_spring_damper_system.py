import numpy as np
import matplotlib.pyplot as plt

class body(object):
    def __init__(self,m=5.0,k=8.0,c=0.08):
        self.mass = float(m)
        self.stiffness_spring = float(k)
        self.damp_coeff = float(c)
    def rk4(self,x, v, a, dt,F):
        """Returns final (position, velocity) tuple after
        time dt has passed.

        x: initial position (number-like object)
        v: initial velocity (number-like object)
        a: acceleration function a(x,v,dt) (must be callable)
        dt: timestep (number)"""
        x1 = x
        v1 = v
        a1 = a(x1, v1, 0 , F)

        x2 = x + 0.5*v1*dt
        v2 = v + 0.5*a1*dt
        a2 = a(x2, v2, dt/2.0 , F)

        x3 = x + 0.5*v2*dt
        v3 = v + 0.5*a2*dt
        a3 = a(x3, v3, dt/2.0 , F)

        x4 = x + v3*dt
        v4 = v + a3*dt
        a4 = a(x4, v4, dt , F)

        xf = x + (dt/6.0)*(v1 + 2*v2 + 2*v3 + v4)
        vf = v + (dt/6.0)*(a1 + 2*a2 + 2*a3 + a4)

        return xf, vf
    def a(self,x, v, dt,F):
        k = self.stiffness_spring
        c = self.damp_coeff
        m = self.mass
        return (F-k*x-c*v)/m
    def cal_pos_n_vel(self,t,dt,x0,v0,F=0.0):
        nsteps = int(float(t)/dt)
        time =np.zeros(nsteps)
        displacement = np.zeros(nsteps)
        velocity = np.zeros(nsteps)
        displacement[0] = 0.0
        velocity[0] = 1.0
        for i in range(1,nsteps):
            displacement[i],velocity[i] = self.rk4(displacement[i-1],velocity[i-1],self.a,dt,F)
            time[i] = time[i-1] + dt
        return time, displacement , velocity
    def plots(self,t,dt,x0,v0,F,save=False):
        time, displacement , velocity = self.cal_pos_n_vel(t,dt,x0,v0,F)
        plt.figure()
        plt.plot(time,displacement)
        plt.plot(time,velocity)
        if(save):
            plt.savefig("../output/Disp&Vel_vs_time.png")
        

        

        
        
