# define the Node class

class Node:
    def __init__(self, element=None, next_node=None) -> None:
        self.element = element
        self.next_node = next_node

# defined linked list class to insert new element and print whole linked list
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_first(self, element):
        n = Node(element)
        n.next_node = self.head
        self.head = n

    def delete_first(self):
        n = self.head
        self.head = n.next_node
        n.next_node = None
        return n.element
        

    def print_list(self):
        n = self.head
        while n is not None:
            print(n.element, ' ', end='')
            n = n.next_node
        print()



# defined function which call the class object

def linked_list():
    ll = LinkedList()

    ll.insert_first(6)
    ll.insert_first(5)
    ll.insert_first(4)
    ll.insert_first(3)
    ll.print_list()


def print_list(n):
    while n is not None:
        print(n.element, ' ' , end='')
        n = n.next_node
    print()


# define another linked list function

def linked_list_3():
    l = Node(3, Node(4, Node(5)))
    print_list(l)
    # print(l.element, l.next_node.element, l.next_node.next_node.element)


# define another linked list

def linked_list_2():
    ll = Node()
    ll.element = 3
    ll.next_node = Node()
    ll.next_node.element = 4
    ll.next_node.next_node = Node()
    ll.next_node.next_node.element = 5
    ll.next_node.next_node.next_node = Node()
    ll.next_node.next_node.next_node.element = 6
    print(ll.element, ll.next_node.element, ll.next_node.next_node.element)

    


# define function 

def linked_list_1():
    n1 = Node()
    n1.element = 3
    n2 = Node()
    n2.element = 4
    n1.next_node=n2
    print(n1.element, n1.nextnode.element, ' ', end='')




# call linked_list function in same file.

if __name__ == "__main__":
    linked_list()

