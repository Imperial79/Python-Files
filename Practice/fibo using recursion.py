def fibo(num):
    if num<=1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)

n = int(input('Enter the number of terms: '))

if n <= 0:
    print('Enter Valid positive integer')
else:
    for i in range(n):
        print(fibo(i))
