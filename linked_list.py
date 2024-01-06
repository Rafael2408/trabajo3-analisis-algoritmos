class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self, node):
        if node is not None:
            print(node.data)
            self.print_list(node.next)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_element(self, data):
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def print_list_reverse(self, node):
        if node is not None:
            print(node.data)
            self.print_list_reverse(node.prev)
