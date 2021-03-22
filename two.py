import math

def per(asd):
    """b = ""
    i = 2
    while i <= 9:
        b = b + asd[i]
        i = i + 1
    ress = int(b, 16)
    print(b)
    print(ress)
    res = []
    while ress:
        res.append(ress % 2)
        ress //= 2
    qas =len(res)
    while len(res) < 32:
        res.append(0)
        qas = qas + 1
    res.reverse()
    ser = []
    ser.append(res[29])
    ser.append(res[28])
    ser.append(res[13])
    ser.append(res[14])
    ser.append(res[15])
    ser.append(res[16])
    ser.append(res[30])
    ser.append(res[31])
    sad = 0
    while sad < 12:
        ser.append(res[sad])
        sad = sad + 1
    das = 20
    while das < 31:
        ser.append(res[das])
        das = das + 1


    fin = int("".join(map(str, ser)), 10)
    print(fin)
    return res
"""
    g = asd & 0x80000000
    f = asd & 0x40000000
    e = asd & 0x20000000
    d = asd & 0x10000000
    c = asd & 0xFFE0000
    b = asd & 0x1E000
    a = asd & 0x1FFF

    c<<=4
    a<<=8
    g>>=24
    f>>=24
    b>>=11
    e>>=28
    d>>=28
    asd = a + b + c + d + e + f + g
    return asd

print(hex(per(0x059bd036)))
print(hex(per(0x7148a3a1)))