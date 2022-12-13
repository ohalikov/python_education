import random

RANGE_NUMBERS = {'start_range': 0, 'end_range': 20}
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
        b = get_new_value_not_equal_zero(RANGE_NUMBERS)
    return a/b


OPERATORS_MAP = {
    "add": add,
    'diff': difference,
    "multiply": multiply,
    'division': division
}


'''
    structure_elements = [
        {
            "left_operand": 'value',
            "right_operand": 'value',
            "operator": "multiply"
        },
    ]
'''


def get_left_and_right_operands(dict_range_numbers):
    while True:
        operand_1 = get_random_value(dict_range_numbers)
        if operand_1 == 0:
            continue

        operand_2 = get_random_value(dict_range_numbers)
        if operand_1 >= operand_2:
            return operand_1, operand_2
        # if operand_2 >= operand_1:
        #     return operand_2, operand_1


def get_generation_operations(count):
    structure_ements = []
    for i in range(count):
        left_operand, right_operand = get_left_and_right_operands(
            RANGE_NUMBERS)
        key_operand, function_for_operand = random.choice(
            list(OPERATORS_MAP.items()))

        inner_structure = {
            "left_operand": left_operand,
            "right_operand": right_operand,
            "operator": key_operand,
            "result": function_for_operand(left_operand, right_operand)
        }
        structure_ements.append(inner_structure)
    return structure_ements


if __name__ == '__main__':
    structure_ements = get_generation_operations(COUNT_EXAMPLES)
    print('structure_elements', structure_ements)
