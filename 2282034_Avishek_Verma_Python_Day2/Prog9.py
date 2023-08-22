line = input("Enter a line: ").split()

for i in line:
    if len(i)%2 == 0:
        print(i, end=" ")