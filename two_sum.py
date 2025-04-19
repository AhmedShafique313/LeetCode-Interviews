nums = [1, 8, 2, 6, 5]
target = 10


def twosum(nums, target):
    dictionary = dict()
    for index, num in enumerate(nums):
        compliment = target - num
        if compliment in dictionary:
            return [dictionary[compliment], index]
        dictionary[num] = index

print(twosum(nums, target))