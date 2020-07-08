class Node:
    def __init__(self, data, next):
        self.data = data
        self.data = next

    def data(self):
        print('getter method called')
        return self.data


class LinkedList:
    size = 0
    head = Node(None, None)

    def size(self):
        return self.size

    def peek(self):
        return LinkedList.head

    # adding to end of list
    def add(self, data):

        if LinkedList.size is 0:  # list is initially empty
            self.head = Node(data, None)
            self.size += 1

        else:  # list not empty
            x = 1
            temp = self.head

            while temp.next is not None:  # finding end of list
                if temp.next == None:
                    break

                temp = temp.next

            # creating new node
            n = Node(data,None)
            temp.next = n
            n.next = None

    """ constructor is not needed
        def __init__(self):
            global size 
            global head
            size = 0
            head = Node(None)
    """


def main():
    ll = LinkedList()
    num1 = int(input("Enter integer: "))
    num2 = int(input("Enter integer: "))
    ll.add(num1)
    ll.add(num2)
    print(head.data)


if __name__ == "__main__":
    main()
