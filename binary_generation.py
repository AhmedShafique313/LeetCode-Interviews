def binary_numbers(n):
    queue = ["1"]
    result = []
    for i in range(n):
        binary = queue.pop(0)
        result.append(binary)
        queue.append(binary + '0')
        queue.append(binary + '1')
    return result

num = 5
print(binary_numbers(num))
