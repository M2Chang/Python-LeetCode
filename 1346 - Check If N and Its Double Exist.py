def checkIfExist(arr):

  size = len(arr)

        for i in range(size):
            for j in range(size):
                if i != j:
                    if arr[i] == 2 * arr[j]:
                        return True

        return False
