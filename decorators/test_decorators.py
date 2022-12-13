def new_function(callback_function):
    def wrapper():
        print("this is wrapper logic")
        callback_function()
    return wrapper


# @new_function  # раскоментировать
def test():
    print("Hello")


# test()  # раскоментировать


test = new_function(test)
test()
