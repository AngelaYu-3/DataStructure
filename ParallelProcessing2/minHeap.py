# python3

class MinHeap:
    def __init__(self, maxLength):
        self.maxLength = maxLength
        self.heap = []


    # inserting value into heap
    def insert(self, value):
        # sorting heap after inserting value at beginning of heap
        self.heap.insert(0, value)
        self.heapify(0)


    # removing min value from heap
    def extract(self):
        # remembering min value to be returned
        minValue = self.heap[0]
        lastIndex = len(self.heap) - 1

        # swapping min value at 0 with last value
        self.heap[0], self.heap[lastIndex] = self.heap[lastIndex], self.heap[0]

        # removing lastIndex with min value
        self.heap.pop(lastIndex)

        # sorting heap after removing min value
        self.heapify(0)
        return minValue


    def heapify(self, root):
        size = len(self.heap)
        smallest = root
        rIndex = 2 * root + 1
        lIndex = 2 * root + 2

        # finding smallest value
        if rIndex < size and self.heap[rIndex] < self.heap[smallest]:
            smallest = rIndex
        if lIndex < size and self.heap[lIndex] < self.heap[smallest]:
            smallest = lIndex

        # if smallest is root, heap is already sorted! can just return heap
        # if smallest is NOT root, switch root w/ smallest and heapify again w/ new root as smallest index
        if smallest != root:
            self.heap[root], self.heap[smallest] = self.heap[smallest], self.heap[root]
            self.heapify(smallest)

        return self.heap


def main():
    test = MinHeap(5)
    testValues = list(map(int, input().split()))

    for x in testValues:
        print(test.insert(x))

    test.extract()

if __name__== "__main__":
    main()


