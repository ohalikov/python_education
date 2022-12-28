# множество похоже на словарь. В котором значения отброшены и оставлены только ключи.
#
# Пустое множество - это множество - это множество, содержащее 0 элементов.

empty_set = set()
even_numbers = {0, 2, 4, 6, 8}
print(type(even_numbers))

old_numbers = {1, 3, 5, 7, 9}
print(type(old_numbers))


# преобразование других типов данных с помощью функции set
print(set('letters'))
# {'l', 'r', 's', 't', 'e'}

# преобразование списка в множество
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))
# {'Dancer', 'Dasher', 'Mason-Dixon', 'Prancer'}

# А теперь из кортежа:
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))

# Когда мы передаем функции set() словарь, возращаются ключи:
print({'apple': 'red', 'orange': 'orange', 'cherry': 'red'})

# >>>
# ADD ELEMENT
s = set((1, 2, 3))
s.add(4)
print(s)

# Удаление элемента
s = set((1, 2, 3))
s.remove(3)
print(s)

# Интерируем по множествам с помощью for
furniture = set(('sofa', 'ottoman', 'table'))
for pice in furniture:
    print(pice)
