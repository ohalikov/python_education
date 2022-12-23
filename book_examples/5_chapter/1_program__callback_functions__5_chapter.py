def fun(a, b):
    sum = a + b
    if sum > 4:
        print("lox")
    else:
        print("pidr")
    return True


def another(func, aa, bb):
    func(aa, bb)
    # return True


print('=============')
another(fun, 1, 3)
