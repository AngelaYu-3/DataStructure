"""
Sorted Linked List in ascending order implementation (no duplicates)
with Node class and insert, remove header, and remove tail
methods
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

    def duplicate(self, data):
        curr = self.head

        while curr is not None:
            if curr.data == data:
                return True
            else:
                curr = curr.next

        if curr is None:
            return False

    def insert(self, data):
        if self.head is None:
            #print("1:")
            n = Node(data)
            self.head = n

        elif (self.head is not None) and (self.head.next is None):
            if self.head.data > data:
                #print("2: %d" % self.head.data)
                n = Node(data)
                n.next = self.head
                self.head = n
                return

            else:
                #print("3:")
                n = Node(data)
                self.head.next = n
                return

        else:

            if self.head.data > data:
                #print("4: %d" % self.head.data)
                n = Node(data)
                n.next = self.head
                self.head = n

            else:
                curr = self.head

                while curr.next is not None:
                    if (curr.data < data) & (curr.next.data > data):
                        #print("5: %d" %curr.data)
                        n = Node(data)
                        n.next = curr.next
                        curr.next = n
                        break
                    else:
                        #print("6: %d" %curr.data)
                        curr = curr.next

                if curr.next is None:
                    n = Node(data)
                    curr.next = n

def main():
    ll = LinkedList()
    var = 1
    val = None

    while var == 1:
        val = input("Enter in a value or press 'q' to quit: ")

        if (val == 'q') or (val == 'Q'):
            #print("wrong place")
            ll.print()
            break
        else:
            val = int(val)
            isdup = ll.duplicate(val)
            if isdup == True:
                continue
            else:
                ll.insert(val)
                ll.print()

if __name__ == '__main__':
    main()



