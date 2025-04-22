def sum_equals_zero(arr):
    prefix_sum = 0
    index_map = {}
    max_len = 0

    for index, value in enumerate(arr):
        prefix_sum += value

        if prefix_sum == 0:
            max_len = index + 1  # From start to current index

        if prefix_sum in index_map:
            max_len = max(max_len, index - index_map[prefix_sum])
        else:
            index_map[prefix_sum] = index
    
    return max_len

# Example usage
a = [15, -2, 2, -8, 1, 7, 10, 23]
print(sum_equals_zero(a))
