num = [1,1,3,4,5,5,9]

num2 = []

for i in num:
    if(i not in num2):
        num2.append(i)
print(num2)