def RemoveElement(arr, value):
    k = 0
    for i in range(len(arr)):
        if arr[i] != value:
            arr[k] = arr[i]
            k += 1
    return k

num = [0,1,2,2,3,4,0,5]
val = 2
print(RemoveElement(num, val))
