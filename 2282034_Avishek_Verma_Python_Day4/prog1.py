'''
1. Write a function display_student() that accepts student name, and her/his degree and display
both. If the degree is missing in the function call, assign default value ‘MCA’ to it. 
'''


def display_student(name, degree='MCA'):
    print("Name:", name)

    print("Degree:", degree)


n = input("Enter name: ")
d = input("Enter degree: ")

if d.strip() == '':
    display_student(n)
else:
    display_student(n, d)
