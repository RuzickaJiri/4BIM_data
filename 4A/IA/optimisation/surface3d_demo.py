# Imports from the matplotlib library
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
# --------------------------------------

"""
# Definition of what to plot

fig = plt.figure() # opens a figure environment
ax = fig.gca(projection='3d') # to perform a 3D plot
X = np.arange(-2, 2, 0.25) # x range
Y = np.arange(-2, 2, 0.25) # y range
X, Y = np.meshgrid(X, Y) # creates a rectangular grid on which to plot the function values (Z)
Z= 2*X**3 + 2*Y**3 + X**2*Y + X*Y**2 - 9*X - 9*Y # defines the function values
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False)  # plot definition and options

# Runs the plot command
plt.show()
"""


# TD1

# 1
fig = plt.figure() # opens a figure environment
ax = fig.gca(projection='3d') # to perform a 3D plot
x = np.arange(-2, 2, 0.25)  # x range
y = np.arange(-2, 2, 0.25)  # y range
x, y = np.meshgrid(x, y)
z = (x-y)**4 +2*x**2 + y**2 - x + 2
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, linewidth=0, antialiased=False)  # plot definition and options
plt.show()
# la première question est qualitative, on voit que le minimum global se situe au point (0,0)
# la fonction est positive et donc elle atteint son minimum quand elle s'annule

# 2
# calcul du gradient

# 3



