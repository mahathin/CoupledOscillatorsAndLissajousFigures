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
def n_coupled(x0, w, dt = 0.01, total_time = 20):
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

w = 1
dt = 0.01
X0 = np.array([1])
output = n_coupled(X0, w)
position = np.array([output[t][0] for t in output.keys()])
velocity = np.delete((np.roll(position, 1)-position)/dt, 0) 
acceleration = np.delete((np.roll(velocity, 1)-velocity)/dt, 0) 

#plotting
plt.plot(list(output.keys())[:], position)
plt.title("Position")
plt.xlabel("Time(arbitrary units)")
plt.ylabel("Position(arbitrary units)")

plt.plot(list(output.keys())[:-1], velocity)
plt.title("Velocity")
plt.xlabel("Time(arbitrary units)")
plt.ylabel("Velocity(arbitrary units)")

plt.plot(list(output.keys())[:-2], acceleration)
plt.title("Acceleration")
plt.xlabel("Time(arbitrary units)")
plt.ylabel("Acceleration(arbitrary units)")

