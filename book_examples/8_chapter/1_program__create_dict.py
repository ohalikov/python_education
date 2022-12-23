# Ассоциативный массив, хэш - таблица
bierce = {
    "day": "a",
    "positive": "m",
    "misfortune": "f",
}

print(bierce)

# Создание словаря передав именованные аргументы
# и значения в функцию dict()

# Traditional way
acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
# Another way
acme_customer_2 = dict(first="Wile", middle="E", last="Coyote")
third_dict = dict(my_name="Ivan", surname="Ivanov",
                  middle_name="Иванович", work="")
four_dict = dict(first_day='Monday', second_day='Thusday',
                 third_day='Wednesday')


print(acme_customer_2)
print(third_dict)
print(four_dict)
