

class CatClass:
    # Всегда внутри класса необходимо прописывать метод инициализации
    # чтоб создать объект этого класса. И снабдить его аргументом self
    # который будет ссылаться на этот же объект
    def __init__(self, color) -> None:
        self.color = color
        self.type_ = 'cat'
    

    def meow(self):
        for i in range(3):
            print('Meow')

    
    def info(self):
        print(self.color, self.type_)


Matroskin = CatClass('grey')
# Matroskin.info()

# >>> Публичное изменение
# Matroskin.type_ = 'dog' - это не логично, поэтому нужно сделать атрибут частным

# >>> Приватный/Частный доступ
# 1 Способ.
    # self.color = color
    # self._type_ = 'cat'  ->  
    # Теперь это условно частный атрибут класса, так как всё равно можно его изменить


# 2 Способ.
    # self.color = color
    # self.__type_ = 'cat'  -> это действительно предотвращает доступ к атрибуту класса извне
    # выведет ошибку при доступе Matroskin.__type_


# НООООООООООООООООООООООООООО
# и это можно обойти если поставив  _CatClass перед __type 
# _CatClass__type_ = 'dog'  // выведет dog


# >>> Наследование (inheritance)
# Предполагает, что один класс наследует атрибуты и методы другого.
# В этом случае говорят про РОДИТЕЛЯ или СУПЕРКЛАСС (parent class, base class) 
# и ПОТОМКА или ПОДКЛАСС (child class, derived class)


class Animal:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length

    
    def eat(self):
        print('Eating')


    def sleep(self):
        print('Sleeping')



# ЕСЛИ МЫ ХОТИМ добавить Атрибут в классе-потомке
# сохранив атрибуты родителького класса, нам нужно их вызвать
# явным образом с помощью функции super()
# class Bird(Animal):
#     def __init__(self, weight, length, flying_speed):
#         super().__init__(weight, length)  # Вызываем метод init класса Animal
#         self.flying_speed = flying_speed  # км/ч
#     def move(self):
#         print('Flying')


# pigeon = Bird(0.3, 30, 200)


# print(pigeon.weight, pigeon.length, pigeon.flying_speed)
# pigeon.move()
# pigeon.eat( )


class Bird(Animal):
    def __init__(self, weight, lenght, flying_speed):
        super().__init__(weight, lenght)
        self.flying_speed = flying_speed

    
    def put_shit(self):
        print("I put shit, ha ha")



vorobey = Bird(0.1, 20, 1000)
vorobey.put_shit()


# >>> ПЕреопределение класса

class Flightless(Animal):
    def __init__(self, running_speed):
        self.running_speed = running_speed

    def move(self):
        print('Running')
    

ostrich = Flightless(60)
ostrich.move()
ostrich.sleep()
print(ostrich.running_speed)


class Fish:

    def swim(self):
        print("Swimming")


class Bird2:
    def fly(self):
        print('Flying')


class SwimmingBird(Bird2, Fish):
    pass


duck = SwimmingBird()

duck.fly()
duck.swim()


# >>> Полиморфизм - poly morph
# Один и тот же объект может принимать разные формы. 
# Операторы, функции и объекты могут взаимодействовать с различными типами данных.


# Полиморфизм оператор +
'''
    2 + 2
    'классы' + ' и ' + 'объекты'
'''
# Полиморфые функций на примере len

'''
    len('Программирование на питоне')  -> 26 символов
    len(['Программирование', 'на', 'Питоне' ]) -> 3
    len({0:'Программирование'}, 1: 'на', 2: 'Питоне'}) -> 3
    import numpy as np
    print(len(np.array([1,2,3]))) -> 3
'''

# Полиморфизм классов

'''
Предполагает, что у разных, не связанных 
между собой классов могут быть 
методы с одинаковыми названиями
'''

class CatClass:
    def __init__(self, name, color):
        self.name = name
        self._type_ = 'кот'
        self.color  = color

    def info(self):
        print(f'Меня зовут {self.name}, я {self._type_}, цвет шерсти {self.color}')
    
    def sound(self):
        print('Я умею мяукать')


class DogClass:

    def __init__(self, name, color) -> None:
        self.name = name
        self._type_ = 'пес'
        self.color = color

    def info(self):
        print(f'Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}')
    
    def sound(self):
        print('Я умею лаять')


cat = CatClass('Бегемот', 'Черный')
dog = DogClass('Барбос', 'серый')
print('\n\n\n\n')
for animal in (cat, dog):
    animal.info()
    animal.sound()


# Парадигма программирования

'''
    2 вида:
    - Императивное (imperare - властвовать, повелевать), мы говорим компьютеру, что нужно сделать.
        - Процедурное
        - Объектно-ориентированное
    - Декларативное
        - Функциональное
        - Логическое
        - Математическое

'''



class Person():
    def __init__(self, name, surname, height, weight):
        self.name = name
        self.surname = surname
        self.height = height
        self.weight = weight

    def say(self):
        print()