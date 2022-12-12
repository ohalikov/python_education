# Присвоить tuple нескольким переменным
# Деструктуризация или распаковка элементов
marx_tuple = ('Grouncho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(f'a = {a}, \nb = {b}, \nc = {c}\n===================')

# Использование кортежа для обмена значениями не используя доп.переменную
password = 'swordfish'
icecream = 'tuttifrutti'

print(f'old psw = {password}\nold icrm = {icecream}\n')

password, icecream = icecream, password
print(f'new psw = {password}\nnew icrm = {icecream}')
