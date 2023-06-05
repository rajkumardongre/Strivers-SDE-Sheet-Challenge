def pairSum(arr, s):
    n = len(arr)
    res = []
    d = {}
    for i in range(n):
        if(d.get(s-arr[i], 0) != 0):
            for j in range(d.get(s-arr[i])):
                if(arr[i] < s-arr[i]):
                    res.append([arr[i], s-arr[i]])
                else:
                    res.append([s-arr[i], arr[i]])
        d[arr[i]] = d.get(arr[i], 0) + 1
    res.sort()
    return res