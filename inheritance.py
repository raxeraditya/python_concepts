class A:
    def first(self):
        print("hey class A")

class B(A):# to pass a class in paranthesis to use any method use to call B only
    def second(self):
        print("hey class B")

obj = B()
obj.first()

