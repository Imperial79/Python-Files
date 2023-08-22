lastNo = int(input("Enter the range: "))
sums = 0
for num in range(2, lastNo):
    count = 0
    for i in range(1, num):
        if (num % i == 0):
            count += 1
    if (count < 2):
        print(num)
        sums += num
print("Sum = {}".format(sums))
