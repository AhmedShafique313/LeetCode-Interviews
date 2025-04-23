def Remove_Duplicates_from_Sorted_Array(arr):
    # two pointer technique
    unique_count = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_count]:
            unique_count+=1
            arr[unique_count] = arr[i]
    return unique_count + 1

nums = [0,0,1,1,1,2,2,3,3,4]
print(Remove_Duplicates_from_Sorted_Array(nums))