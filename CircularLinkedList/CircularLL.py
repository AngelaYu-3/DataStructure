
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class CircularLL:
    def __init__(self):
        self.tail = None

    def print(self):
        curr = self.tail.next
        if self.tail.next is not None:
            while(True):
                print(curr.data)
                curr = curr.next
                if curr == self.tail.next:
                    break


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

    def remove(self):
        

def main():
    cll = CircularLL()
    cll.insert(3)
    cll.insert(5)
    cll.print()
    x = cll.tail.data
    print(x)

if __name__ == '__main__':
    main()