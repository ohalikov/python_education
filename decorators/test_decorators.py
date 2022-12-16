'''
    Декораторы -> обертка над функией
    
    Декоратор - это функция, которая позволяет обернуть другую функцию для расширения её функциональности без непосредственного изменения её кода. 
    Вот почему декораторы можно рассматривать как практику метапрограммирования, 
    когда программы могут работать с другими программами как со своими данными.
'''


def new_function(callback_function):
    def wrapper(value):
        print("this is wrapper logic")
        callback_function(value)
    return wrapper


# @new_function  # раскоментировать
def test(value):
    print(f"Hello {value}")


# test()  # раскоментировать


test = new_function(test)
test("qq")
