def pyramid(symbol = ' * ', row = 6):
    s=row
    for i in range (row):
        for j in range (i):
            print(symbol, end = '')
        print('')


symbol = input('Enter the symbol of pyramid: ')
row = input('Enter rows for pyramid: ')

if(symbol == '' and row == ''):
    pyramid()
elif (symbol != '' and row != ''):
    pyramid(symbol, int(row))
else:
    pyramid(symbol)