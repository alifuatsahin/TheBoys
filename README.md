# The Boys

This project repo contains the codes and planning of 2 different projects.

- Predator-prey Game Competition
- Unmanned Ground Vehicle Project

Details about each can be found below.

## Table of Contents

- [Installation](#installation)
- [Predator-Prey Game](#ME461)
- [Unmanned Ground Vehicle](#ME462)
- [Contributors](#contributors)

# Installation

The predator-prey game requires a microcontroller (pi pico or any other microcontroller that can be coded with micropython). The unmanned ground vehicle project is coded in Jetson Nano and two Raspberry Pi Picos. In addition to the microcontrollers, the sensors and the setup are needed to run the codes. Setups and robots can be found under the following descriptions.

# Predator-prey Game Competition

This project aims to build a simple robot that will navigate on the grid-based arena collecting points and avoiding risks according to its role in limited time. 


## Meanings of Cell Colors
White: Default color and indicates a neutral cell, which does not result in any points or have any constraints or functionality.

Red: Indicates a wall, no robots can pass through this cell.

Green: This is, the so-called, transformer cell. Once a robot enters this cell, all robots will toggle roles, i.e. predator becomes prey, and the prey becomes predator.

Yellow and Blue: These cells represent different terrains that impose different speeds and points according to each role.

![image](https://github.com/alifuatsahin/TheBoys/assets/123699292/cad642ac-5037-4b41-856b-76156fa010cc)

## Design Constraints

Robot structure and functionality are constrained to have a fair game. During the competition, a robot will be predator or prey, and roles can switch during a game. Details are given below.

Pi Pico W will be the onboard microcontroller. There should be LEDs that can display (at minimum RED and GREEN) at 3 (or more) different locations as shown in Figure 3. The LEDs should not be visible from the top camera but visible from the sides when we watch them move in the Arena. The LEDs will be used for debugging and status indication. During testing or competition stages, LEDs should be green if your robot is a prey, and red if it is a predator. Details are given below.
The ArUco marker assigned to your group is to be the only thing that is visible from the overhead camera that captures and broadcasts arena images and marker locations.
The robot should fit under a CD-ROM, where the diameter of a CD-ROM is 120mm.  If needed wheels can slightly overhang as shown, yet if you can fit the wheels under the footprint of the CD-ROM that is preferable. Robot height is also limited to 120mm.
The robot should be powered up using a power bank. Powerbank capacity is not limited. After all, the higher the capacity, the larger and heavier the power bank!


## Roles of a Robot:
A robot can either be a predator or a prey. According to its role, a robot will have different speed limits within cells that have different colors. Before a competition run, game settings will be published via MQTT. 

## Speed Limits and Moving in the Arena:
The robot is constrained to move at 3 different speeds, i.e. Low, Medium, and High. At first, set them to 45%, 60%, and 90% duty cycle. During the competition, the robots are calibrated so that all robots move at the same speed for each level.
Robots will move using 4-neighbors, i.e. the red path from (1,1) to (5,6) in Figure 1 is not acceptable, yet the green one is. Green is acceptable because it is a 4-path, but obviously  acceptable does not imply best or optimal!

## Point assignment
Entering a cell and visiting a cell have different meanings within our context.
Once your robot enters a cell, it cannot leave this cell without visiting that cell. Visiting a cell means that the distance between the centroid of the marker and the center of the cell should be less then ¼ of one side of a cell, note that cells are square(ish). If any point is assigned to this cell (i.e. it is Blue or Yellow), you will receive the point not when your robot enters the cell, but when it officially visits the cell. 
For a green cell, the transformation will only start after your robot officially visits that cell.

![image](https://github.com/alifuatsahin/TheBoys/assets/123699292/bffcd88e-ab87-424c-9b2e-ff6e85e49681)

# Unmanned Ground Vehicle Project

This project introduces two unmanned ground vehicles which can carry a specified load to a given location. If a larger load is to be carried or there is uneven terrain, two robots can connect and collaborate to carry the given load. The robots are designed such that any sensor or controller can be easily integrated to the system. In our case, we have experimented with a LIDAR and a Stereo camera to carry the load to a specified location from the optimal path by avoiding obstacles.

![image](https://github.com/alifuatsahin/TheBoys/assets/123699292/64569bbd-cbfa-4941-98f4-7ef43bd4ba40)

## Contributors
Ali Fuat Sahin,
Hüsnü Furkan Evci,
Tuna Yel
