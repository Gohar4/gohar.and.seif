#Import modules
from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor,LandmarkMap
from math import pi, atan2
import matplotlib.pyplot as plt
import numpy as np
import sympy

#Create object of the vehicle
anim = VehicleIcon('robot1.png', scale = 3)
#user inputs the initial positon of the robot
Xcoordinate = int(input("Enter the X coordinate for the robot's initial position: "))
Ycoordinate = int(input("Enter the Y coordinate for the robot's initial position: "))
start=initialPos=[Xcoordinate, Ycoordinate]
#setting dimension of map, controlling vehicle postion, and setting initial position
veh = Bicycle(
    animation = anim,
    control = RandomPath,
    dim = 20,
    x0=(initialPos[0],initialPos[1],0),
)
#plot map obstacles and goal
veh.init(plot=True)
obs = int(input("Enter the number of obstacles: "))
map = LandmarkMap(obs, 20)
Xtarget = int(input("Please enter initial X coordinate for goal: "))
Ytarget = int(input("Please enter initial Y coordinate for goal: "))
goal = [Xtarget, Ytarget]
#desgin and plotting the goal marker 
goal_marker_style = {
    'marker': 'D',
    'markersize': 6,
    'color': 'g',
}
plt.plot(goal[0], goal[1], **goal_marker_style)
map.plot()
#range bearing sensor added
sensor=RangeBearingSensor(robot=veh,map=map, animate=True)
for i in sensor.h(veh.x):
    dis_land = i[0]
    ang_land = i[1]

# inserting goal inside array(append)
goal_array=[goal]
goal_array.append(goal)
goal_array.insert(0,initialPos)
x_array=[item[0] for item in goal_array]
y_array=[item[1] for item in goal_array]

opi = pi/4
#loop that allows robot to move if certain condions are not exceeded while avoding obstacles
run=True
target=[goal_array]
while(run): #while loop stops when target is reached
    for i in sensor.h(veh.x):
        if (i[0] > 0.5) and (abs(i[1]) > opi):
            veh.step(1,steer)
            steer = goal_heading-veh.x[2]
            plt.pause(0.005)
        else:
            veh.step(-1,0) 
            plt.pause(0.005)
        veh._animation.update(veh.x) #updates vehicle animation as it moves
#plot vehicle and target 
plt.plot(goal[0], goal[1], **goal_marker_style)