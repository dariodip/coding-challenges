"""
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""

class Node():

    def __init__(self, val):
        self.val = val
        self.both = 0


special_node = Node(None)


class XORDoubleLinkedList():

    def __init__(self):
        self.head = special_node
        self.tail = special_node

    def add(self, element):
        newNode = Node(element)
        if self.head == special_node:
            self.tail = self.head = newNode
        else:
            newNode.both = get_pointer(self.tail)
            self.tail.both = self.tail.both ^ id(newNode)
            self.tail = newNode

    def get(self, index):
        previous = 0
        current = self.head
        for i in range(ind - 1):
            tmp = get_pointer(current)
            current = dereference_pointer(previous ^ current.both)
            previous = tmp
            if current.both == previous and i < ind-2:
                raise Exception('Invalid Index')
        return current

    def __str__(self):
        s = ''
        previous = 0
        current = self.head
        current_id = 0
        while current.both != previous:
            s += '[current_id:{}, val:{}, both:{}]'.format(current_id, current.val, current.both)
            current_id += 1
            tmp = get_pointer(current)
            current = dereference_pointer(previous ^ current.both)
            previous = tmp
        return s
