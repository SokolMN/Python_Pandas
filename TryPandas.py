import pandas as pd

#Series
#Структура/объект Series представляет из себя объект, похожий
# на одномерный массив (питоновский список, например), но отличительной его чертой
# является наличие ассоциированных меток, т.н. индексов, вдоль каждого элемента из списка.
# Такая особенность превращает его в ассоциативный массив или словарь в Python.

my_series = pd.Series([5, 6, 7, 8, 9, 10])

print(my_series)

print(my_series.index)
print (my_series.values)

print(my_series[4])

#Индексы можно задавать явно
my_series2 = pd.Series([5,6,7,8,9,10], index= ['a', 'b', 'c', 'd', 'e', 'f'])
k = "f"
print(my_series2[k], " ", my_series2['f'])


#Можно сразу несколько значений изменить
my_series2['a', 'b', 'c']= 0
print(my_series2)

#Можно фильтровать по значениям
print(my_series2[my_series2>0])

#И применять математические функции
print(my_series2[my_series2>0] *2)


#Можно проинициализировать по-другому
my_series3 = pd.Series({'a':5, 'b':5})
print(my_series3)

##Проверка, что элемент по ключу есть в списке
print('a' in my_series3)

#Можно менять индексы
my_series3.index = ['A', 'B']

print(my_series3)

