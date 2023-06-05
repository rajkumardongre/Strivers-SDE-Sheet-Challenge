
def findDuplicate(arr:list, n:int):
    d = {}
    for i in range(n):
        d[arr[i]] = d.get(arr[i], 0) + 1
    
    for key in d:
        if d[key] > 1:
            return key