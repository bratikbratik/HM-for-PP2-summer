string = "Hello, nice to meet you! HOPE you will be able to PURSUE your DREAMS."

upper_sum = 0
lower_sum = 0

upper_sum(1 for char in string if char.isupper())
lower_sum(1 for char in string if char.islower())

print(upper_sum, lower_sum)