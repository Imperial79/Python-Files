'''
Accept a sequence of colon separated numbers from user and generate a list which contains every 
number.
Sample 
Input: 55:66:77:99:88:11
Output: [55,66,77,99,88,11]
'''

str = input("Enter the string: ")
arr = str.split(":")
arr = [int(x) for x in arr]
print(arr)