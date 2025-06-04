import math
radius = int(input("Give me radius of a sphere: "))

def volume_of_sphere(a):
    answer = 4/3 * math.pi * (radius**3)
    print(answer)

volume_of_sphere(radius)