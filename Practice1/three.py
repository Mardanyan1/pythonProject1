import math

def f(n,m):
    summ = 0
    summ1 = 0
    summ2 = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            summ1 += 21*(j**8)+abs(i)
    for i in range(1, n+1):
        summ2 += 50*i + math.sin(i)
    summ = summ1 - summ2 + summ
    return summ

res = f(14, 38)
print('%.2e' % res)
