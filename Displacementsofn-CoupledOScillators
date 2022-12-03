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

#input data:
n = int(input("Enter the number of oscillators"))
w = float(input("Enter a positive number for the angular frequency: note that this is root(k/m) and thus takes into account both the mass and stiffness"))
if w <= 0:
    print("angular frequency has to be a positive number")
    exit
initialpositions = []
for i in range(0,n):
    e = float(input("input the initial displacement of the ith mass"))
    initialpositions.append(e)
x0 = np.array(initialpositions)

#n-coupled code
s = n_coupled(x0, w)
m = []
for i in range(0,n):
    m.append([s[t][i] for t in s])

#plotting
plt.xlabel("Time(arbitrary units)")
plt.ylabel("Position(arbitrary units)")

for i in range(0,n):
    plt.plot(s.keys(), m[i], label = "Mass"+str(i+1))
    
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
plt.tight_layout()
#plt.savefig('fig.png')
