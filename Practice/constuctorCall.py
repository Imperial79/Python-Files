class A:
    def __init__(self):
        print('This is A')


class B(A):
    def __init__(self):
        super().__init__()
        print('This is B')


class C(A):
    def __init__(self):
        super().__init__()
        print('This is C')


class D(B, C):
    def __init__(self):
        super().__init__()
        print('This is D')


c = D()
