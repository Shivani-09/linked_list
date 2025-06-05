import array

class StackArray:
    def __init__(self, size):
        self.stack = array.array('i', [0]*size)
        self.top = -1
        self.size = size

    def push(self, item):
        if self.top < self.size - 1:
            self.top += 1
            self.stack[self.top] = item
        else:
            print("Stack Overflow")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1


sa = StackArray(3)
sa.push(1)
sa.push(2)
print(sa.pop())  
print(sa.pop())  
print(sa.pop())  