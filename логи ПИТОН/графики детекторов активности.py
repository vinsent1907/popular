# для построения используется matplotlib

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
    #int_list = list(map(int,str_list))

def colom(k,m):                                   # функция принимает список и номер столбца,  возвращающая нужный столбец в виде списка (используется смещение 26)
    col = []
    for i in range(26+m,len(k),26):
        col.append(k[i])
    return col


len_colom = len(list(map(int,colom(str_list,23)))) # число элементов в столбце
#print(len_colom)
 
X = list(range(0,len_colom,1))
Y1 = list(map(int,colom(str_list,18)))
Y2 = list(map(int,colom(str_list,19))) 
Y3 = list(map(int,colom(str_list,21)))
Y4 = list(map(int,colom(str_list,22)))
#Y5 = list(map(int,colom(str_list,23)))

maxY = max(max(Y1),max(Y2))                                   # максимальное значение по шкале Y
maxX = len_colom

#print (max(Y5))
#Y6 = list(map(int,colom(str_list,24)))
#X = np.linspace(0.1, 8.5, 30)
#Y1 = 2+np.cos(X)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, aspect = maxX/maxY*0.5)


#def minor_tick(x, pos):
#    if not x % 1.0:
#        return ""
#    return "%.2f" % x

ax.xaxis.set_major_locator(MultipleLocator(240.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(650000/10))
ax.yaxis.set_minor_locator(AutoMinorLocator(1))
#ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))
ax.set_xlim(0, maxX)
ax.set_ylim(0, 650000)


ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.25')

ax.grid(linestyle="-", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c='r', lw=1, label="Activity detector N°1", zorder=2)# Красный график
ax.plot(X, Y2, c='y', lw=1, label="Activity detector N°2", zorder=1) # Желтый график
ax.plot(X, Y3, c='b', lw=1, label="Activity detector N°3", zorder=1) # Синий график
ax.plot(X, Y4, c='g', lw=1, label="Activity detector N°4", zorder=1) # Зеленый график
#ax.plot(X, Y5, c='m', lw=1, label="Activity detector N°5", zorder=1)
#ax.plot(X, Y6, linewidth=0, marker='', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Подробный тренд активности", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Время с")
ax.set_ylabel("Активность МБк")

ax.legend()

def text(x, y, text):
    ax.text(x, y, text, backgroundcolor="white",
            ha='center', va='top', weight='bold', color='blue')

RV = str(round((max(Y4)/max(Y1)*100),2))
#bottom, left, right, center
ax.text(4320, -130000, "Радиохимический выход - " + RV + "%" ,
        fontsize=10, ha="right", color='.5')

plt.show()
