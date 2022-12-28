# Объединяем словари с помощью конструкции {**a, **b}

first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
third = {'d': 'donuts'}
union_dicts = {**first, **second, **third}

print(union_dicts)


# Объединяем словари с помощью функции update()

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)

print(pythons)


# Кто победит ? Значение из первого словаря или Второго ? ВТОРОГО
f_dict = {'a': 1, 'b': 2}
second = {'b': 'platypus'}

first.update(second)
print(first)  # {'a': 'agony', 'b': 'platypus'}
