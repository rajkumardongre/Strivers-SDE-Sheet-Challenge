
def sort012(arr, n) :
    lst = [0,0,0]
    for i in range(n):
        lst[arr[i]] += 1
    j = 0
    for i in range(lst[0]):
        arr[j] = 0
        j += 1
    
    for i in range(lst[1]):
        arr[j] = 1
        j+=1
    
    for i in range(lst[2]):
        arr[j] = 2
        j+=1


