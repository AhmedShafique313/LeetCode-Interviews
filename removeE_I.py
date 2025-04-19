a = [1, 9, 3, 5, 7, 8]

def removal_even_integers(arr):
    # for i in arr:
    #     if i%2!=0:
    #         return i
    return [i for i in arr if i%2!=0]

print(removal_even_integers(a))