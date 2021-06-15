def findMaxConsecutiveOnes(nums):
    size = len(nums)
    count = 0
    ans = 0
    for i in range(size):
        if nums[i] == 1:
            count += 1
            ans = max(ans, count)
        else:
            count = 0
    return ans


nums = [1,1,0,1,1,1]

print( findMaxConsecutiveOnes(nums) )

