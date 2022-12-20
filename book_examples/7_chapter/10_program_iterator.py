cheeses = ['brie', 'gjetos', 'havarti']
for cheese in cheeses:
    if cheese.endswith('s'):
        print("i'll be eat anything that ends with 'i'")
        break
    elif cheese.startswith('q'):
        print("i wont eat anything that starts with 'g'")
        break
    else:
        print(cheese)
else:
    print("didnt find anythig that started with 'x'")


'''
Мы по-прежнему можем использовать опцинальный блок else 
если цикл for завершился без break
'''
print('\n\n')

cheeses2 = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:
    print('This is not much of a cheese shop, is it?')


# Итерируем по нескольким последовательностям
# с помощью функции zip()
'''
    Есть еще один хороший прием — параллельное итерирование по нескольким по-
    следовательностям с помощью функции zip():
'''

days = ['Monday', 'Tuesday', 'Wendsday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
deserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, desert in zip(days, fruits, drinks, deserts):
    print(day, ": eat", fruit, '- drink', drink, '- enjoy', desert)

# Функция zip позволяет пройти по нескольким последовательностям
# и создать кортежи из элементов с одинаковым смещением.

english = 'Monday', 'Tuesday', 'Wednesday'  # tuple
french = 'Lundi', 'Mardi', 'Mercredi'

# Объединим с помощью zip()
language_list = list(zip(english, french))
language_dict = dict(zip(english, french))
print(language_dict)
