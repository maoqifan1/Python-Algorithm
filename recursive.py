
def count_down(i):
    if i <= 0:
        return 
    else:
        print(str(i))
        count_down(i - 1)

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

def fabonacci(i):
    if i == 1 or i == 2:
        return 1 
    elif i >= 3:
        return fabonacci(i - 1) + fabonacci(i - 2)

def s_um(arr):
    if arr == []:
        return 0
    return arr[0] + s_um(arr[1:])

def sum_(arr):
    if arr == []:
        return
    return 1 + sum_(arr[1:])

def findMax(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]    
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

# def binarySearch(arr, item):
#     if len(arr) == 1 and arr[0] == item:
#         return 0
#     sub = binarySearch(arr[:len(arr) / 2 - 1])
#     return  


if __name__ == "__main__":
    ss =[1, 2, 3]
    print(ss) 
