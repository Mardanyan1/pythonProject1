import math

def f(n):
    if n==0:
        return 5
    else:
        return math.tan(f(n-1))+math.tan(f(n-1))-53

res = f(15)
print('%.2e' % res)
