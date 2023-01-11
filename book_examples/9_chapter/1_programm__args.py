def agree():
    return True


if agree():
    print("Ablabla")
else:
    print("NOOOOOOO")


# Аргументы и параметры
def echo(anything):
    return anything + ' ' + anything


res_echo = echo('Rumplestilstkin')
print(res_echo)


# NONE - это не то же самое что и FALSE (оно им не является)
def whatis(thing):
    if thing is None:
        print(thing, "is NONE")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")


whatis(None)
whatis(True)
whatis(False)

# РАЗНИЦА МЕЖДУ ПАРАМЕТРОМ И АРГУМЕНТОМ.
# Аргументы передаются в функцию при ее вызове.
# Параметры - это принятый функцией аргумент.

# Позиционные аргументы


def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken', 'cake'))


# Аргументы - ключевые слова
# Для того чтобы избежать путаницы с позиционными аргуентами
# вы можете указать аргументы с помощью имен соответствующих параметров.

print(menu(entree='beef', dessert='bagel', wine='bordeaux'))


def new_menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'desert': dessert}


print(new_menu(wine='sdafad', entree='afsfadsfasd'))

# НЕ ИСПОЛЬЗОВАТЬ В КАЧЕСТВЕ ПАРАМЕТРОВ ПО УМОЛЧАНИЮ СПИСОК + СЛОВАРЬ.
# ====================================================================


# EXAMPLE 1:
# каждый раз должна запускаться с новым пустым списком result
# добавлять в него аргумент arg, а затем выводить на экран
# список, состоящий из одного элемента.
print('=================================================')


def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('a')
buggy('b')

print('\n============= Ниже корректная работа ============')


def works(arg):
    result = []
    result.append(arg)
    return result


print(works('a'))
print(works('b'))


print('\n============= Ниже корректная работа ============')


def nobuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


nobuggy('a')
nobuggy('b')

# ====================================================================
print("ПОЛУЧАЕМ / РАЗБИВАЕМ аргументы -> ключевые слова с помощью символа *")
# ====================================================================


def print_args(*args):  # кортеж
    print('Positional argument tuple:', args)


print_args(3, 2, 1, 'wait!', 'uh...')  # будет кортеж аргументов
# (3, 2, 1, 'wait', 'uh')


def print_more_args(requeired1, requeired2, *params):
    print('Need this one:', requeired1)
    print('Need this one too:', requeired2)
    print(params)


print_more_args('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
