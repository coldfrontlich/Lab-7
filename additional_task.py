import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

figure = plt.figure()
l, = plt.plot([], [], 'k')

plt.xlim(-10, 10)
plt.ylim(-3, 3)

writer = PillowWriter(fps=30)

xlist = []
ylist = []

with writer.saving(figure, "sin.gif", 100):
    for xval in np.linspace(-10, 10, 100):
        xlist.append(xval)
        ylist.append(np.sin(xval))
        l.set_data(xlist,ylist)
        writer.grab_frame()