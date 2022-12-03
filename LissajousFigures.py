#importing necessary modules
import numpy as np
import matplotlib.pyplot as plt

#definitions
#DEFINITION 1: generating an n by n symmetric matrix with diagonal elements = -2, the neighbouring elements = 1
def matrix(n):
        Matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if i == j:
                    Matrix[i,j] = -2
                    if i != 0:
                        Matrix[i-1,j] = 1
                    if i != n-1:
                        Matrix[i+1,j] = 1
        return Matrix

#DEFINITION 2: updating matrix
def n_coupled(x0, w, dt = 0.01, total_time = 10):
    positionoutput = {} 
    V = np.zeros(len(x0), dtype='float64')
    Matrix = matrix(len(x0)).astype('float64')
    X = x0.astype('float64')
    for t in np.arange(0,total_time+dt,dt):
        A = np.matmul(w*Matrix,X) #equation of motion
        V += A*dt #updating position and velocity
        X += V*dt
        positionoutput[t] = np.copy(X)
    return positionoutput

#input data
X0 = float(input("input the initial displacement of the mass in X direction"))
Y0 = float(input("input the initial displacement of the mass in Y direction"))
w1 = float(input("input the angular frequency of springs along X direction"))
w2 = float(input("input the angular frequency of springs along Y direction"))

x0 = np.array([X0])
y0 = np.array([Y0])

dt = 0.01
results_x = n_coupled(x0, w1)
results_y = n_coupled(y0, w2)

plt.plot(results_x.values(), results_y.values())
plt.xlabel("x-position (arbitrary units)")
plt.ylabel("y-position (arbitrary units)")
plt.title("Lissajous Figures")

