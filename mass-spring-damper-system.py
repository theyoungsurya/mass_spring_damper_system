import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def f(st,t):
    F=500
    c=0.9
    k=50.0
    m=2.0
    x=st[0]
    y=st[1]
    acc = (F-(c*y)-(k*x))/m
    return [y,acc]
st0 = [1.0,1.0]
t = np.arange(0.0, 10.0, 0.1)
st = odeint(f,st0,t)
plt.plot(t,st)
