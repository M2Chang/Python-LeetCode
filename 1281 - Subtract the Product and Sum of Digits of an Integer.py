def subtractProductAndSum(n):
    sumans = 0
    product = 1
    while (n != 0):
        sumans += (n % 10)
        product *= (n % 10)
        n = n // 10
    return (product - sumans)


n = 234
print(subtractProductAndSum(n))