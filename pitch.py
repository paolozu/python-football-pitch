#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 19:38:43 2023

@author: paolozu
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Arc

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

#Pitch Outline
plt.plot([0,0],[0,90], color="black")
plt.plot([0,130],[90,90], color="black")
plt.plot([130,130],[90,0], color="black")
plt.plot([130,0],[0,0], color="black")

# Center line, circle and spot
plt.plot([65,65],[0,90], color="black")
centreSpot = plt.Circle((65,45),0.8,color="black")
centreCircle = plt.Circle((65,45),9.15,color="black",fill=False)


#Left Penalty Area
plt.plot([16.5,16.5],[65,25],color="black")
plt.plot([0,16.5],[65,65],color="black")
plt.plot([16.5,0],[25,25],color="black")

plt.plot([0,5.5],[54,54],color="black")
plt.plot([5.5,5.5],[54,36],color="black")
plt.plot([5.5,0.5],[36,36],color="black")

leftArc = Arc((11,45),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="black")
leftPenSpot = plt.Circle((11,45),0.8,color="black")


# Right penality area
plt.plot([130,113.5],[65,65],color="black")
plt.plot([113.5,113.5],[65,25],color="black")
plt.plot([113.5,130],[25,25],color="black")

plt.plot([130,124.5],[54,54],color="black")
plt.plot([124.5,124.5],[54,36],color="black")
plt.plot([124.5,130],[36,36],color="black")

rightArc = Arc((119,45), height=18.3, width=18.3, angle=0, theta1=130, theta2=230, color="black")
rightPenSpot = plt.Circle((119,45),0.8,color="black")

ax.add_patch(centreSpot)
ax.add_patch(centreCircle)
ax.add_patch(leftArc)
ax.add_patch(rightArc)
ax.add_patch(leftPenSpot)
ax.add_patch(rightPenSpot)

plt.axis('off')
plt.show()
