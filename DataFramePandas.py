import pandas as pd
import matplotlib.pyplot as plt
import sys
help(pd)
#Объект DataFrame лучше всего представлять себе в виде обычной таблицы
# и это правильно, ведь DataFrame является табличной структурой данных.
# В любой таблице всегда присутствуют строки и столбцы. Столбцами в объекте DataFrame
# выступают объекты Series, строки которых являются их непосредственными элементами.

df = pd.DataFrame({'country': ['Kazahstan', 'Russia', 'Belarus', 'Ukraine'],
                   'population': [14.04, 143.5, 9.5, 45.5],
                  'square': [22343, 2342343, 34342, 34243]
                   })
print(df)

#Извлечение столбца
print('\n')
print("Извлечение столбца")
print(df[['country']])

print('\n')
print("Извлечение нескольких столбцов")
print(df[['country','population']])

print("FFf")
print(df.columns)

print()

df2 = pd.DataFrame({'country': ['Kazahstan', 'Russia', 'Belarus', 'Ukraine'],
                   'population': [14.04, 143.5, 9.5, 45.5],
                  'square': [22343, 2342343, 34342, 34243]
                   }, index = ['KZ', 'RU', 'BY', 'UA'])

#Индексам можно давать названия (метод не выпадает из списка)

df2.index.name = 'Country Code'
print(df2)


print("Обращение по индексу")
print(df2.loc['KZ'])



print("Обращение по номеру индексу")
print(df2.iloc[1])

print('\n')
print("Можно делать выборку по индексу и интересующим колонкам:") #Но почему-то обратиться к фрэйму по двум индексам сразу нельзя
print(df2.loc[['KZ', 'RU'], 'population'])

print('\n')
print("Обращение через переменную")
kz_poperty = 'KZ'
print(df2.loc[kz_poperty])

#Можно выводить записи по условиям
print('\n')
print("Выборка по условиям")
print(df2[df2.population > 10][['country', 'square']])

print("DDDDD")
print(df2.population)

#Образаться к столбцам можно двумя способами:
#df.population и df['population']


#Добавление столбца
df2['density'] = df2['population'] / df2['square'] * 1000000
print(df2)

#Удаление столбца
df2.drop(['density'], axis = 'columns') #Почему-то не работает
del df2['density'] #Можно удалить так
print('\n')
print(df2)


df2 = df2.rename(columns={'country' : 'COUNTRY'})
print('\n')
print(df2)


#Запись DataFrame в CSV файл
df2.to_csv("filename.csv") #Так же можно передавать кучу параметров (коидровку, разделитель и тд) Надо смотреть документацию


#Чтение из CSV файла
df3 = pd.read_csv('filename.csv') #, sep=',')
print(df3)

print('\n')
#Группировка данных
titanic_df = pd.read_csv('titanic.csv')
print(titanic_df)
print('\n' + 'Head')
print(titanic_df.head(6))
print(titanic_df.columns)

print('\n' + 'Сколько мужчин и женщин выжило')
print(titanic_df.groupby(['Sex', 'Survived'])['PassengerID'].count())

print('\n' + 'Сколько мужчин и женщин было в каких классах через group by')
print(titanic_df.groupby(['Sex', 'PClass']) ['PassengerID'].count())

#Сводная таблица
print('\n' + 'Сколько мужчин и женщин было в каких классах через сводную таблицу')
pvt = titanic_df.pivot_table(index = ['Sex'], columns = ['PClass'], values = 'Name', aggfunc = 'count')
print('\n', pvt)

print('\n' + 'Итого женщин в классах было:')
print(pvt.loc['female'])

#Чтобы удалить класс *, сделаем выборку только по нужным классам
print('\n' + 'Итого женщин в нормальных классах было:')
print(pvt.loc['female', ['1st', '2nd', '3rd']])





apple_df = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
apple_df.index = pd.to_datetime(apple_df.index) #Так как мы используем дату в качестве индекса, а потом по ней сортируем, то лучше привести её к питоновскому формату (заменил 2012-02/23 на 2012-02-23)

print('\n', apple_df)

#Сортируем по индексу (по дате)
apple_df = apple_df.sort_index()
print('\n Информация по акциям')
print(apple_df.info())

print('\n Средняя цена акции на закрытии')
print(apple_df.loc['2012-Feb', 'Close'].mean()) ##Вместо Feb можно написать 02

print('\n Средняя цена акции на закрытии c 2012 по 2015')
print(apple_df.loc['2012-Feb':'2015-Feb', 'Close'].mean()) ##Вместо Feb можно написать 02


print('\n Средняя цена акции на закрытии по неделям')
print(apple_df.resample('W')['Close'].mean())

#Вывод графика
#Выводим цену акций на момент закрытия с 2012 по 2017
new_sample_df = apple_df.loc['2012-Feb':'2017-Feb', ['Close']]
new_sample_df.plot()
plt.show()
