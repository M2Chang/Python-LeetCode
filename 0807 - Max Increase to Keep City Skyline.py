def maxIncreaseKeepingSkyline(grid):
    size = len(grid)
    citysum = 0

    rowmax = []
    colmax = []

    for i in range(size):
        rowmaxhold = 0
        colmaxhold = 0
        for j in range(size):
            if grid[i][j] > rowmaxhold:
                rowmaxhold = grid[i][j]

            if grid[j][i] > colmaxhold:
                colmaxhold = grid[j][i]

        rowmax.append(rowmaxhold)
        colmax.append(colmaxhold)

    for i in range(size):
        for j in range(size):
            x = min(rowmax[i], colmax[j])

            if grid[i][j] < x:
                citysum += x - (grid[i][j])

    return citysum


grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(maxIncreaseKeepingSkyline(grid))
