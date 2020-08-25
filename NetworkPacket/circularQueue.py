class CircularQueue():

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = 0

    def enqueue(self, data):

        if (self.tail + 1) % self.size == self.head:
            print("queue is full")
        else:
            if self.head == -1:
                self.head = 0

        if (self.tail == self.head) and (self.queue[self.tail] is not None) and (self.queue[self.head] is not None):
            print("queue is full")
        else:
            self.queue[self.tail] = data
            if self.tail != self.size - 1:
               self.tail += 1
            else:
                self.tail = 0

    def dequeue(self):
        if (self.tail == self.head) and (self.queue[self.tail] is None) and (self.queue[self.head] is None):
            print("queue is empty")
        else:
            self.queue.pop(self.head)
            if self.head != self.size - 1:
                self.head += 1
            else:
                self.head = 0

    def print(self, is_queue):
        if is_queue is True:
            for i in range(self.size):
                if self.queue[i] is None:
                    pass
                else:
                    print(self.queue[i])
        else:
            for i in range(self.head, self.size):
                print(self.queue[i])



def main():
    size = int(input("Size of queue: "))
    test = CircularQueue(size)

    while True:
        user = input("enqueue, dequeue, or exit: ")

        if user == "enqueue":
            data = int(input("data value: "))
            test.enqueue(data)
            print("Tail: {} Head: {}".format(test.tail, test.head))
            test.print(True)
        elif user == "dequeue":
            test.dequeue()
            print("Tail: {} Head: {}".format(test.tail, test.head))
            test.print(False)
        else:
            #test.print()
            exit()

if __name__ == "__main__":
    main()