def histogram():
    nums = list(map(int, input("Give me nums for histogram: ").split()))
    for num in nums:
        print("*" * num)

histogram()