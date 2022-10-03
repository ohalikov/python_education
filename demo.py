def print_hello():
    print("hello")
    

def print_hello_world():
    print("hello world!!!!")
    

print(__name__)
if "__main__" == __name__:
    print_hello_world()