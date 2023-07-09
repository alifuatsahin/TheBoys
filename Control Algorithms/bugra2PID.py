#  Motion planner - ME462 Project - Ali Fuat Şahin - 09/07/2023

import numpy as np
import time

# Robot Parameters
L = 50
R = 9

desiredDistance = 1

prevError = 0  # Initialization
error = 0
integral = 0
v = 0
w = 0
offset = 0.1  # To be tuned
Ts = 0.1 * 10 ** 6  # Sampling time in ns
timer = time.time_ns()

while True:
    while abs(v) < desiredDistance:
        speedL = 0
        speedR = 0
        u2 = 10  # Depth reading from the camera
        u1 = 5  # Deflection reading from the camera
        u = np.transpose(np.matrix([u1, u2]))

        phi = np.arctan2(u2, u1)
        v = np.sqrt(u2 ** 2 + u1 ** 2)

        error = phi

    if time.time_ns() - timer > Ts:
        Kp = 0
        Kd = 0  # Ts included
        Ki = 0  # Ts included

        w = Kp * error + Kd * (error - prevError)
        if error < offset:
            integral = integral + Ki * error
            w += Ki * error

        speedL = (2 * v - w * L) / (2 * R)
        speedR = (2 * v + w * L) / (2 * R)

        u2 = 10  # Depth reading from the camera
        u1 = 5  # Deflection reading from the camera
        u = np.transpose(np.matrix([u1, u2]))

        phi = np.arctan2(u2, u1)
        v = np.sqrt(u2 ** 2 + u1 ** 2)

        error = phi
