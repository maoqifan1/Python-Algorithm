
def qSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]
        return  qSort(less) + [pivot] + qSort(more)


if __name__ == "__main__":
    print(qSort([2, 1, 3, 5, 8, 10, 7]))


