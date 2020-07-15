"""
queue implementation
    queue and dequeue
"""

from LinkedList import LinkedList

class Queue:
    ll = LinkedList()
    def queue(self,data):
        self.ll.addHead(data)
        self.ll.print()

    def dequeue(self):
        self.ll.removeTail()
        if self.ll.size == 0:
            pass
        else:
            self.ll.print()

def main():
    q = Queue()
    x = 1
    while x == 1:
        user = input("Queue or Dequeue or 'q' to quit: ")
        if (user == 'Queue') or (user == 'queue'):
            val = int(input("Value: "))
            q.queue(val)
        elif (user == 'Dequeue') or (user == 'dequeue'):
            q.dequeue()
        elif user == 'q' or user == 'Q':
            break
        else:
            continue

if __name__ == "__main__":
    main()