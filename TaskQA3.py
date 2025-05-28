arr = [int(x) for x in input("Enter numbers separated by space: ").split()]
multiples_of_3 = [x for x in arr if x % 3 == 0]
print(multiples_of_3)