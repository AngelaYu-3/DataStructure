"""
circular linked list--(queue)
      insert(): adds node to tail
      remove(): removes node from head
      reverse(): reverses direc of circular linked list
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

    def reverse(self):
        if self.tail is None:
            pass
        else:
            curr = self.tail.next
            ntail = self.tail.next
            point = self.tail
            while(True):
                next = curr.next      #remembers node after curr so can progress thru list after curr.next is changed
                npoint = curr         #used to progress point
                curr.next = point     #taking curr.next and reversing it to point to the Node behind curr
                #print(curr.data)
                point = npoint        #progressing point forwards by one
                curr = next           #progressing curr forwards by one
                #print(curr.data)
                if next == ntail:      #if curr.next before reversal is equal to the initial head, one loop has been made so break
                    self.tail = ntail  #set new tail as what was the old head
                    break

def main():
    cll = CircularLL()
    while(True):
        user = input("insert, remove, reverse, or quit: ")
        if user == 'insert':
            value = int(input('Value: '))
            cll.insert(value)
            cll.print()
            #print(cll.tail.data)
        elif user == 'remove':
            cll.remove()
            cll.print()
        elif user == 'reverse':
            cll.reverse()
            cll.print()
        elif user == 'quit':
            break
        else:
            continue


if __name__ == '__main__':
    main()