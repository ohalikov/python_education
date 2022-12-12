# Сравнение кортежей

a = (7, 2.1, 9.1)
b = (7, 2, 9.11)

print(f'''Поэлементное сравнение {a} и {b } ''')
print(f'a == b ? => {a == b}')

print(f'a <= b ? => {a <= b}')
print(f'a >= b ? => {a >= b}')


# Итерирование по кортежам
words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(word)

# ИЗМНЕНИЕ КОРТЕЖА
# >>> ЭТО НЕВОЗМОЖНО. Как и в случае со строками
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(id(t1))  # 140159499810368
print(id(t2))  # 140159543134672
t1 += t2
print(t1)
print(id(t1))


a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))  # ['ready', 'fire', 'aim']
