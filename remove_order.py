nums = [1, 3, 2, 3, 4, 5, 2, 6]
# output = [1, 3, 2, 4, 5, 6]

def remove_duplicates_maintain_order(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

print(remove_duplicates_maintain_order(nums))
