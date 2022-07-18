from functools import reduce

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num = filter(lambda x: x % 2 != 0, num)

num = reduce(lambda a, b: a + b, num)

print(num) # 25
