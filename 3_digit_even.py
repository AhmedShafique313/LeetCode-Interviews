from itertools import permutations

def Digit_Number(digits):
    result = set()
    for perm in permutations(digits, 3):
        if perm[0] == 0:
            continue
        num = perm[0]*100 + perm[1] *10 + perm[2]
        if num % 2==0:
            result.add(num)

    return sorted(result)

arr = [2,1,3,0]
print(Digit_Number(arr))