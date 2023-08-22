'''
2. Create an OrdinaryCounter class, which mimics a physical clicker counter — the kind people
use at entrances to events and buildings to count how many people are coming in. It may
have an initializer that initializes count to zero, increment, to increment the counter, clear,
to reset the counter to zero, and get_value, to get counter value. Create a SpecialCounter class
that behaves somewhat like the OrdinaryCounter, but always increment by two instead of
one, and also has functionalities to decrement counting.
'''


class OrdinaryCounter:

    def __init__(self):
        self.i = 0

    def increment(self):
        self.i += 1

    def reset(self):
        self.i = 0

    def get_value(self):
        print("i ORD---->",   self.i)


class SepcialCounter(OrdinaryCounter):
    def __init__(self):
        super().__init__()

    def increment(self):
        self.i += 2

    def get_value(self):
        print("i SPC---->",   self.i)

    def decrement(self):
        self.i -= 1


def main():
    obj1 = OrdinaryCounter()
    obj2 = SepcialCounter()
    again = True
    while (again):
        print('1. Increment Ord')
        print('2. Reset Ord')
        print('3. Get Value Ord')
        print('4. Incrememnt Spc')
        print('5. Decrement Spc')
        print('6. Get Value Spc')
        print('7. Exit')

        ch = int(input())

        if ch == 1:
            obj1.increment()
        elif ch == 2:
            obj1.reset()
        elif ch == 3:
            obj1.get_value()
        elif ch == 4:
            obj2.increment()
        elif ch == 5:
            obj2.decrement()
        elif ch == 6:
            obj2.get_value()
        elif ch == 7:
            again = False
        else:
            print('Invalid request')


main()
