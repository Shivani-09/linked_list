
def push():
    n = int(input("Enter the element to be pushed: "))
    if len(stack) == 0:
        stack.append(n)
    else:
        stack.insert(0, n)
        print(n, "is pushed to the stack")
        print()

def pop():
    n = int(input("Enter the element to be popped: "))
    if len(stack) == 0:
        print("Stack is empty, cannot pop")
    else:
        print("Popped element:", stack.pop(0))
        print()

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements are:")
        for ele in stack:
            print(ele)
    print("Top of stack is:", stack[0])
    print()

stack =[]
while(1):
    print("Enter the option \n1. Push\n2. Pop\n3. Display\n4. Exit")
    str = input("Enter your choice: )
    if str == '1':
        print("Push operation")
        push()
    elif str == '2':
        print("Pop operation")
        pop()
    elif str == '3':
        print("Display operation")
        display()
    else:
        print("Exiting the program")
        break
    