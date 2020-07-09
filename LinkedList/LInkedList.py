"""
basic linked list implemetation:
    add Tail & Head
    remove Tail & Head
    remove at a certain index

    TODO
       -only print when calling remove() not w/ removeHead() & removeTail() too
       -user interface
       -try to break logic!
"""

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def data(self):
        print('getter method called')
        return self.data


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def size(self):
        return self.size

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def print(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    #adding to end of list
    def addTail(self, data):
        if self.size is 0:  #list is initially empty
            self.head = Node(data, None)
            self.size += 1

        else:  #list not empty
            current = self.head

            while current.next is not None:  # finding end of list
                current = current.next

            # creating new node
            n = Node(data,None)
            current.next = n
            self.size += 1

    #adding to front of list
    def addHead(self, data):
        if self.size is 0:  #list is initially empty
            self.head = Node(data, None)
            self.size += 1

        else: #list not empty
            n = Node(data,self.head)
            self.head = n
            self.size += 1

    #removing from back of list
    def removeTail(self):
        current = self.head

        while current.next.next is not None:
            current = current.next

        data = current.next.data
        current.next = None
        self.size -= 1
        return data

    #removing from front of list
    def removeHead(self):
        newHead = Node(self.head.next.data, self.head.next.next)
        data = self.head.data
        self.head.next = None
        self.head = newHead
        self.size -= 1
        return print(data)

    #removing and returning node at location i--i is relative to head Node (pos 1)
    def remove(self, i):
        if i > self.size:
            return None
        elif i == 1:
            self.removeHead()
        elif i == self.size:
            self.removeTail()
        else:
            current = self.head
            currentInd = 1

            while currentInd != self.size - 1:
                current = current.next
                currentInd += 1

            newPtNode = Node(current.next.next.data, current.next.next)
            current = newPtNode
            data = current.next.data
            return data



def main():
    ll = LinkedList()
    ll.addTail(3)
    ll.addTail(785)
    ll.addHead(45)
    ll.addTail(32)
    ll.addTail(20)
    ll.addHead(18)
    ll.print()
    print('\n')
    ll.remove(1)
    ll.removeHead()
    """
    print('\n')
    ll.print()
    ll.removeTail()
    print('\n')
    ll.print()
    ll.removeHead()
    print('\n')
    ll.print()
    #print(ll.peek())
    """


if __name__ == "__main__":
    main()
