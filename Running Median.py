from __future__ import division


length = array[0]
array = [1:]


def median_odd(c):
    l = len(c)
    a = int((l-1)/2)
    return float(c[a])


def median_even(c):
    l = len(c)
    a = int(l/2)
    b = int((l/2) -1)
    median = (c[a] + c[b])/ 2
    return (median)

i = 1
while(i<=length):
    n = array[:i]
    l = len(n)
    if(l%2 == 0):
        print(median_even(n))
    else:
        print(median_odd(n))
    i = i+1