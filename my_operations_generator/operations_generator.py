import random
import pprint

RANGE_NUMBERS = {'start_range': 0, 'end_range': 20}
RANGE_NUMBERS_MULTIPLY = {'start_range': 0, 'end_range': 10}
RANGE_NUMBERS_DIV = {'start_range': 1, 'end_range': 10}

COUNT_EXAMPLES = 20


def get_random_value(dict_range_numbers):
    return random.randrange(dict_range_numbers['start_range'], dict_range_numbers['end_range'])


def get_new_value_not_equal_zero(dict_range_numbers):
    while True:
        value = get_random_value(dict_range_numbers)
        if value == 0:
            continue
        return value


def add(a, b):
    return a + b


def difference(a, b):
    return a - b


def multiply(a, b):
    return a*b


def division(a, b):
    if b == 0:
        b = get_new_value_not_equal_zero(RANGE_NUMBERS_DIV)
    remainder = a % b
    return a//b, b, remainder


OPERATORS_MAP = {
    "add": add,
    'diff': difference,
    "multiply": multiply,
    'division': division
}


def get_left_and_right_operands(dict_range_numbers, operator):
    operand_1 = None
    operand_2 = None
    while True:
        if operator == 'multiply':
            operand_1 = get_random_value(
                RANGE_NUMBERS_MULTIPLY)
            operand_2 = get_random_value(
                RANGE_NUMBERS_MULTIPLY)
        elif operator == 'division':
            operand_1 = get_random_value(
                RANGE_NUMBERS)
            operand_2 = get_random_value(
                RANGE_NUMBERS_DIV)
        else:
            operand_1 = get_random_value(
                dict_range_numbers)
            operand_2 = get_random_value(
                dict_range_numbers)

        if operand_1 == 0:
            operand_1 = None
            continue

        if operand_1 >= operand_2:
            return operand_1, operand_2


def get_inner_structure(left, right, operator, function):
    right_operand = right
    remainder = 0
    if operator == 'division':
        result_of_function, right_operand, remainder = function(left, right)
    else:
        result_of_function = function(left, right)

    if remainder != 0:
        inner_structure = {
            "left_operand": left,
            "right_operand": right_operand,
            "operator": operator,
            "result": result_of_function,
            "division_remainder": remainder
        }
    else:
        inner_structure = {
            "left_operand": left,
            "right_operand": right_operand,
            "operator": operator,
            "result": result_of_function
        }
    return inner_structure


def get_random_operation():
    return random.choice(list(OPERATORS_MAP.items()))


def get_generation_operations(count):
    structure_ements = []
    for i in range(int(count)):

        operator, calculating_function = get_random_operation()
        left_operand, right_operand = get_left_and_right_operands(
            RANGE_NUMBERS, operator)
        inner_structure = get_inner_structure(
            left_operand, right_operand, operator, calculating_function)

        structure_ements.append(inner_structure)

    return structure_ements


# >>> MAIN FUNCTION <<<
'''
    structure_elements = [
        {
            "left_operand": 'value',
            "right_operand": 'value',
            "operator": "multiply"
        },
    ]
'''
if __name__ == '__main__':
    structure_ements = get_generation_operations(COUNT_EXAMPLES)
    # pp = pprint.PrettyPrinter(width=60, compact=True)
    # pp.pprint(structure_ements)
