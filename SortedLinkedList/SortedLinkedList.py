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


def main():
    ll = LinkedList();
    var = 1
    while var == 1:
        ch = input("Enter in a value or press 'q' to quit: ")
        ll.insert(ch)
        ll.print()

if __name__ == '__main__':
    main()



