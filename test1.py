mport numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
 
fig, ax = plt.subplots()
 
 
class Pendulum(object):
    def __init__(self, length=1, init_angle=30, tf=10, dt=0.05):
        self.length = length
        self.init_angle = init_angle*np.pi/180
        self.dt = dt
        self.t = np.arange(0, tf+dt, dt)
 
        Z0 = np.array([self.init_angle, 0])
 
        self.Z = odeint(self.odefun, Z0, self.t, args=(9.81/length,))
 
    def odefun(self, Z, t, k):
        dZdt = np.zeros(2)
        dZdt[0] = Z[1]
        dZdt[1] = -k * np.sin(Z[0])
        return dZdt
 
 
pend = Pendulum()
l = pend.length
 
ax.set(xlim=[-l-0.5, l+0.5], ylim=[-l-0.5, l+0.5])
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='--')
 
line, = ax.plot([], [], color='b', linewidth=2)
obj, = ax.plot([], [], 'bo')
time_text = ax.text(-l-0.2, -l-0.2, '')
 
 
def animate(i):
    theta = pend.Z[i, 0]
    x = l*np.sin(theta)
    y = -l*np.cos(theta)
    line.set_data([0, x], [0, y])
    obj.set_data([x], [y])
    time_text.set_text('time = {:.1f}'.format(pend.t[i]))
    return line, obj, time_text
 
 
anim = FuncAnimation(fig, animate,
                     frames=len(pend.Z), interval=int(pend.dt*1000),
                     blit=True)
