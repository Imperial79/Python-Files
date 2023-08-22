class Students:
    def __init__(this, name, roll):
        this.name = name
        this.roll = roll

    def display(this):
        print(this.name,',', this.roll)
        


arr = []

for i in range(3):
    print('------------ [',i+1,'] ----------------')
    arr.append(Students(input('Enter name: '), 
    int(input('Enter Roll: '))))
    

for i in range(3):
    print('------------- [ DISPLAYING ] ----------------')
    arr[i].display()