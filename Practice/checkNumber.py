#WAP a python program to validate Phone Number with conditions: 
# 1. Must be only numbers, 2. Must start with (6, 7, 8, 9), Must have length of 10


def validateNumber(number):
    for i in number:
        if(type(i) == int and len(str(i))==10 and (str(i)[0] in ['9','8','7','6'])):
            print(str(i) + ' is a Phone Number')



numbers = [11111, '9093086276', 2632613264, 99889981, 8888, 8653826902, 7333747219, 6321459874]

validateNumber(numbers)



