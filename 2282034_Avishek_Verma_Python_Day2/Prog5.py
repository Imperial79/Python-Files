'''Reverse word by word'''

line = input("enter a line: ")
str = line.split(" ")
print(" ".join(str[::-1]))