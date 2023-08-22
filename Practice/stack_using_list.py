# Stack using List
def push():
    element = int(input('Enter element to push: '))
    stack.append(element)
    display()

def pop():
    stack.pop()
    display()

def display():
    print('stack-----> ', stack)

stack = []

while True:
    print('1. Push')
    print('2. Pop')
    print('3. Exit')
    choice = input('Enter choice (1, 2, 3): ')

    if(choice == '1'):
        push()
    elif(choice == '2'):
        pop()
    elif(choice == '3'):
        break
    else: 
        print('Invalid Choice')