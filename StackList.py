class StackList:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, item):
        self.top += 1
        if self.top < len(self.stack):
            self.stack[self.top] = item
        else:
            self.stack += [item]  # Manually increase size

    def pop(self):
        if self.top == -1:
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

s = StackList()
s.push(5)
s.push(10)
print(s.pop())  
print(s.pop())  
print(s.pop())  