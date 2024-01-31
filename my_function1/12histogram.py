nums = list(map(int, input("Give me nums for histogram: ").split()))

def histogram(nums):
    for num in nums:
        print("*" * num)

histogram(nums)