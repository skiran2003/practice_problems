class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    def peek(self):
        if not self.stack:
            raise IndexError("peek from empty stack")
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)       
    def clear(self):
        self.stack.clear()
    def display(self):
        return self.stack.copy()

# Creating object of Stack and performing operations   
s= Stack()

# Pushing elements onto the stack and displaying the stack
s.push(1)
s.push(2)
s.push(3)
print(f'Elements of the stack are {s.display()}')

# Popping an element and displaying the stack
s.pop()
print(f'Elements of the stack after popping an element {s.display()}')
s.push(4)

# Displaying the top element of the stack
print(f'Top element of the stack is {s.peek()}')

# Checking the size of the stack
print(f"Size of the stack is {s.size()}")

# Clearing the stack
s.clear()

# Displaying the stack after clearing it
print(s.display())

