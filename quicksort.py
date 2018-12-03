from time import sleep
import numpy as np

def qSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]
        return  qSort(less) + [pivot] + qSort(more)

def form(arr):
    arr1 = arr[:]
    arr2 = []
    for i in arr:
        k = 0
        for j in arr1:
            k = k + (i * j)
        arr2.append(k)
    return arr2
    
if __name__ == "__main__":
    print(qSort([2, 1, 3, 5, 8, 10, 7]))


