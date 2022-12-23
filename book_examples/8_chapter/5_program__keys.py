# dict_keys(['green', 'red', 'yellow'])
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(type(signals.keys()))  # dict_keys
keys = list(signals.keys())  # чтобы перевеси keys в list

print(keys)


# get values
values = list(signals.values())  # чтобы перевести values в list


print(signals.items())  # все элементы пары ключ значение кортежем в списке
# [('green', 'go'), ('red', 'smile for the camera'), ('yellow', 'go faster')]
list(signals.items())

print(len(signals))  # len() длина символов
