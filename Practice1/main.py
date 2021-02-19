import math

def sum(a, b):
    res = a+b
    return res

def f(x, y, z):
    Bap = math.sqrt((21*(z**8)+abs(x))/(math.tan(z)-z))+((((x**5)/7)-(x**7)+65)/((y**6)-z**3))+((x - 57 * x**2)/((22*(x**6)) + 96*(y**4)))
    return Bap
"""
num1 = 5
num2 = 5.5
text1 = 'hello Bap'
text2 ='''
sdfdsfdvsdfv
vsvbdf

dsvsdffd
'''
flag = True

list1 = [1, 2, "test"]#не меняются значения
list2 = (1, 2, "test")#меняются значения

print(num1)
print("i have " + str(num1) + " dollars")
print(f"i have {num1} dollars")
print("i have {0} dollars {1}".format(num1,num2))

user_input = input("enter: ")
print(user_input*10)

a = 7
b = 15
result = a ** b
print(sum(2, 3))



# PascalCase
# camelCase
# snake_case
"""

res = f(78, 4, -91)
print('%.2e' % res)
res = f(5, 84, -65)
print('%.2e' % res)

