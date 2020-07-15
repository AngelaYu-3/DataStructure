"""
basic stack implementation
    push & pop
"""

from LinkedList import LinkedList

class Stack:
    ll = LinkedList()
    def push(self,data):
        self.ll.addHead(data)
        self.ll.print()

    def pop(self):
        self.ll.removeHead()
        if self.ll.size == 0:
            pass
        else:
            self.ll.print()

def main():
    stack = Stack()
    x = 1
    while x == 1:
        user = input("Push or Pop or 'q' to quit: ")
        if (user == 'Push') or (user == 'push'):
            val = int(input("Value: "))
            stack.push(val)
        elif (user == 'Pop') or (user == 'pop'):
            stack.pop()
        elif user == 'q' or user == 'Q':
            break
        else:
            continue

if __name__ == "__main__":
    main()

