# Копирование списков copy() - list()
import copy

a = [1, 2, 3]

# три способа скопировать список
b = a.copy()
c = list(a)
d = a[:]

b[1] = 'dsfaf'
c[0] = 'qq'
d[2] = [9, 10]

print('b = ', b)
print('c = ', c)
print('d = ', d)


# DEEPCOPY

# Функция copy()
new_d = d.copy()
new_d2 = list(d)
new_d3 = d[:]
new_d3[2][0] = 43
print(new_d3)  # [1, 2, [43, 10]]
print(d)  # [1, 2, [43, 10]]  ТАК НЕ ДОЛЖНО БЫТЬ.

# Функция deepcopy() -> РАБОТАЕТ КАК НАДО!!!
new_arrayA = [1, 2, [8, 9]]
new_arrayB = copy.deepcopy(new_arrayA)
new_arrayA[2][1] = 99
new_arrayB[2][1] = 9999

print("new_arrayA = ", new_arrayA)
print("new_arrayB = ", new_arrayB)
