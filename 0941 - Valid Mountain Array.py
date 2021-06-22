    def validMountainArray(arr):
        
        size = len(arr)
        
        i = 0

        #check if beginning is ascending
        while (i < size and (i+1) < size and arr[i] < arr[i + 1]):
            i += 1
        
        #check if array is decreasing from beginning
        if (i == 0 or (i) == size - 1):
            return False

        #check if it is decreasing
        while (i < size and (i+1) < size and arr[i] > arr[i+1]):
                i += 1

        return i == (size - 1)
