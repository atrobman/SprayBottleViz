import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

#variables
r = 25 #spray radius
v = 60 #spray velocity
h = 0 #spray height
a = 90 #spray angle (from table)
g = 9.8 #gravity

#generate input data in a circle with radius r
theta = np.linspace(0, 2*np.pi, 1000)
x_in = r * np.cos(theta)
y_in = r * np.sin(theta)

#perform transformation
y_out = [None] * len(x_in)

for i in range(len(x_in)):
	point_height = y_in[i] + r + h

	#y = .5*g*t^2
	#sqrt(2*y/g)=t
	time_taken = sqrt(2 * point_height / g)

	#x = v * t
	x_landed = v * time_taken

	y_out[i] = x_landed

#plot
plt.plot(x_in, y_out)
plt.xlim(-1.1*r, 1.1*r)
# plt.ylim( 0, 1 + v * sqrt(2 * (2*r+h) / g) )
plt.ylim(min(y_out)-5, min(y_out)+200)
plt.show()
