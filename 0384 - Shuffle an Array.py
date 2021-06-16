def shuffle(nums, n):

    result = []

    x = nums[0:n]
    y = nums[n:]

    for i in range(n):
        result.append(x[i])
        result.append(y[i])


    return (result)

nums = [2,5,1,3,4,7]
n = 3

print(shuffle(nums,n))
