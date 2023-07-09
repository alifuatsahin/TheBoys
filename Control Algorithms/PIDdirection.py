# Ali Fuat Şahin - ME462 Project - 08/07/2023

import numpy as np
import time

# RGB Frame resolution 1280x800 / FOV 90x65 - MAX
# Depth Frame resolution 1280x720 / FOV 87x58 - MAX

errorDist = 0
errorDir = 0
integralDist = 0
integralDir = 0
Ts = 0.1  # Sampling time
timer = time.time_ns()

while True:
    while abs(errorDist) < 0.5 and abs(errorDir) < 0.5:
        continue # Comment this out after filling inside the while loop
        # Read new input values from the camera

    if time.time_ns() - timer > 100000:
        deflection = 10  # aruco center coordinate reading from the IntelRealsense D455 camera
        depth = 50  # desired distance between the robot and the aruco marker

        crossProduct = (depth / np.sqrt(2) * deflection / 640)
        dotProduct = np.sqrt(depth ** 2 - crossProduct ** 2)

        pErrorDist = errorDist
        pErrorDir = errorDir
        errorDist = dotProduct
        errorDir = crossProduct

        KpDist = 0
        KdDist = 0
        KiDist = 0

        KpDir = 0
        KdDir = 0
        KiDir = 0

        integralDist = integralDist + KiDist * errorDist * Ts
        integralDir = integralDir + KiDir * errorDir * Ts

        speed = KpDist * errorDist + KdDist * (errorDist - pErrorDist) / Ts + integralDist
        speedDif = KpDir * errorDir + KdDir * (errorDir - pErrorDir) / Ts + integralDir

        rSpeed = speed + speedDif
        lSpeed = speed - speedDif

        # Finally read new input values and turn back to the loop
