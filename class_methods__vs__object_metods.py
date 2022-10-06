class Rectangle():
    def __init__(self, w, h) -> None:
        self.w = w
        self.h = h
        
    def area(self):
        return self.w * self.h
    
    def perimeter(self):
        return 2 * (self.w + self.h) 
    
    
class Square(Rectangle):
    def __init__(self, side_one):
        super().__init__(side_one, side_one)
        self.side_one = side_one


r = Rectangle(4, 5)
s = Square(7)

print(s.area())
print(s.side_one)




class C:
    x = 2  # class variable
    def __init__(self, y):
        self.y = y  # instance variable

C.x

c1 = C(3)
print(c1.x)
print(c1.y)


class D:
    x = []
    def __init__(self, item):
        self.x.append(item)

d1 = D(1)
d2 = D(2)
d2 = D(3)


print(d1.x)


class MyClass:
    pass

my_inst = MyClass()
type(my_inst)

my_inst.__class__
print(issubclass(MyClass, object))


class Rectangle2D(object):
    def __init__(self, width, height, pos = None, color = 'blue'):
        self.width = width
        self.height = height
        self.pos = pos or [0,0]
        self.color = color
        
r1 = Rectangle2D(5,3)
r2 = Rectangle2D(7,9)
r1.pos[0] = 5
r1.pos[1] = 76

r2.pos[0] = 545
r2.pos[1] = 276

print(r1.pos[0], r1.pos[1])
print(r2.pos[0], r2.pos[1])


class Foo(object):
    foo = 'attr foo of Foo'
    

class Bar(object):
    foo = 'attr foo of Bar'
    bar = 'attr bar of Bar'
    
    
class FooBar(Foo, Bar):
    foobar = 'attr foobar of Foobar'
    
    
fb = FooBar()
print(fb.foo)

print(FooBar.mro())