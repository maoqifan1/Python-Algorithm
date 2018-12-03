from functools import reduce

arr1 = [1, 2, 3, 4, 5, 6]

arr2 = map(lambda x: 2 * x, arr1)

for value in arr2:
    print(value)

# print(reduce(lambda x,y: x + y , arr1))
