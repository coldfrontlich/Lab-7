#Помогаев Максим R3142, 2 вариант
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(np.pi * (-2), np.pi * (2))
y = np.sin(x) * np.cos(x)
z = np.sin(x) * np.cos(x)

figure = plt.figure()
ax = figure.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='red')
plt.show()

