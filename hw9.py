import numpy as np

import matplotlib.pyplot as plt
#what is the differe
deltax = 0.001
E = 0
U0 = 20
length = 5
m = 1
hbar = 1
final_values = []
allowed_energies = []

def sw(x, X, B):
    return (B+1)/2 + np.sign(.25 - (X-x)**2) * (B-1)/2

def U(x):
    return U0*sw(x,0,0)*sw(x,1,0)*sw(x,2,0)*sw(x,3,0)*sw(x,-1,0)*sw(x,-2,0)*sw(x,-3,0)

#how do I turn a float into an int?


y = []
for i in range(int(length/deltax)):
    y.append(0)

x = []
for i in range(len(y)):
    x.append(i*deltax)

y[0] = 1

#for i in range(0, len(y)):
#    y[i] = U(i*deltax)

deltaE = 0.01

for i in range(int(20/(deltaE * 5))):
    E = E + deltaE
    for i in range(1, len(y)-1):
        y[i+1] = 2*y[i] - y[i-1] + (deltax**2)*(2*m/(hbar**2))*(U(x[i]) - E)*y[i]
    print("E :" + str(E) + " Value: " +str(y[len(y)-1]))
    final_values.append(y[len(y)-1])
    if len(final_values) > 1:
        if final_values[len(final_values)-1]*final_values[len(final_values)-2] < 0:
            allowed_energies.append(E)
    y = []
    for i in range(int(length/deltax)):
        y.append(0)
    y[0] = 1

print(allowed_energies)

#plot the graph
#plt.plot(x,y)

#show the graph
#plt.show()

#save the graph
#plt.savefig("hw9.png")

#close the graph
#plt.close()
