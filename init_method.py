# __init__() method
# The __init__ method is similar to constructors in C++ and Java.
# Constructors are used to initializing the object’s state.
# Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. It runs as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.


# Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name
#   self.name is a variable to store class argument 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)

#   person ek class ka nam he chuki isme constructor ka use hua he isliye class me hame vo argument pass 
#   karna pad raha he jo self , name he name is a passing argument through a class
#   because init is executed without calling method(function)
p = Person('Nikhil')
p.say_hi()


class tor:
    a = 5
    def __init__(self):
        print(self.a)
    def mn(self,a,b):
        print(a*b)
        print("hey run")

name = tor()
name.mn(5,6)
