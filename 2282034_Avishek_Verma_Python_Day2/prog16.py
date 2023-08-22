str = input("Enter the list of string with ',': ").replace(' ', '').split(',')
str.sort()
print(', '.join(str))
