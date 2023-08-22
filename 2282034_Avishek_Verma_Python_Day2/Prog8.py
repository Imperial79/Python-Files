'''
8. Find words which are greater than some given length k.
'''

line = input("Enter a line: ").split()
k = int(input("enter length: "))

for i in line:
    if len(i)>k:
        print(i, end=" ")