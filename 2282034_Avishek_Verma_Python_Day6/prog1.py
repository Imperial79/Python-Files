'''
1. Define a class Employee to store information of an employee (empNo, name, department,
basicPay, DA, HRA and grossSalary). Write a constructor which will take as input the
empNo, name, department, basicPay for several employees. The program will calculate the
DA, HRA and total for each employee and define a method to display the details of the
employee having the highest gross salary.   
'''


class Employee:
    def __init__(self, empNo, name, dept, basicPay, da, hra):
        self.empNo = empNo
        self.name = name
        self.dept = dept
        self.basicPay = basicPay
        self.da = da
        self.hra = hra

    def calGrossSal(self):
        self. d = self.basicPay * (self.da/100)
        self. h = self.basicPay * (self.hra/100)
        return self.basicPay + self.d + self.h

    def display(self):

        print("Emp ID:", self.empNo)
        print("Name:", self.name)
        print("Dept:", self.dept)
        print("BAsic Pay:", self.basicPay)
        print("DA:", self.d)
        print("HRA:", self.h)
        print("GROSS SAL:", self.calGrossSal())


lst = []
n = int(input('Enter number of employees: '))
h = None
for i in range(n):
    print('------- Entering details for EMPLOYEE', i+1, '-------')
    name = input('Enter name: ')
    dept = input('Enter dept: ')
    basicPay = int(input('Enter Basic Pay: '))
    da = int(input('Enter DA: '))
    hra = int(input('Enter HRA: '))
    lst.append(Employee(i, name, dept, basicPay, da, hra))
    if(h == None):
        h = lst[0]
    else:
        if lst[i].calGrossSal() > h.calGrossSal():
            h = lst[i]

print('Employee with max gross sal')

h.display()
