def Romans_to_Integers(arr):
    prev_val = 0
    total = 0
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for char in reversed(arr):
        current = roman_map[char]
        if current < prev_val:
            total -=current
        else:
            total+=current
        prev_val = current
    return total
