class Student:
    __desg = 'BCA'
    def __init__(this, roll, name):
        this.roll = roll
        this.name = name

    def display(this):
        print('---------DETAILS---------')
        print('Name ->', this.name)
        print('Roll ->', this.roll)
        print('Designation ->', this.__desg)

obj1 = Student(32301219050, 'Avishek Verma')
# print(obj1.__desg)

print(obj1.display())


