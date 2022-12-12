# Создаем кортежи с помощью функции tuple()
max_list = ['Gruncho', 'Chico', 'Harpo']
new_tuple = tuple(max_list)
print(new_tuple, '\n=============================')


# Объединение кортежей с помощью оператора +
print(('Gruncho',) + ('Chici', 'Harpo', 'Giri'))


# Размножаем элементы с помощью оператора *
yoda_word_multiply = ('yoda',) * 3
print('=============================\n', yoda_word_multiply)
print(type(yoda_word_multiply))
