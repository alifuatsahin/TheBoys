# mpcController - ME462 Project - Ali Fuat Sahin - 08/07/2023

from scipy import linalg
import numpy as np

# Initial Conditions
x1 = 10
x2 = 10
x3 = np.pi / 12

v = 0.1
w = 0.1

# Parameters
Ts = 0.1  # Sampling time

# Linearized continuous time kinematic model of the robot
Ac = np.matrix([[0, 0, -v * np.cos(x3)], [0, 0, v * np.cos(x3)], [0, 0, 0]])
Bc = np.matrix([[np.cos(x3), 0], [np.sin(x3), 0], [0, 1]])
Cc = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# Dc -> 3x2 zeros

# Discrete model of path tracking algorithm
A = np.identity(3) + Ac * Ts
B = Ts * Bc
C = Cc

# Weighting Matrices
Q = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 10]])  # State weights
R = np.matrix([[1, 0], [0, 1]])  # Input weights

Pinf = linalg.solve_discrete_are(A, B, Q, R)
Kinf = -linalg.inv(R + np.transpose(B)*Pinf*B)*np.transpose(B)*Pinf*A
