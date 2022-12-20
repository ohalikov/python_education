# Преобразование в список результат работы функции range
number_list = list(range(1, 6))
print(number_list)

# СПИСКОВЫЕ ВКЛЮЧЕНИЯ. ГЕНЕРАТОРЫ СПИСКОВ
# [выражение for элемент in итерабельный объект]
# [выражение for элемент in итерабельный объект if условие]


# NEW EXAMPLE
new_number_list = [
    number
    for number in range(1, 6)
    if number > 3
]
print(new_number_list)


# NEW EXAMPLE
a_list = [number for number in range(1, 8) if number % 2 == 1]
print(a_list, '\n\n')  # [1,3,5,7]  Вывод нечетных чисел


# NEW EXAMPLE
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

print('\n\n')
rows = range(1, 4)
cols = range(1, 3)
cells = [
    (row, col)
    for row in rows if row > 1  # можно добавлять условие
    for col in cols
]
print(cells)
