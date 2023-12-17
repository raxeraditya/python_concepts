# create  a variable within a function then use self keyword 
# but create a function with many parameter they are not use self
# self only use for create a variable not use parameter

class myClass:
    def __init__(self,a ,b):
        print(a*b)# this is a parameter not use self
obj = myClass(5,2)

class mySclass:
    def __init__(self):
        self.a = 5
        self.b = 2
        print(self.a*self.b)# use self because this is variable not a prameter
