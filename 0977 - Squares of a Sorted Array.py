def sortedSquares(nums):
    size = len(nums)

    for i in range(size):
        nums[i] = pow(nums[i], 2)

    nums.sort()
    print(nums)


nums = [-4,-1,0,3,10]
sortedSquares(nums)
