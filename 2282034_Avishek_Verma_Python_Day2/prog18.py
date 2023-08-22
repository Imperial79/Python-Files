start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

for i in range(start, end+1):
    a = str(i)
    if (int(a[0]) % 2 == 0 and int(a[1]) % 2 == 0 and int(a[2]) % 2 == 0):
        print(a, end=', ')
