# BIM A+3 - Assignment 3.1
# Vicente Mediano Corona
# The Python program calculates geometrical characteristics of a polygon shape with n number of points

print()
print("The Python program calculates geometrical characteristics of a polygon shape with n number of points")
print()

# Print requested number of sides
n_sides = int(input("Enter number of points n: "))

# Lists that stores all the entered pointns. Its empty at start.
x = []
y = []

# Input all points.
print()
print("Enter x and y coordinates for polygon points in a counterclockwise sequence: ")
print()
for i in range(n_sides):
    xValue = int(input(f"Enter 'x' value for Point {i + 1}: "))
    yValue = int(input(f"Enter 'y' value for Point {i + 1}: "))
    x.append(xValue)
    y.append(yValue)
    print()

# Print a Table of entered Points
print()
print(f"{'  Point'}   {'x':>6}   {'y':>9}")
print("-" * 33)
for i in range(n_sides):
    print(f"{i+1:>5}   {x[i]:>10.2f}  {y[i]:>10.2f}")
print()

# Create List for storing Calculated Values
AxList = []
SxList = []
SyList = []
IxList = []
IyList = []
IxyList = []

for i in range(-1, n_sides-1):
    # Calculate values for cross-seccional Area of the polygon (Ax), Static Moments of the cross section (Sx, Sy), and Axial Moments of inertia of the transmission (Ix, Iy, Ixy) to fill-in lists:
    AxValue = (x[i+1] + x[i]) * (y[i+1] - y[i])
    SxValue = (x[i+1] - x[i]) * (y[i+1]**2 + y[i]*y[i+1] + y[i]**2)
    SyValue = (y[i+1] - y[i]) * (x[i+1]**2 + x[i]*x[i+1] + x[i]**2)
    IxValue = (x[i+1] - x[i]) * (y[i+1]**3 + (y[i+1]**2)* y[i] + y[i+1]*(y[i]**2) + (y[i]**3))
    IyValue = (y[i+1] - y[i]) * (x[i+1]**3 + (x[i+1]**2)* x[i] + x[i+1]*(x[i]**2) + (x[i]**3))
    IxyValue = (y[i+1] - y[i]) * (y[i+1] * (3*x[i+1]**2 + 2*x[i+1] * x[i] + x[i]**2) + y[i]*(3*x[i]**2 + 2*x[i+1]*x[i] + x[i+1]**2))
    # Append calculated values to the lists:
    AxList.append(AxValue)
    SxList.append(SxValue)
    SyList.append(SyValue)
    IxList.append(IxValue)
    IyList.append(IyValue)
    IxyList.append(IxyValue)

# Calculate cross-seccional Area of the polygon (Ax), Static Moments of the cross section (Sx, Sy), Axial Moments of inertia of the transmission (Ix, Iy, Ixy), coordinates of the centroid of the cross section (xt, yt), and moments of inertia with respect to the axes moved in parallel through the points of gravity of the cross-secction (Ixt, Iyt, Ixyt)::
Ax = 0.5 * sum(AxList)
Sx = -1/6 * sum(SxList)
Sy = 1/6 * sum(SyList)
Ix = -1/12 * sum(IxList)
Iy = 1/12 * sum(IyList)
Ixy = -1/24 * sum(IxyList)
xt = Sy/Ax
yt = Sx/Ax
Ixt = Ix - (yt**2 * Ax)
Iyt = Iy - (xt**2 * Ax)
Ixyt = Ixy + xt*yt*Ax

# Print Geometric Charactersitics:
print("Geometric characteristics: ")
print(f"Ax:  {Ax:>6.2f}")
print(f"Sx:  {Sx:>6.2f}")
print(f"Sy:  {Sy:>6.2f}")
print(f"Ix:  {Ix:>6.2f}")
print(f"Iy:  {Iy:>6.2f}")
print(f"Ixy:  {Ixy:.2f}")
print(f"xt:  {xt:>6.2f}")
print(f"yt:  {yt:>6.2f}")
print(f"Ixt:  {Ixt:>5.2f}")
print(f"Iyt:  {Iyt:>5.2f}")
print(f"Ixyt:  {Ixyt:>4.2f}")
print()
print("        __________________________________")
print("       | End of the program. Thank you :) |")
print("       |_  _______________________________|")
print("         |/")
print("  (\___/)   ")
print(" (=° x °=)")
print("(''')_(''')_/")
print()