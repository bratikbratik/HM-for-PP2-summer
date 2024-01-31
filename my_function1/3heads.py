heads = int(input("Print how many heads: "))
legs = int(input("Print how many legs: "))

def solver(heads: int, legs: int):
    print(f"Rabbits: {(legs - 2 * heads) // 2}. Chickens: {heads - ((legs - 2 * heads) // 2)}")

solver(heads, legs)
