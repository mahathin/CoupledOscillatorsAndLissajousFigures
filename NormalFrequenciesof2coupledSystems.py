#necessary modules
import numpy as np

#inputdata
m = float(input("Enter a positive number for the mass"))
k = float(input("Enter a positive number for the stiffness"))

for w in np.arange(-100, 100, 0.01):
    mat = np.array([[(-m*(w**2)+(2*k)),-k],[-k, (-m*(w**2)+(2*k))]])
    if -0.01 <= np.linalg.det(mat) <= 0.01:
        print(mat)
        print(w, np.linalg.det(mat))

