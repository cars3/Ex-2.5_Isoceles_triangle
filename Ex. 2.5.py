import math

A = (5, -2)
B = (6, 4)         # Assigning the values for the points of the triangle
C = (7, -2)

distances = []
occurrence = []
counter = 0

def distance_formula(pos1, pos2):
    distance = math.sqrt(math.fabs((pos2[0] - pos1[0])**2 - (pos2[1] - pos1[1])**2))
    distances.append(distance)
    return distance      # Using the distance formula -> square root of (x2 - x1)^2 - (y2 - y1)^2

distance_formula(A,B)
distance_formula(B,C)    # Finding the distance between points
distance_formula(A,C)

for distance in distances:
    count = 0
    for item in distances:
        if (item == distance):   # The part for checking the whether any 2 lines are equal
            count = count + 1
    occurrence.append(count)

if 2 in occurrence:
    print("With the given data of triangle of ABC the code was able to understand this is an Isoceles Triangle")
else:
    print("With the given data of triangle of ABC the code was able to understand this is not an Isoceles Triangle")