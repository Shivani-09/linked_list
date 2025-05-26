class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(5001)
node2 = Node(7001)
node3 = Node(9001)

node1.next = node2
node2.next = node3
node3.next = None

head = node1

while head is not None:
    print(head.data, end=' -> ')
    head = head.next
print("None")