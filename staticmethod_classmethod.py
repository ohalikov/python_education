class MyClass:
    def method(self):
        '''
            При помощи параметра self методы экземпляра класса могут иметь свободный доступ к атрибутам и другим методам того же объекта. 
            Благодаря этому они на многое способны, когда речь заходит о модификации состояния объекта.
            Методы экземпляра также могут иметь доступ к самому классу — при помощи атрибута self.__class__. 
            Это означает, что они могут менять состояние не только объекта, но и класса.
        '''
        return 'instance method called', self  
    
    @classmethod    
    def classmethod(cls):
        '''
            Метод класса имеет доступ только к аргументу cls, он не может изменять состояние экземпляра объекта. 
            Для этого нужен доступ к self. 
            Методы класса могут изменять состояние класса в целом, что затронет и все экземпляры этого класса.
        '''
        return 'class method called', cls  
    
    @staticmethod
    def staticmethod():
        '''
            Методы такого типа не принимают в качестве параметра ни self, ни cls (хотя, безусловно, они свободно могут принимать другие параметры в любых количествах).
            Таким образом, статический метод не может изменять состояние ни объекта, ни класса. Виды данных, которые могут принимать статические методы, ограничены. 
            Эти методы помещаются в класс, просто чтобы они находились в пространстве имен этого класса, т. е., для организационных целей.
        '''
        return 'static method called'  # static method called
    
    

classM = MyClass()

print(classM.method())  # ('instance method called', <__main__.MyClass object at 0x7f6d61c965b0>)
print(classM.classmethod())  # ('class method called', <class '__main__.MyClass'>)
print(classM.staticmethod())  # static method called

