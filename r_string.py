def reverse_string(arr):
    for i in range(len(arr)):
        reverseString = arr[::-1]
    return reverseString

a = 'Bayerische Motoren Werke'
b = 'lamborgini'
print(reverse_string(b))