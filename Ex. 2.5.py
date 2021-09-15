import numpy as np

A = np.array((1, 5, -2))
B = np.array((1, 6, 4))
C = np.array((1, 7, -2))

AB = np.linalg.norm(A - B)
BC = np.linalg.norm(B - C)
AC = np.linalg.norm(A - C)

if AB == AC:
    print("With triangle ABC, this is an Isoceles Triangle")
elif AB == BC:
    print("With triangle ABC, this is an Isoceles Triangle")
elif AC == BC:
    print("With triangle ABC, this is an Isoceles Triangle")
else:
    print("With triangle ABC, this is not an Isoceles Triangle")
