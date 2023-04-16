import matplotlib.pyplot as plt
import numpy as np

energies = []
L = 5

n = []
for i in range(1,15):
    n.append(i)
    E = i**2 * np.pi**2/(2 *L**2)
    energies.append(E)


print(n)
y = [2.22, 2.69, 3.28, 8.61, 9.87, 11.87, 13.84, 2.09, 2.42, 2.99, 3.49, 9.11, 10.81, 12.94]
y.sort()
print(y)
plt.scatter(n, y)
plt.scatter(n, energies)
plt.show()

#the difference between the two scatter plots is that the intital graph has no gaps while this one does
