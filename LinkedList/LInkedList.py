"""
basic linked list implemetation:
    add Tail & Head
    remove Tail & Head
    remove at a certain index
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

    def sz(self):
        return print(self.size)

    def peek(self):
        if self.head is None:
            return None
        else:
            return print(self.head.data)

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
        if self.size == 1:
            newHead = Node(None, None)
            self.head = newHead
            self.size -= 1

        elif self.size == 0:
            return None

        else:
            current = self.head

            while current.next.next is not None:
                current = current.next

            data = current.next.data
            current.next = None
            self.size -= 1
            return data

    #removing from front of list
    def removeHead(self):
        if self.size == 1:
            newHead = Node(None, None)
            self.head = newHead
            self.size -= 1

        elif self.size == 0:
            return None

        else:
            newHead = Node(self.head.next.data, self.head.next.next)
            data = self.head.data
            self.head.next = None
            self.head = newHead
            self.size -= 1
            return data

    #removing and returning node at location i--i is relative to head Node (pos 1)
    def remove(self, i):
        if i > self.size:
            return None
        elif i == 1:
            print(self.removeHead())
        elif i == self.size:
            print(self.removeTail())
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

    #connect linked list with users
    def user(self, option):
       if option == 'size':
           return self.sz()

       elif option == 'peek':
           return self.peek()

       elif option == 'addHead':
           data = int(input("Value of data: "))
           return self.addHead(data)

       elif option == 'addTail':
           data = int(input("Value of data: "))
           return self.addTail(data)

       elif option == 'removeTail':
           return self.removeTail()

       elif option == 'removeHead':
           return self.removeHead()

       elif option == 'print':
           return self.print()

       else:
           index = int(input("Value of index: "))
           return self.remove(index)


def main():
    ll = LinkedList()
    var = 1
    while var == 1:
        option = input("Choose size, peek, addHead, addTail, removeTail, removeHead, remove, print, stop: ")
        if option == 'stop':
            ll.print()
            break
        ll.user(option)

if __name__ == "__main__":
    main()
