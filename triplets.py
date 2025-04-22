def finding_triplets(arr, k):
    arr.sort()
    result = []
    n = len(arr)
    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == k:
                result.append([arr[i], arr[left], arr[right]])
                left +=1
                right-=1
            if s < k:
                left +=1
            else:
                right-=1
    return result

k = 15
a = [2, 3, 5, 1, 6, 8, 4, 7]
print(finding_triplets(a, k))