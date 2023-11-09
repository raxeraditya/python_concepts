#       agar kisi class variable ko localy(inside a function)use karna ho to self ka use karte he
#       jabki variable inside a class not inside a mehtod(funciton) tab ham self ka use jab variable
#       function ke andar ho to us case me print(self.a<self ka use nahi karna padta he kyoki vo local vriable) 
#       argument dene par sirf function me self dete [def name(self,a,b)] he na ki variable ko like[print(a*b)]
#       self ka means class ke object ke throgh ek method(function) ko call kiya ja sakta he agar hame 
#       method(function) ke andar ke variable ko class ke object ke throgh call karna ho to variable ke pehlt .self ka use karte he 

# class can be created multiple function and variable 

# class is a blueprint of a object
# object is the backbone of class 
# because through a object can call a classes function
# how to define a class name not define a space in class name
# class can define a camel case first letter is capital in each word without space
class DemoClass:
    a = 28 #run programe untill out a class can defined a object then call a function
    def sum(self):
        print(390+48)
object = DemoClass() # can define a object allways round bracket
print(object.a) # one class can define multiple object
# i created a car class then define farrari variable many car brand but call a any car brand through a object
# object can define allways outside a class
# function create outside a class and method can defined inside in class 
object.sum()
# self function ownself a object then can in anu othe object



# constructor not call they can be autometic executed
# but method(function) call through a object
class Demo:
    a = 65
    print(a)
# without self not create a method(function)
# without self not create a variable inside in method(function)

    def show(self):
        b = 67
        print(b)
        # a is outside the function and inside the class then use allways self method to print a variable
        print(self.a) # a is not defined when self not use because a is global inside a class 

obj = Demo()
obj.show()

class mam:
    def add1(self,a,b):
        print(a*b)
# argument not use self function
variable = mam()
variable.add1(6,8)