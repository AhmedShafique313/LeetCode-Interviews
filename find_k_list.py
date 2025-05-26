def finding_kth_element(numbers):
    largest = 0
    sec_largest = 0
    for num in numbers[1::]:
        if num > largest:
            sec_largest = largest
            largest = num
        elif num!=largest and num > sec_largest:
            sec_largest = num
    return sec_largest

# a = [-2,-1,0,1,2]
arr = [-6,-7,-4,-2,0,4,6,2,7]
print(finding_kth_element(arr))