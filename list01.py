def sorting01_ascending(arr):
    zeros = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            zeros+=1
        
    for i in range(n):
        if i < zeros:
            arr[i] = 0
        else:
            arr[i] = 1
    return arr


a = [0, 1, 0, 1, 1, 1, 0, 0]
print(sorting01_ascending(a))
