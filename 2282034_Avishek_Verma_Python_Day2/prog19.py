lst = [21, 77, 76, 23]
arr = []
sum = 0
for i in lst:
    a = str(i)
    for j in range(0, len(a)):
        sum += int(a[j])
    arr.append(sum)
    sum = 0
print(arr)
