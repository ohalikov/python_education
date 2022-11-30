
'''
Типы данных: Изменяемые и неизменяемые.
К изменяемым относятся: dict, list, set, bytesarray

Пример №1:
    print(3+"df")  # error 'int' + 'str'

Пример №2:

    x1 = 3
    x2 = 'p'
    print(x1+x2)  
    >>> таже самаяошибка

Пример №3:
    a = 7
    print(a)
    b = a
    print(b)

    b = a + 4
    print(b)
    print(a) 
    >>> ответ 11

Пример №4
    print(9 % 5)  # остаток от деления первого числа на второе.
    divmod(9, 5)  # частное. Остаток (1, 4)
      
'''

p = divmod(10, 5)
print(p)

print(-5 ** 2)
print(0b10)
print(0o10)
print(0x10)
