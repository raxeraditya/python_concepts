# __init__() method
# constructor is allways executed first. while call a class 
# The __init__ method is similar to constructors in C++ and Java script.
# create a variable within the class or method then allways use self just like this in js


# Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.sname = name
#   self.name is a variable to store class argument 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.sname)
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
name.mn(6,6)
