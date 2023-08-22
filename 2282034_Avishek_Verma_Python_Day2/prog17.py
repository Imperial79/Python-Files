bin = input("Enter the list of binary with ',': ").replace(' ', '').split(',')


def binaryToDecimal(binary):

    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


for i in bin:
    if (binaryToDecimal(int(i)) % 3 == 0):
        print(i, end=', ')
