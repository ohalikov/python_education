# HOW TO START

## install FASTAPI

    https://bobbyhadz.com/blog/python-no-module-named-fastapi

## OPEN TERMINAL

    cd my_operations_generator/
    uvicorn main:my_own_api --reload --port 8500

## endpoint

    http://127.0.0.1:8500/operations/20

## Example JSON

[
{"left_operand":7,"right_operand":5,"operator":"division","result":1,"division_remainder":2},
{"left_operand":15,"right_operand":2,"operator":"diff","result":13},
{"left_operand":12,"right_operand":7,"operator":"diff","result":5},
{"left_operand":3,"right_operand":3,"operator":"division","result":1},
{"left_operand":12,"right_operand":1,"operator":"diff","result":11},
{"left_operand":11,"right_operand":11,"operator":"add","result":22},
{"left_operand":10,"right_operand":0,"operator":"diff","result":10},
{"left_operand":9,"right_operand":1,"operator":"diff","result":8},
{"left_operand":9,"right_operand":4,"operator":"multiply","result":36},
{"left_operand":15,"right_operand":1,"operator":"diff","result":14},
{"left_operand":5,"right_operand":0,"operator":"multiply","result":0},
{"left_operand":6,"right_operand":1,"operator":"multiply","result":6},
{"left_operand":6,"right_operand":5,"operator":"multiply","result":30},
{"left_operand":13,"right_operand":1,"operator":"division","result":13},
{"left_operand":1,"right_operand":1,"operator":"add","result":2},
{"left_operand":3,"right_operand":0,"operator":"multiply","result":0},
{"left_operand":5,"right_operand":3,"operator":"add","result":8},
{"left_operand":16,"right_operand":11,"operator":"division","result":1,"division_remainder":5},
{"left_operand":18,"right_operand":9,"operator":"diff","result":9},
{"left_operand":8,"right_operand":5,"operator":"add","result":13}
]
