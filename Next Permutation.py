def reverseFromN(arr, si):
    li = len(arr) - 1
    # mid = (len(arr) + si - 1)//2
    while(si < li):
        temp = arr[si]
        arr[si] = arr[li]
        arr[li] = temp
        si += 1
        li -= 1

def nextPermutation(permutation, n):
    n = len(permutation)
    if(n == 1):
        return permutation
    i = n-2
    while(i >= 0):
        if(permutation[i] < permutation[i+1]):
            break
        i -= 1
    j = n-1
    if i == -1:
        reverseFromN(permutation, i+1)
        return permutation    
    else:
        while (j >= 0):
            if(permutation[j] > permutation[i]):
                temp = permutation[j]
                permutation[j] = permutation[i]
                permutation[i] = temp
                break
            j -= 1

        reverseFromN(permutation, i+1)
        return permutation    

