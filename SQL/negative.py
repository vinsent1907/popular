U = [1,2,3]
def negativ(n):                                   # функция возвращающая нужный столбец
    col = []
    for i in range(0,len(n),1):
        col.append(n[i]*(-1))
    return col

qqq = negativ(U)
print(qqq)
