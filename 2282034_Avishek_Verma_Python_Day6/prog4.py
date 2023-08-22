'''
4. Create a base class called Shape. Use this class to store values that could be used to compute the area of figures. Derive two specific classes called Triangle and Rectangle from the base Shape. Add to the base class, a constructor to initialize base class data members and another method display_area () to compute and display the area of figures. Redefine this method in the derived classes to suit their requirements. Use these three classes to design a program that will accept dimensions of a triangle and rectangle and display the area.
'''


class Shape:
    def __init__(self, area):
        self.area = area

    def display(self):
        print('Area', self.area)


class Triangle(Shape):
    def __init__(self, h, b):
        self.h = h
        self.b = b

    def display_area(self):
        super().__init__(0.5 * self.h * self.b)
        super().display()


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def display_area(self):
        super().__init__(self.l * self.b)
        super().display()


t = Triangle(12, 10)
t.display_area()

r = Rectangle(10, 5)
r.display_area()
