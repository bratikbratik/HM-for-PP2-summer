n = int(input("Give me a number: "))
even_nums = []

for i in range(n+1):
    if i % 2 == 0:
        even_nums.append(i)

print(even_nums)