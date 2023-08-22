
def min(a,b):
    if(a<b):
        return a
    return b

def hcf(a,b):
    small = min(a,b)  
    if(a % small == 0 and b % small == 0):
        return small
    for i in range (int(small/2), 1, -1):
        if(a % i == 0 and b % i == 0):
            return i
    return 1


a=int(input('Enter 1st num: '))
b=int(input('Enter 2nd num: '))

print("HCF is", hcf(a,b))

