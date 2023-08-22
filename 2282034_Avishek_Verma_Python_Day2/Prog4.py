'''String Palindrome'''

line = input("Enter a string: ")
#print(line[::-1].replace(" ", ""))

if(line[::-1].replace(" ", "").lower() == line.replace(" ", "").lower()):
    print("Palindome")
else:
    print("Not palindrome")