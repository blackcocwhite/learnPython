def lib(max):
    n,a,b = 0,0,1
    while n < max :
        yield(b)
        a,b = b,a+b
        n = n + 1
    return 'done'

def triangle():
    p = [1];
    while True:
        yield p
        p = [1] + [ p[i] + p[i+1] for i in range(len(p)-1)] + [1]
'''
n = 0
for t in triangle():
    print(t)
    n = n + 1
    if n == 10 :
        break
'''

import math
import numpy
def matrix(col,row):
    i = 0
    k = 1
    j = 0
    result = numpy.zeros((row,col))
    small = col if col > row else row
    count = math.ceil(small/2)
    while i < count :
        maxRight = col  - i
        maxBottom = row  - i
        for j in range(i,maxRight):
            result[i][j] = k
            k += 1
            j += 1
        for j in range(i,maxBottom-1):
            result[j+1][maxRight-1] = k
            k += 1
            j += 1
        for j in range(maxRight-1,i,-1):
            if result[maxBottom-1][j-1]:
                break
            result[maxBottom-1][j-1] = k
            k += 1
            j += 1
        for j in range(maxBottom - 1,i ,-1):
            if result[j-1][i]:
                break
            result[j-1][i] = k
            k += 1
            j += 1
        i = i + 1
    print(result) 
matrix(10,6)



'''
g = lib(6)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
'''

    