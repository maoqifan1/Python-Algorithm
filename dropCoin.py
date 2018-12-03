def f(n):
    # base case
    if n == 1:     
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 1
    if n == 4:
        return 3
    if n == 5:
        return 1

    h = [1,3,5]
    minx = n
    for i in range(3):
        # recursive case
        coun = f(n-h[i])+1   
        if minx > coun:       
            minx = coun
    return minx

print(f(11))