def findNumbers(nums):
    count = 0
    size = len(nums)

    for i in range(size):

        digits = 0
        while (arr[i] > 0):
            digits += 1
            arr[i] = arr[i] // 10

        if (digits % 2) == 0:
            count += 1

    return (count)


arr = [12,345,2,6,7896, 1234]
print(findNumbers(arr))
