nums = list(map(int, input("Give me some numbers: ").split()))

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

result = has_33(nums)
print(result)

