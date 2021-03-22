import math

def num21(x):
    if x[0]==1983:
        if x[4]==1970:
            return 8
        elif x[4]==1990:
            return 9
        elif x[4]==1981:
            return 10
    elif x[3]==1968:
        return 7
    elif x[3]==1999:
        if x[1]=='mask':
            if x[2]==2001:
                return 0
            elif x[2]==1969:
                return 1
            elif x[2]==1961:
                return 2
        elif x[1]=='sass':
            return 3
        elif x[1]=='abap':
            if x[4]==1970:
                return 4
            elif x[4] == 1990:
                return 5
            elif x[4] == 1981:
                return 6

res = num21([1983, 'abap', 2001, 1999, 1990])
print(res)
res = num21([2007, 'sass', 1961, 1968, 1990])
print(res)