import math

def tabl(a):



    rad1 = a
    #замена [at] на @
    i = 0
    while i < 3:
        num = rad1[0][i].find("[at]")
        if num < 0:
            print("")
        else:
            rad1[0][i] = rad1[0][i].replace("[at]", "@")
        i = i + 1
    #удаление второй буквы
    j = 0
    while j < 3:
        num = rad1[1][j].find(" ")
        if num < 0:
            print("")
        elif num == 4:
            rad1[1][j] = rad1[1][j][:2]+rad1[1][j][4:]
        j = j + 1
    # удаление пустого столбца
    k = 0
    kk = 0
    while k < 3:
        num = rad1[2][k].find("none")
        if num < 0:
            print("")
        else:
            kk = kk + 1
        k = k + 1
    if kk == 3:
        del rad1[2]
    #удаление похожих столбцов
    q=0
    kk = 0
    while q < 3:
        if rad1[2][q] == rad1[3][q]:
            kk = kk + 1
        q = q + 1
    if kk == 3:
        del rad1[2]
    #изменение номера
    z = 0
    q = 0
    while q < 3:
        num = rad1[3][z].find("+7")
        if num < 0:
            print("")
        else:
            rad1[3][z] = rad1[3][z].replace("+7", "")
        z = z + 1
        q = q + 1
    qwer = rad1
    return qwer



rad1 = tabl([["lalov22[at]rambler.ru","totov38[at]yandex.ru","zacefij44[at]yandex.ru"],["А.Н. Лалов", "М.Ф. Тотов", "С.Е. Цачефий"],["none","none","none"],["нет","нет","да"],["нет","нет","да"],["+7 (998) 206‐43‐20","+7 (496) 298‐66‐60" ,"+7 (402) 250‐29‐47"]])

print(rad1)