def duplicateZeros(arr):
    size = len(arr)
    i = 0
    while i <= size - 1:
        if arr[i] == 0:
            arr.insert((i+1),0)
            arr.pop()
            i = i + 2
        else: i = i + 1
    return arr

arr = [1,0,2,3,0,4,5,0]
duplicateZeros(arr)