def twoSum(nums, target):
    size = len(nums)

    sum = 0
    result = []
    for i in range(size):
        for j in range(i + 1, size):
            sum = nums[i] + nums[j]
            if sum == target:
                result.append(i)
                result.append(j)
    return result


nums = [3,2,3]
target = 6
print(twoSum(nums, target))
