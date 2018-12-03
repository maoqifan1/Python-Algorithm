from collections import OrderedDict
from math import floor

def binarySearch(arr, item):
    low = 0
    high = len(arr) - 1
    times = 0
    result = OrderedDict()
    while low <= high:
        mid = floor((high + low) / 2)
        if item == arr[mid]:
            result["index"] = mid
            result["times"] = times
            return result
        if arr[mid] > item:
            high = mid - 1
            times += 1
        else:
            low = mid + 1
            times += 1
    return None


if __name__ == "__main__":
     my_arr = [1, 3, 7, 10, 11, 15, 20]
     result = binarySearch(my_arr, 10)
     for key, value in result.items():
         print(str(key)+" => "+ str(value) + "\t")
