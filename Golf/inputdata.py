import matplotlib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import physics as ph

startx = 0
starty = 0

v0 = int(input("enter the muzzle speed of the projectile: "))
angle = int(input("enter the angle of the launch: "))

movement_time = ph.maxtime(angle)
path_angle = ph.findangle(v0, angle)
linear_speed = ph.linearspeed(v0, path_angle, movement_time)
maxalt = ph.maxalt(linear_speed, angle)
graph = ph.ballpath(startx, starty, linear_speed, path_angle, movement_time)


t = np.arange(0.0, maxalt)
fig, ax = plt.subplots()
ax.plot(t.shape, graph)

ax.set(xlabel='x', ylabel='y',
       title='your launch graph')

ax.grid()
plt.show()

