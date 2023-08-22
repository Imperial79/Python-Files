from math import pow, factorial

n = int(input('Enter the range: '))
sum = 0
for i in range (1, n+1):
    if(i  == n):
        print(pow(i,i) , '/' , i,'! ',end = '')
    else:
        print(pow(i,i) , '/' , i,'! + ',end = '')
    sum += pow(i,i)/factorial(i)
print(' = ', int(sum))