#Помогаев Максим R3142, 2 вариант
import numpy as np
import matplotlib.pyplot as plt

array = np.genfromtxt('data2.csv', delimiter=',', names=True)
ph = array['ph']
np.float_(ph)

plt.hist(ph, edgecolor = 'k', bins=20)
plt.title('Histogram')
plt.xlabel('ph')
plt.ylabel('frequency')
plt.show() 

plt.hist(ph, edgecolor = 'k', bins=20, density=True)
plt.title('Normalize Histogram')
plt.xlabel('ph')
plt.ylabel('frequency')
plt.show() 

print(np.nanstd(ph))
