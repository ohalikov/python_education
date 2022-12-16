import random
import pprint


def add(a, b):
    return a + b


def difference(a, b):
    return a - b


def multiply(a, b):
    return a*b


def division(a, b):
    if b == 0:
        pass
        # b = get_new_value_not_equal_zero(RANGE_NUMBERS)
    remainder = a % b
    return a//b, b, remainder


OPERATORS_MAP = {
    "add": add,
    'diff': difference,
    "multiply": multiply,
    'division': division
}


def get_random_operation():
    items = OPERATORS_MAP.items()
    print(items)
    return random.choice(list(items))


print(get_random_operation())
