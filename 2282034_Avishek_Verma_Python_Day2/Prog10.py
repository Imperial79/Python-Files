line = input("enter a line: ").split("_")
c = 0
for i in line:
    print(i.capitalize(), end='')

print()
        
for i in line:
    c+=1  
    
    if(c==1):
        print(i, end='')
        continue
    else:
        print(i.capitalize(), end='')
    


