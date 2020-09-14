# python3

class MaxHeap:
    def __init__(self, max_len):
        self.max_len = max_len
        self.heap = []

    def insert(self, value):
        length = len(self.heap)
        curr = length
        if curr % 2 == 0:
            p = int((curr - 2) / 2)
        else:
            p = int((curr - 1) / 2)

        if length < self.max_len:
            self.heap.insert(length, value)
            while self.heap[p] < self.heap[curr]:
                self.heap[p], self.heap[curr] = self.heap[curr], self.heap[p]
                if p == 0:
                    break
                if p % 2 == 0:
                    curr = p
                    p = int((p - 2) / 2)
                else:
                    curr = p
                    p = int((p - 1) / 2)

    def extract_max(self):
        root = 0
        largest = root
        l = (2 * root) + 1
        r = (2 * root) + 2

        max_val = self.heap[0]
        swap = len(self.heap) - 1

        self.heap[0], self.heap[swap] = self.heap[swap], self.heap[0]
        self.heap.pop(swap)

        if l < len(self.heap) and self.heap[l] > self.heap[largest]:
            largest = l
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r

        if largest == 0:
            pass
        else:
            while self.heap[largest] > self.heap[root]:
                self.heap[root], self.heap[largest] = self.heap[largest], self.heap[root]
                root = largest
                l = (2 * root) + 1
                r = (2 * root) + 2

                if l < len(self.heap) and self.heap[l] > self.heap[largest]:
                    largest = l
                if r < len(self.heap) and self.heap[r] > self.heap[largest]:
                    largest = r

        return(max_val)

    def get_max(self):
        return(self.heap[0])


def main():
    m = int(input("max: "))
    test = MaxHeap(m)

    while True:
        user = input("insert, max, get: ")

        if user == 'insert':
            value = int(input("value: "))
            test.insert(value)
            print(test.heap)
        elif user == "get":
            print(test.get_max())
            print(test.heap)
        elif user == 'max':
            print(test.extract_max())
            print(test.heap)
        else:
            exit()

if __name__ == "__main__":
    main()