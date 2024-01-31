elements = list(input("Give me some elements for the unique list: ").split())

def unique(list):
    my_set = []
    for element in list:
        if element not in my_set:
            my_set.append(element)
    print(my_set)

unique(elements)