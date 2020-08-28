class CircularQueue():

    def __init__(self, size):
        self.size = size
        self.queue = [0 for __ in range(size)]
        self.head = -1
        self.tail = -1

    def enqueue(self, data):
        if(self.tail + 1) % self.size == self.head:
            print("queue is full")

        else:
            #adding in first element to empty queue
            if self.head == -1:
                self.head = 0

            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1:
            print("queue is empty")
        elif self.head == self.tail:
            removed = self.queue[self.head]
            self.head = self.tail = -1
            return removed
        else:
            removed = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return removed

    def empty(self):
        if self.head == -1:
            return True
        else:
            return False

    def full(self):
        if (self.tail + 1) % self.size == self.head:
            return True
        else:
            return False

    def __getitem__(self, item):
        return self.queue[item]

    def peek(self):
        return self.queue[self.head]

    def print(self):
        if self.tail > self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i])
        elif self.tail == self.head:
            if self.tail == -1:
                pass
            else:
                print(self.queue[self.tail])
        else:
            for i in range(self.head, self.size):
                print(self.queue[i])
            for i in range(0, self.tail + 1):
                print(self.queue[i])

def main():
    size = int(input("Size of queue: "))
    test = CircularQueue(size)

    while True:
        user = input("enqueue, dequeue, get, or exit: ")

        if user == "enqueue":
            data = int(input("data value: "))
            test.enqueue(data)
            test.print()
        elif user == "dequeue":
            print("Removed: {}".format(test.dequeue()))
            test.print()
        elif user == "get":
            index = int(input("index: "))
            print(test.__getitem__(index))
        elif user == "exit":
            test.print()
            exit()
        else:
            continue


if __name__ == "__main__":
    main()