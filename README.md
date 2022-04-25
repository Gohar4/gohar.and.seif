## Mohamed Gohar202000317 and Seif Salama 202000190
## A robot that maneuvers past and detects obstacles

# Main Code
###### Required Softwares
ubuntu
python(3.6 or above)
robotics toolbox
virtual studio code

###### Modules Required 
  from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor,LandmarkMap
*add 2D visuals, enable animation, contol of vehicle movment across grid, obstacles, and sensor*
  from math import pi, atan2
 *all math modules*
  import matplotlib.pyplot as plt
  import numpy as np
  import sympy
*plotting added and other math modules*

###### User Inputs
Xcoordinate = int(input("Enter the X coordinate for the robot's initial position: "))
Ycoordinate = int(input("Enter the Y coordinate for the robot's initial position: "))
obs = int(input("Enter the number of obstacles: "))
Xtarget = int(input("Please enter initial X coordinate for goal: "))
Ytarget = int(input("Please enter initial Y coordinate for goal: "))
*user chooses start and target coordinates as well as number of obstacles*

###### Desgin setting locations
anim = VehicleIcon('robot1.png', scale = 3)
*vehicle png chosen and size*
veh = Bicycle(
    animation = anim,
    control = RandomPath,
    dim = 20,
    *map size*
    x0=(initialPos[0],initialPos[1],0),
)
*initlal positon and controlling vehicle movment*
goal_marker_style = {
    'marker': 'D',
    'markersize': 6,
    'color': 'g',
}
*marker size, color, and shape*
