'''Generate a string by removing the ith character from a given string.'''

line= input("Enter a string: ")
i = int(input("Which ith character you want to remove? "))

print(line[:i] + line[i+1:])