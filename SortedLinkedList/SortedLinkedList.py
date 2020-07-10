"""
Sorted Linked List in ascending order implementation (no duplicates)
with Node class and insert, remove header, and remove tail
methods

    TODO
        -finish last insert condition
        -test
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def data(self):
        print('getter method called')
        return self

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        head = self.head

        if head is None:
            n = Node(data)
            self.head = n

        elif (head is not None) and (head.next is None):
            if head.data > data:
                n = Node(data)
                n.next = self.head
                self.head = n
                return

            else:
                n = Node(data)
                self.head.next = n
                return

        else:


def main():
    ll = LinkedList();
    num = int(input("Enter a number: "))
    ll.insert(num)
    num = int(input("Enter a number: "))
    ll.insert(num)
    c = ll.head
    b = ll.head.next
    print(c.data)
    print(b.data)

if __name__ == '__main__':
    main()






