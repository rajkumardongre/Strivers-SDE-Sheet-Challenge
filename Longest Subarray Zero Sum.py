def LongestSubsetWithZeroSum(arr):
    res = -1
    sum = 0
    d = {}
    n = len(arr)
    for i in range(n):
        sum += arr[i]
        if(d.get(sum, -1) == -1):
            d[sum] = i
        else:
            if res < (i - d[sum]):
                res = i - d[sum]
        if sum == 0 and res < i+1:
            res = i+1
    if res == -1:
        return 0
    return res