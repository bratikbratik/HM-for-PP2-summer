import time
import math

num = int(input("Gibe me a num: "))
delay = int(input("Enter delay in milliseconds: "))

time.sleep(delay / 1000)

result = math.sqrt(num)

print(f"Sqrt of {num} after {delay} ms is {result}")