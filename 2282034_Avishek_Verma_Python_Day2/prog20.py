#   20. Break a list into chunks of size N.

str = input("Enter a string: ").split(" ")
n = int(input("How many parts to divide? "))

for i in range(0, len(str), n):
    print(str[i:i+n], end=', ')
