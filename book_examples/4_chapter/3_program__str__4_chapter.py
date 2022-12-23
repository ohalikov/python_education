name = 'Henny'

# name[0] = 'P'  # будет ошибка, строки не изменяемый тип данных

# Результат замены который надо сохранять. Новую строку возращает
print(name.replace('H', 'P'))

print('V' + name[1:])
# print(name)  # Ничего не изменится. Будет Penny

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:])
print(letters[1:3])
print(len(letters))
print(
    f'Выглядит так всего 26 символов \n(0, {len(letters[0:-2])})\n{letters[0:-2]}')
print(letters[::4])  # каждый 4 символ

print(letters[-1::-1])  # полный реверс
print(letters[::-1])
