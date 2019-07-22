import numpy as np
def min_l(l):
    min_x = float('inf')
    i = len(l) - 1
    while i >= 0:
        if l[i] == 0:
            l.remove(0)
        elif l[i] < min_x:
            min_x = l[i]
        i -=1 
    return l,min_x


def count_n_k(l,n,k):
    l = list(set(l))
    for i in range(k):
        l,min_x = min_l(l)
        l = np.array(l) - min_x
        if min_x != 0:
            print(min_x)
        elif min(l) == max(l) == 0:
            print(0)

if __name__ == '__main__':
    a = np.array([1,2,3])
    print(a-1)

    