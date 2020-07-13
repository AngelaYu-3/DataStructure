"""
Sorted Linked List in ascending order implementation (no duplicates)
with Node class and insert, remove header, and remove tail
methods
    TODO
        -finish last insert condition
        -test
"""
import sys

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

    def print(self):
        curr = self.head

        while curr is not None:
            print(curr.data)
            curr = curr.next

    def insert(self, data):

        if self.head is None:
            print("1:")
            n = Node(data)
            self.head = n

        elif (self.head is not None) and (self.head.next is None):
            if self.head.data > data:
                print("2: %d" % self.head.data)
                n = Node(data)
                n.next = self.head
                self.head = n
                return

            else:
                print("3:")
                n = Node(data)
                self.head.next = n
                return

        else:

            if self.head.data > data:
                print("4: %d" % self.head.data)
                n = Node(data)
                n.next = self.head
                self.head = n

            else:
                curr = self.head

                while curr.next is not None:
                    if (curr.data < data) & (curr.next.data > data):
                        print("5: %d" %curr.data)
                        n = Node(data)
                        n.next = curr.next
                        curr.next = n
                        break
                    else:
                        print("6: %d" %curr.data)
            """
            curr = self.head

            while curr.next is not None:
                if (curr.data < data) & (curr.next.data > data):
                    n = Node(data)
                    curr.next = n
                    n.next = curr.next.next
                    break
                else:
                    curr = curr.next

            if curr.next is None:
                n = Node(data)
                curr.next = n
            """



def main():
    ll = LinkedList();
    var = 1
    while var == 1:
        value = int(input("Enter in a value: "))
        ll.insert(value)
        ll.print()

if __name__ == '__main__':
    main()



