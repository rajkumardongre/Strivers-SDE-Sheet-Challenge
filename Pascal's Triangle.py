def printPascal(n:int):
    if n==1:
        return [[1]]
    elif n == 2:
        return [[1], [1,1]]
    else:
        res = [[1], [1,1]]
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                row.append(res[i-1][j-1] + res[i-1][j])
            row.append(1)
            res.append(row)
        return res