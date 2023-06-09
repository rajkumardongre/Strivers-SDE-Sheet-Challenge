def removeDuplicates(arr,n):
    prev = arr[0]
    res = 1
    curr = 1
    while(curr < n):
        if(prev == arr[curr]):
            curr += 1
        else:
            prev = arr[curr]
            temp = arr[res]
            arr[res] = arr[curr]
            arr[curr] = temp
            res += 1
            curr += 1
    return res
    # return 0