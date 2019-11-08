import matplotlib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import physics as ph

startx = 0
starty = 0

power = int(input("enter the power of the launch in joules: "))
angle = int(input("enter the angle of the launch"))
movement_time = ph.maxtime(angle)
path_angle = ph.findangle(power, angle)
launch_power = ph.findpower(power, path_angle, movement_time)
maxalt = ph.maxalt(launch_power,angle)
t = np.arange(0, maxalt, 10)
fig, ax = plt.subplots()
graph = ph.ballpath(startx, starty, launch_power, path_angle, movement_time)
ax.plot(t, graph)
print(maxalt)
ax.set(xlabel='x', ylabel='y',
       title='your launch graph')
ax.grid()
plt.show()

