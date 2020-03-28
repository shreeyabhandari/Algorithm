def sorted (T):
    l = len(T)
    if l>1:
        for i in range(l-1):
            if T[i] > T[i+1]:
                return False
    return True

print(sorted([1,2,3,4]))
print(sorted([2,1,0,5]))


def add (T, x):
    temp=[]
    l = len(T)
    i = 0
    while i<l and T[i]<x:
        temp.append(T[i])
        i +=1
    temp.append(x)
    while i<l:
        temp.append(T[i])
        i += 1
    return temp

print(add([1,2,5,7], 8))


def cocktail (T):
    swap = True
    left = True
    l = len(T)
    begin = 0
    while swap:
        swap = False
        i = begin
        if left:
            while i < l-1:
                if T[i] > T[i+1]:
                    T[i], T[i+1] = T[i+1], T[i]
                    swap = True
                i += 1
            left = False
            l -=1
        else:
            for i in range(l-1):
                if T[l-1-i] < T[l-i-2]:
                    T[l-1-i], T[l-i-2] = T[l-i-2], T[l-1-i]
                    swap = True
            left = True
            begin += 1


T = [1,0,2,5, 10, 3]
cocktail(T)
print(T)


def bool_array (T):
    l = len(T)
    cpt = 0
    for i in T:
        if i == False:
            cpt += 1
    for i in range(l):
        if i < cpt:
            T[i] = False
        else:
            T[i] = True
T = [True, True, False, True, False, False]
bool_array(T)
print(T)

def bool_array_bis(T):
    current = 0
    end = len(T)-1
    while (current < end):
        if T[current] == False:
            current += 1
        else:
            T[current], T[end] = T[end], T[current]
            end -= 1

T = [True, True, False, True, False, False]
bool_array_bis(T)
print(T)


def flag(T):
    i_blue = 0
    i_red = len(T)-1
    i_current = 0
    while (i_current <= i_red):
        if T[i_current] == "White":
            i_current +=1
        elif T[i_current] == "Red":
            T[i_current], T[i_red] = T[i_red], T[i_current]
            i_red -= 1
        else:
            T[i_current], T[i_blue] = T[i_blue], T[i_current]
            i_blue += 1

T = ["White", "Blue", "Blue", "Red", "Blue", "White", "Blue"]
flag(T)
print(T)

