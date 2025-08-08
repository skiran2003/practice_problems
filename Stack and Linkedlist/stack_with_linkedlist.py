class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_value = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_value
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data
    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size
    def clear(self):
        self.top = None
        self.size = 0
    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
# Creating object of Stack and performing operations
s = Stack()
# Pushing elements onto the stack and displaying the stack
s.push(7)
s.push(2)
s.push(9)
print(f'Elements of the stack are {s.display()}')
# Popping an element and displaying the stack
s.pop()
print(f'Elements of the stack after popping an element {s.display()}')
s.push(5)  

# Displaying the top element of the stack
print(f'Top element of the stack is {s.peek()}')
# Checking the size of the stack
print(f"Size of the stack is {s.get_size()}")
# Clearing the stack
s.clear()
# Displaying the stack after clearing it
print(s.display())
