# Most basic control package - ME462 Project - Ali Fuat Sahin - 08/07/2023

import numpy as np
import time

dirOffset = 10  # To be changed after camera readings
distOffset = 50  # To be determined according to user

depth = 0
deflection = 0

Ks = 50  # Speed constant
Kr = 100  # Rotation constant

timer = time.time_ns()
Ts = 100000


def move(speed, depth, dirOffset):  # Message sending commands will be added inside these functions
    rSpeed = np.sign(depth - dirOffset) * speed
    lSpeed = np.sign(depth - dirOffset) * speed
    return lSpeed, rSpeed


def turn(speed, deflection):
    rSpeed = -np.sign(deflection) * speed
    lSpeed = np.sign(deflection) * speed
    return lSpeed, rSpeed


while True:
    while abs(deflection) < dirOffset and abs(depth) < distOffset:
        continue
        # Read camera output

    if time.time_ns() - timer > Ts:
        deflection = 5  # Camera readings
        depth = 50
        speed = np.sqrt(Ks * (depth - distOffset) ** 2 + Kr * (deflection - dirOffset) ** 2)
        if abs(deflection) > dirOffset:
            lSpeed, rSpeed = turn(speed, deflection)
        elif abs(depth) > distOffset:
            lSpeed, rSpeed = move(speed, depth, dirOffset)
        else:
            pass
