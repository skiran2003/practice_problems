class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Traversal function to display the linked list
def traverse(head):
    current = head
    elements = []
    while current:
        elements.append(current.value)
        current = current.next
    return elements

node1= Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Linking nodes to form a linked list
node1.next = node2
node2.next = node3
node3.next = node4

# Displaying the linked list
print(f'Elements of the linked list are {traverse(node1)}')