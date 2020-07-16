"""
circular linked list
      -add method for a reversed circular linked list
"""
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class CircularLL:
    def __init__(self):
        self.tail = None

    def print(self):
        if self.tail is None:
            print('None')
        else:
            curr = self.tail.next
            while(True):
                print(curr.data)
                #statements here prevent circular print--stop when one circ is made
                curr = curr.next
                if curr == self.tail.next:
                    break

    #insert from tail
    def insert(self, data):
        if self.tail is None:
            n = Node(data)
            n.next = n
            self.tail = n
        else:
            n = Node(data)
            next = self.tail.next
            n.next = next
            self.tail.next = n
            self.tail = n

    #remove from head
    def remove(self):
        if self.tail is None:
            pass
        else:
            if self.tail.next == self.tail:
                self.tail = None
            else:
                head = self.tail.next
                self.tail.next = head.next
                head.next = None

def main():
    cll = CircularLL()
    while(True):
        user = input("insert, remove, or quit: ")
        if user == 'insert':
            value = int(input('Value: '))
            cll.insert(value)
            cll.print()
        elif user == 'remove':
            cll.remove()
            cll.print()
        elif user == 'quit':
            break
        else:
            continue


if __name__ == '__main__':
    main()