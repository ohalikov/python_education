# Преобразование с помощью функции dict()

lol_array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
lol_tuple = [('a', 'b'), ('c', 'd'), ('e', 'f')]
lol_string = ['ab', 'cd', 'ef']

# Список содержащий двухэлементные списки
dict__lol_array = dict(lol_array)
# Список содержащий двухэлементные кортежи
dict__lol_tuple = dict(lol_tuple)
# Список содержащий двухсимвольные строки
dict__lol_string = dict(lol_string)


print("dict__lol_array->", dict__lol_array)
print("dict__lol_tuple->", dict__lol_tuple)
print("dict__lol_string->", dict__lol_string)


# Кортеж, включающий двухэлементные списки:
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))

# Список, содержащий двухсимвольные строки:
los = ['ab', 'cd', 'ef']
print(dict(los))
# Кортеж, содержащий двухсимвольные строки:
tos = ('ab', 'cd', 'ef')
print(dict(tos))
