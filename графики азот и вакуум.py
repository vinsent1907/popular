# This figure shows the name of several matplotlib elements composing a figure

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter

with open(r'''Production log.log''', 'r', encoding='utf-16le') as file: # открывает файл для чтения в кодировке utf-16le
    str_f = file.read()
    str_list = list(str_f)
    for i in range(len(str_f)):
        if str_list[i] == '\n':
            str_list[i] = '\t'           #заменяем перенос строки на горизонтальную табуляцию
        if str_list[i] == '-':
            str_list[i] = ''             #отрицательные числа становятся положительными для преобразованиея в int
    str_list =''.join(str_list)  
    str_list = str_list.split('\t')

def colom(k,m):                                   # функция возвращающая нужный столбец
    col = []
    for i in range(26+m,len(k),26):
        col.append(k[i])
    return col

len_colom = len(list(map(int,colom(str_list,23)))) # число элементов в столбце
 
X = list(range(0,len_colom,1))
Y1 = list(map(int,colom(str_list,6)))
Y2 = list(map(int,colom(str_list,7))) 
Y3 = list(map(int,colom(str_list,8)))
Y4 = list(map(int,colom(str_list,9)))


maxY = max(max(Y1),max(Y2))                                   # максимальное значение по шкале Y
maxX = len_colom

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, aspect = maxX/maxY*0.5)


ax.xaxis.set_major_locator(MultipleLocator(240.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(maxY/10))
ax.yaxis.set_minor_locator(AutoMinorLocator(1))
ax.set_xlim(0, maxX)
ax.set_ylim(0, maxY)


ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.25')

ax.grid(linestyle="-", linewidth=0.5, color='.25', zorder=-10)


#def negative(cc):
#    co = []
#    for i in range (0,len(cc),1):
#        col.append((k[i])
#    return co

#qqq = negative(Y3)
#print(qqq)

ax.plot(X, Y1, c='r', lw=0.5, label="Установленное давление азота", zorder=10)# Красный график
ax.plot(X, Y2, c='y', lw=3, label="Значение давления азота", zorder=1) # Желтый график
ax.plot(X, Y3, c='b', lw=0.5, label="Установленное давление вакуума", zorder=10) # Синий график
ax.plot(X, Y4, c='g', lw=3, label="Значение давления вакуума", zorder=1) # Зеленый график


ax.set_title("Подробный тренд давления", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Время с")
ax.set_ylabel("Давление mbar")

ax.legend()

plt.show()
a = -5
print(int(a))
