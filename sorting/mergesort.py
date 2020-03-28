def partition(T, begin, end):
    pivot = T[begin]
    i = begin
    j = end
    begin += 1
    while begin <= end:
        while begin <= j and T[begin] < pivot:
            begin += 1
        while end > i and T[end] > pivot:
            end -= 1
        if begin < end:
            T[begin], T[end] = T[end], T[begin]

    T[i], T[end] = T[end], T[i]
    return end

def Quicksort(T, begin, end):
    if begin < end:
        cut = partition(T, begin, end)
        Quicksort(T, begin, cut -1)
        Quicksort(T, cut+1, end)

T = [2, 6, 0, 8, 1]
print(T)
Quicksort(T, 0, 4)
print(T)


def merge (T, begin, m, end):
    i = begin
    j = m + 1
    tab = []

    while i <= m and j <= end:
        if T[i] < T[j]:
            tab.append(T[i])
            i += 1
        else:
            tab.append(T[j])
            j += 1
    while i <= m:
        tab.append(T[i])
        i += 1
    while j <= end:
        tab.append(T[j])
        j += 1
    k = 0
    for i in range(begin, end+1):
        T[i] = tab[k]
        k += 1

def merge_sort(T, begin, end):
    if begin < end :
        m = (begin + end) // 2
        merge_sort(T, begin, m)
        merge_sort(T, m+1, end)
        merge(T, begin, m, end)

T = [2, 6, 0, 8, 1]
print(T)
merge_sort(T, 0, 4)
print(T)
