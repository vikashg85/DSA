from linkedlist import linked_list

class Stack:
    def __init__ (self):
        self.stack = None

    def push(self, element):
        self.stack.element = linked_list.insert_first(element)

    def pop(self):
        self.stack