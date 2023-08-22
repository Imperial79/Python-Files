'''
Duplicate chararcters in string
'''

line = input("enter a line: ").lower()
arr = []

for i in line:
    if i in line.replace(i, "",1):
        print(i.replace(" ", ""), end="")
        line = line.replace(i, "")

