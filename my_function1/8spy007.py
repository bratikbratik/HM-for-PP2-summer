nums = list(map(int, input("Give me some numbers: ").split()))

def spy(nums):
    zero_counter = 0
    for i in nums:
        if i == 0:
            zero_counter += 1
        elif i == 7 and zero_counter == 2:
            return True
    return False

result = spy(nums)
print(result)

