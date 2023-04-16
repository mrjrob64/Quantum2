import numpy as np
import matplotlib.pyplot as plt

energies = []
x = []

L = 5
print("HI")
for n in range(1,15):
    E = n**2 * np.pi**2/(2 *L**2)
    energies.append(E)
    x.append(n)
    print(E)

#The first energies are close but get further as they go on

#These are first 14 energy levels from the last part
y = [0.38, 1.48, 3.32, 5.88, 9.15, 13.1, 17.62, 0.1, 0.84, 2.31, 4.51, 7.43, 11.05, 15.3]
y.sort()

plt.scatter(x, energies, label='single well')
plt.scatter(x, y, label='multiple wells')
plt.legend(loc='upper left')

plt.show()

plt.savefig("scatter_plot_1.png")