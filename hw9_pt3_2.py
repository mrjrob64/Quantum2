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
p = [0.38, 1.48, 3.32, 5.88, 9.15, 13.1, 17.62, 0.1, 0.84, 2.31, 4.51, 7.43, 11.05, 15.3]
y.sort()
p.sort()
print(y)
plt.scatter(n, y)
plt.scatter(n, energies)
plt.scatter(n, p)
plt.show()

#the difference between the two scatter plots is that the intital graph has no gaps while this one does
