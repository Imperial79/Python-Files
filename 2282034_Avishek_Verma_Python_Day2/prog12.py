line = input("Enter a line: ").split()

for i in line:
    if i.startswith('M'):
        print(i, end=' ')

