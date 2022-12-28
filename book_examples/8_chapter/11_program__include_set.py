# { выражение for выражение in итерабельный объект if условие}

a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)


# Создаем неизменяемое множество с помощью функции frozenset()

print(frozenset([3, 2, 1]))
print(frozenset(set([2, 1, 3])))
print(frozenset((2, 3, 1)))
# frozenset( {1,2,3} )

fs = frozenset([3, 2, 1])
print(fs.add(4))  # ОШИБКА!!!
