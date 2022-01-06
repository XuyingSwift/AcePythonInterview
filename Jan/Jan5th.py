def twoSum(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        else:
            seen[num] = index
    return []


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    target = 3
    result = twoSum(nums, target);
    print(result[0])
    print(result[1])
