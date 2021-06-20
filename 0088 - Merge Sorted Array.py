def merge(num1, m, num2, n):

    last = (m + n) - 1
    mlast = m - 1
    nlast = n - 1

    while nlast >= 0:
        if mlast >= 0 and (num1[mlast] > num2[nlast]):
            num1[last] = num1[mlast]
            last -= 1
            mlast -= 1
        else:
            num1[last] = num2[nlast]
            last -= 1
            nlast -= 1
    return num1

    def merge2(self, num1, m, num2, n):
        last = (m + n) - 1
        mlast = m - 1
        nlast = n - 1

        for i in range(last, mlast, -1):
            num1[i] = num2[nlast]
            nlast -= 1

        num1.sort()
        return num1

