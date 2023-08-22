name = input("Enter name: ").split()

for i in range(0, len(name)-1):
    print(name[i][0].capitalize(), end='. ')
print(name[len(name)-1].capitalize())