# Last simplest version of the motion planner - ME462 Project - Ali Fuat Şahin - 09/07/2023

import numpy as np
import time

# Robot Parameters
L = 50
R = 9

# Control Parameters
l = 10  # To be optimized
offset = 0.5  # To be optimized
Ts = 0.1 * 10 ** 6  # Sampling time in ns

timer = time.time_ns()

while True:
    if time.time_ns() > Ts:
        u2 = 10  # Depth reading from the camera
        u1 = 5  # Deflection reading from the camera
        u = np.transpose(np.matrix([u1, u2]))

        phi = np.arctan2(u2, u1)
        # v = np.sqrt(u2 ** 2 + u1 ** 2)

        Rot = np.matrix([[np.cos(-phi), -np.sin(-phi)], [np.sin(-phi), np.cos(-phi)]])

        [v, w] = np.matrix([[1, 0], [0, l]]) * Rot * u

        if v < offset:
            speedL = 0
            speedR = 0
        else:
            speedL = (2*v - w*L)/(2*R)
            speedR = (2*v + w*L)/(2*R)