person = {'first_name' : 'Иван',
          'last_name' : 'Иванов',
          'born' : 1980,
          'dept' : 'IT'}

# Добавление элементов в словарь
person['languages'] = ['Python', 'C++']

# Измение элемента в словарь
person['languages'] = ['HASKELL']


print(person.items(), "\n\n")


# Проход по всем элементам (ключ, значение)
for key, value in person.items():
    print(f"key = '{key}' -> value = '{value}'" )


# Взять элемент словаря по его ключу
print(f"\n\n{person.get('borne')}")


# Проверка определенного ключа в словаре
print("'dept' in  person.keys() =>", 'dept' in  person.keys())

# Проверка наличия определенного значения в словаре
print("1980 in person.values() =>", 1980 in person.values())

# Проверка пары ключ-значение: Метод .items()
print("('born', 1980) in person.items() =>", ('born', 1980) in person.items())
