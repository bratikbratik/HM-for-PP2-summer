import math

def polygon_area(num_sides, side_length):
    return int((num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides)))

num_sides = int(input())
side_length = int(input())

answer = polygon_area(num_sides, side_length)
print(answer)