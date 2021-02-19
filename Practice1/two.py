import math

def f(x):
    if x<84:
        qwe = 21*((((x**2)/99)+math.tan(x)+46)**4)+50*x*x
    elif 84<=x<108:
        qwe = 46*(x**7)-x
    elif 108<=x<158:
        qwe = (((x**7)-math.tan(x)+32)**6) + abs(x)
    elif 158<=x<240:
        qwe = 22*(x**6)+27*(x**4)
    elif x>=240:
        qwe = math.sin((x**3)+30*(x**8))+((x**7)/20)-80
    return qwe

res=f(217)
print('%.2e' % res)
res=f(118)
print('%.2e' % res)
