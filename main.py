from display import display
from pop import pop
from push import push
globalstack =[]
# check if globalstack size is 0 if yes intialize with sample size 10
if len(globalstack) == 0:
    globalstack = [None] * 10
    print("Stack initialized with size 10")
while(1):
    print("Enter the option \n1. Push\n2. Pop\n3. Display\n4. Exit")
    str = input("Enter your choice: ")
    if str == '1':
        str1 = input("Enter the value to be pushed: ")
        push(globalstack, str1)
    elif str == '2':
        print("Pop operation")
        pop(globalstack)
    elif str == '3':
        print("Display operation")
        display(globalstack)
    else:
        print("Exiting the program")
        break
    