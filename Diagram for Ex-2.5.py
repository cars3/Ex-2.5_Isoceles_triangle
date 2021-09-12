import matplotlib.pyplot as plt

A = (5, -2)
B = (6,4)  # The coordinates of the triangle
C = (7, -2)

x = [5,6,7]
y = [-2,4,-2]       # the X and Y points of the triangle
plt.plot((x[0], x[1]),(y[0],y[1]), label = '$AB$')
plt.plot((x[1], x[2]),(y[1],y[2]), label = '$AC$') # Drawing the lines
plt.plot((x[2], x[0]),(y[2],y[0]), label = '$BC$')

plt.text(x[0] - 0.2 ,y[0], "B")
plt.text(x[1] + 0.1 ,y[1], "A") # Labelling the points
plt.text(x[2] ,y[2], "C")

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best') # Adding  the labels to the x and y axis, legend, and grid
plt.grid()
plt.axis('equal')

plt.show()