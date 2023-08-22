
with open('file1.txt', 'r') as file1:
    x = file1.read()
    print(x)

with open('newFile.txt', 'w') as newFile:
    newFile.write(x)
