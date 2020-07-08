"""
Sorted Linked List in ascending order implementation
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
            return

def main():
    #print("hi")
    ll = LinkedList();
    num = int(input("Enter a number: "))
    ll.insert(num)
    c = ll.head
    print(c.data)

if __name__ == '__main__':
    main()






