#Built-in / Standard Library Geometry (Used for complex-number geometry in 2D.)
'''import cmath
p = 3 + 4j
print(abs(p))      # distance from origin
print(cmath.phase(p))  # angle'''
'''Useful for:
Rotations
Polar coordinates
Vector-like operations'''


#math Module (Basic Geometry)
'''
import math
print(math.dist((0,0), (3,4)))  # distance
print(math.hypot(3,4))          # hypotenuse'''
#Useful functions:dist()hypot()sin()cos()tan()radians()degrees()



#turtle Graphics Geometry (Great for learning geometry visually.)
'''import turtle
t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.right(90)
turtle.done()
print(t)'''
#Can draw: Lines Polygons Curves Spirals Fractals


#tkinter.Canvas  (2D geometry drawing system.)
'''from tkinter import *
root = Tk()
c = Canvas(root, width=400, height=400)
c.pack()
c.create_line(0,0,200,200)
c.create_rectangle(50,50,150,150)
c.create_oval(100,100,200,200)
root.mainloop()'''
#Shapes: Line Rectangle Polygon Arc  Circle/Oval

#NumPy Geometry Arrays (Excellent for vectors, matrices, transformations.)
'''import numpy as np
p1 = np.array([1,2])
p2 = np.array([4,6])
distance = np.linalg.norm(p2 - p1)
print(distance)'''
#Useful for:Vector geometry Transformations Rotations Linear algebra 3D math

#Matplotlib Geometry
'''import matplotlib.pyplot as plt
x = [0,1,2]
y = [0,1,0]
plt.plot(x,y)
plt.show()'''

#Geometry Patches
'''from matplotlib.patches import Circle
fig, ax = plt.subplots()
circle = Circle((0.5,0.5), 0.2)
ax.add_patch(circle)
plt.show()'''
#Classes:Circle Rectangle Polygon Ellipse Arc

#Shapely (Professional Geometry Library) (One of the BEST libraries for computational geometry.)
#Install:pip install shapely
'''Geometry Classes
Class	              Description
Point	              Single point
LineString	          Connected line
Polygon	              Polygon shape
MultiPoint	          Multiple points
MultiLineString	      Multiple lines
MultiPolygon	      Multiple polygons
GeometryCollection	  Mixed geometries'''
'''from shapely.geometry import Point, LineString, Polygon
p = Point(1, 2)
line = LineString([(0,0), (1,1), (2,2)])
poly = Polygon([(0,0), (1,0), (1,1), (0,1)])
print(poly.area)
print(poly.length)'''
#Advanced Features:Intersection, Union, Buffer, Convex hull ,Distance, Spatial predicates

#.SymPy Geometry (Symbolic geometry mathematics.)

#Install:pip install sympy
'''Geometry     Classes
Class	     Description
Point	      Point
Line	     Infinite line
Segment	     Line segment
Ray	          Ray
Circle	      Circle
Ellipse	      Ellipse
Polygon	      Polygon
Triangle	  Triangle
RegularPolygon	Regular polygon
Plane	        3D plane'''
'''from sympy.geometry import *
p1 = Point(0,0)
p2 = Point(3,4)
line = Line(p1, p2)
print(line.length)'''
#Great for:Exact geometry,Algebraic geometry,Symbolic calculations

#OpenCV Geometry (Computer vision geometry.)
#Install:pip install opencv-python
"""#Useful geometry features: Contours,Convex hull,Bounding rectangles,Circles,Lines,Shape detection
import cv2
import numpy as np
img = np.zeros((400,400,3), dtype=np.uint8)
cv2.line(img, (0,0), (300,300), (255,255,255), 2)"""

#Pygame Geometry(Game geometry.)
#Install:pip install pygame
#Key Classes: Rect Vector2 Vector3
'''import pygame
v = pygame.Vector2(3,4)
print(v.length())'''

# SciPy Spatial Geometry
#Install:pip install scipy
#Modules:scipy.spatial
#Classes:KDTree,ConvexHull,Delaunay,Voronoi
'''from scipy.spatial import ConvexHull'''
#Used in:GIS,AI,Mapping,Spatial analysis

#Trimesh (3D Geometry)(3D meshes and solids.)
#Install:pip install trimesh
'''import trimesh
mesh = trimesh.creation.box()
print(mesh.volume)'''
#Supports:Meshes,Solids,STL/OBJ files,Boolean operations

#VPython (3D Visual Geometry)
#Install:pip install vpython
'''from vpython import *
sphere()
box()
cylinder()'''
#3D Objects:Sphere,Box,Cone,Cylinder,Curve,Arrow

# CadQuery (CAD Geometry)(Professional CAD modeling.)
#Install:pip install cadquery
'''import cadquery as cq
result = cq.Workplane("XY").box(1,2,3)'''
#Used for:Mechanical CAD,Solid modeling,Engineering

#PyVista (3D Surfaces & Meshes)
#Install:pip install pyvista
#Geometry types:Surface meshes,Volumes,Point clouds
'''
import pyvista as pv
sphere = pv.Sphere()
sphere.plot()'''

#Blender Python API
'''Inside Blender.
Classes:Mesh,Curve,Surface,Object
Used for:3D modeling,Animation,Procedural geometry'''