1. DELETE NODE FROM SINGLY LINKED LIST:

class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None
​
def delete_node(node_to_delete):
    next_node = node_to_delete.next
    node_to_delete.value = next_node.value
    node_to_delete.next = next_node.next
​
def print_ll(node):
    current = node 
    while current is not None:
        print(current.value)
        current = current.next
​
x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')
​
x.next = y
y.next = z
​
print_ll(x)
print('=====')
delete_node(y)
print_ll(x)
print('=====')
print_ll(y)
print('=====')
print_ll(z)

2. REVERSE LINKED LIST: 

class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None
​
def reverse(head_of_list):
    current = head_of_list
    prev = None 
    while current is not None:
        next = current.next
        current.next = prev

        prev = current 
        current = next 

    return prev 
​
x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')
​
x.next = y
y.next = z
​

def print_ll(node):
    current = node 
    while current is not None:
        print(current.value)
        current = current.next
​
print_ll(x)
print('====')
new_head = reverse(x)
print_ll(new_head)