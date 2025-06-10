n = int(input("Give me a number: "))
nums = []

for i in range(n+1):
    if i % 3 == 0 and i % 4 == 0:
        nums.append(i)

print(nums)