import numpy as np
import matplotlib.pyplot as plt


def z_fuction(x,y):
    return np.sin(5*x)*np.cos(5*y)/5
def calcuate_derivative(x,y):
    return np.cos(5*x)*np.cos(5*y), -np.sin(5*x) *np.sin(5*y)
def calcuate_gradient(x,y):
    return  np.cos(5*x)*np.cos(5*y),-np.sin(5*x)*np.sin(5*y)

x=np.arange(-1,1,0.05)
y=np.arange(-1,1,0.05)

X,Y=np.meshgrid(x,y)

Z=z_fuction(X,Y)


current_pos=(0.7,0.4,z_fuction(0.7,0.4))

lr=0.01

ax=plt.subplot(projection='3d',computed_zorder=False)
for _ in range(1000):
  X_derivative,Y_derivative=calcuate_gradient(current_pos[0],current_pos[1])
  X_new,Y_new=current_pos[0]-lr*X_derivative, current_pos[1]-lr*Y_derivative
  current_pos=(X_new,Y_new,z_fuction(X_new,Y_new))

  ax.plot_surface(X,Y,Z, cmap='viridis',zorder=0)
  ax.scatter(current_pos[0],current_pos[1],current_pos[2],color='magenta',zorder=1)
  plt.pause(0.001)
  ax.clear()