"""
Sorted Linked List in ascending order implementation (no duplicates)
with Node class and insert, remove header, and remove tail
methods
"""

class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        head = self.head

        if head is None:
            n = Node()
            n.data = data
            n.next = None
            self.head = n
            self.tail = n
            return #don't really need return bc returning null

        elif (head is not None) and (head.next is None):
            if head.data > data:
                n = Node()
                n.data = data
                n.next = self.head
                self.head = n
                n.next.next = None
                self.tail = n.next
                return

            else:
                n = Node()
                n.data = data
                n.next = None
                self.tail = n
                return


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






