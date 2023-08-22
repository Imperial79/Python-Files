# Write a script that prompts the user to input a year and determine whether that year is a leap year or not.

year = int(input('Enter year: '))

if ((year % 400) or (year % 100 != 0) and (year % 4 == 0)):
    print('Leap Year !')
else:
    print('Not a Leap Year !')
