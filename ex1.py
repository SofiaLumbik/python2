size=int(input('Введите размерность массива='))
M=[0]*size #заполнение массива нулями
from random import uniform #подключение функции uniform
for i in range(size): #перебор массива
    M[i]=uniform(1,71) #случайные числа от 1 до 71
print('Массив', M) #вывод массива
for i in range(size): #перебор индексов
    if M[i]==max(M): #находим максимальный элемент
        for i in range(i+1, size): #перебор индексов 
            M[i]=0 #заменяем элементы, стоящие после максимального, нулями
print('Изменённый массив', M) #вывод массива
