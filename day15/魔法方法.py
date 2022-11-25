class A:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        return int(self.x)+int(other.x)
a = A(3.3)
b = A(5.2)
print(a+b)
