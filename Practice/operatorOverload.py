class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, o):
        return self.a * o

    def __mul__(self, o):
        return self.a / o


a = A(12)
print(a * 2)
