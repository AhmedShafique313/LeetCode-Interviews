def Count_Largest_Group(n):
    group_count = {}
    for i in range(1, n + 1):
        digit_sum = sum(int(digit) for digit in str(i))

        if digit_sum in group_count:
            group_count[digit_sum] += 1
        else:
            group_count[digit_sum] = 1
    
    max_size = max(group_count.values())
    largest_group_count = 0
    for count in group_count.values():
        if count == max_size:
            largest_group_count += 1
    return largest_group_count


print(Count_Largest_Group(13))
print(Count_Largest_Group(2))    