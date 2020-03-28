def partition(t, begin, end):
    i = (begin-1)
    pivot = t[end]
    for j in range(begin,end):
        if t[j] < pivot:
            i = i+1
            t[i] , t[j] = t[j] , t[i]
    t[i+1], t[end] = t[end], t[i+1]
    return (i+1)

def quicksort(t, begin, end):
    if begin < end:
        cut = partition(t, begin, end)
        quicksort(t, begin, cut-1)
        quicksort(t, cut+1, end)



t = [10, 9, 13, 7, 5, 8]
n=len(t)
quicksort(t,0,n-1)
print ("the sorted array is:")
for i in range(n):
    print("%d" %t[i])
