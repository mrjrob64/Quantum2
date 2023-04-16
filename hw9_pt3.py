import numpy as np

import matplotlib.pyplot as plt

deltax = 0.001
E = 0
U0 = 20
length = 5
m = 1
hbar = 1
final_values_even = []
final_values_odd = []
allowed_energies = []

def sw(x, X, B):
    return (B+1)/2 + np.sign(.25 - (X-x)**2) * (B-1)/2

def U(x):
    return U0*sw(x,0,0)*sw(x,1.2,0)*sw(x,2.4,0)*sw(x,3.6,0)*sw(x,-1.2,0)*sw(x,-2.4,0)*sw(x,-3.6,0)


x = []
for i in range(int(length/deltax)):
    x.append(i*deltax)

#for i in range(0, len(y)):
#    y[i] = U(i*deltax)

deltaE = 0.01

print("hi")

for i in range(int(20/(deltaE))):
    E  = E + deltaE
    y = []
    for i in range(len(x)):
        y.append(0)
    y[1] = 1
    
    for i in range(1, len(y)-1):
        y[i+1] = 2*y[i] - y[i-1] + (deltax**2)*(2*m/(hbar**2))*(U(x[i]) - E)*y[i]
    print("E :" + str(E) + " Value: " +str(y[len(y)-1]))
    final_values_odd.append(y[len(y)-1])
    if len(final_values_odd) > 1:
        if final_values_odd[len(final_values_odd)-1]*final_values_odd[len(final_values_odd)-2] < 0:
            allowed_energies.append(E)
    
E = 0
for i in range(int(20/(deltaE))):
    E  = E + deltaE
    y = []
    for i in range(len(x)):
        y.append(0)
    y[0] = 1
    y[1] = 1
    
    for i in range(1, len(y)-1):
        y[i+1] = 2*y[i] - y[i-1] + (deltax**2)*(2*m/(hbar**2))*(U(x[i]) - E)*y[i]
    print("E :" + str(E) + " Value: " +str(y[len(y)-1]))
    final_values_even.append(y[len(y)-1])
    if len(final_values_even) > 2:
        if final_values_even[len(final_values_even)-1]*final_values_even[len(final_values_even)-2] < 0:
            allowed_energies.append(E)
    

print(allowed_energies)
#[2.2199999999999966, 2.6899999999999866, 3.279999999999974, 8.60999999999986, 9.869999999999834, 11.869999999999791, 13.83999999999975, 2.0899999999999994, 2.4199999999999924, 2.9899999999999802, 3.4899999999999696, 9.10999999999985, 10.809999999999814, 12.939999999999769, 20.000000000000327]
#this was first 15 so just minus the 20 value