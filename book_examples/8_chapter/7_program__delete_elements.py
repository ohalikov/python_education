pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}

others = {
    'Marx': 'Groucho',
    'Howard': 'Moe'
}

pythons.update(others)

del pythons['Marx']

print(pythons)


del pythons['Chapman']
print(pythons)


# ФУНКЦИЯ POP
# тут объединены функция del и get()
# БУДЕТ ОШИБКА ЕСЛИ УДАЛИТЬ УДАЛЕННЫЙ ЭЛЕМЕНТ
len(pythons)
# Возращает значение по ключу. Удаление пары.
del_element = pythons.pop('Palin')
print(del_element)  # вывод значения

print(pythons.pop('First', None))


# ВКЛЮЧЕНИЯ СЛОВАРЕЙ.
word = 'letters'
letters_counts = {letter: word.count(letter) for letter in set(word)}
print(letters_counts)
