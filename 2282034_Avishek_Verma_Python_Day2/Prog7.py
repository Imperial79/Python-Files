'''
Frequency of each word in a line

line = input("Enter a line: ").lower()

for i in line.split(" "):
    print("{} = {}".format(i,line.count(i)))'''
    
line = input("Enter a line: ").lower().split()
d = []
for i in line:
    c=line.count(i)
    if i not in d:
        d.append(i)
        print(i," ", c)

    
        