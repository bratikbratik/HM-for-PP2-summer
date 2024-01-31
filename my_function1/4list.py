nums = list(map(int, input("Give me numbers separated by space: ").split()))

def filter_prime(nums):
    for i in nums:
        if i % 2 == 0:
            print(i)

filter_prime(nums)