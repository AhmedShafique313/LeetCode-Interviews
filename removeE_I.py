a = [1, 9, 3, 5, 7, 8]

def removal_even_integers(arr):
    result = []
    for i in arr:
        if i % 2!=0:
            result.append(i)
    return result


print(removal_even_integers(a))