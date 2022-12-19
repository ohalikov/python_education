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

for day, fruit, drink in zip(days, fruits, drinks):
    print("day: => ", day, '\n', "fruit: => ",
          fruit, '\n', "drinks: => ", drink, '\n')
