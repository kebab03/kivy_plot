#garden.matplotlib  è chiamato  kmplot
#kivy with matplotlib for android #kivy,#python
# di Sk Sahil



from kmplot.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import numpy as np

from mpl_toolkits.mplot3d import Axes3D

# Axes30 import has side effects, it enables using projection='3d' in add_subplot
import matplotlib.pyplot as plt

import random

def fun(x, y):
    return x**2 + y

fig = plt.figure()

ax = fig.add_subplot( 111, projection="3d")
x = y = np.arange(-3.0,3.0, 0.05)

X, Y = np.meshgrid(x,y)

zs = np.array(fun(np.ravel(X), np.ravel(Y)))
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")
class MyApp( App):
    def build(setf):
        box=BoxLayout()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return box
MyApp().run()