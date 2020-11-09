# python3

class HeapItem:
    def __init__(self, finishTime, threadNum, startTime):
        self.finishTime = finishTime
        self.threadNum = threadNum
        self.startTime = startTime

class MinHeap:
    def __init__(self, maxLength):
        self.maxLength = maxLength
        self.heap = []


    # inserting value into heap
    def insert(self, item):
        # sorting heap after inserting value at beginning of heap
        if len(self.heap) <= self.maxLength:
            self.heap.insert(0, item)
            self.heapify(0)
        else:
            print("WRONG: no space in threads")


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
        r = 2 * root + 1
        l = 2 * root + 2

        # finding smallest finishTime value
        if r < size and self.heap[r].finishTime < self.heap[smallest].finishTime:
            smallest = r
        if l < size and self.heap[l].finishTime < self.heap[smallest].finishTime:
            smallest = l

        # if all finishTimes are the same, smallest threadNum goes first
        if r < size and self.heap[r].finishTime == self.heap[smallest].finishTime:
            if self.heap[r].threadNum < self.heap[smallest].threadNum:
                smallest = r
        if l < size and self.heap[l].finishTime == self.heap[smallest].finishTime:
            if self.heap[l].threadNum < self.heap[smallest].threadNum:
                smallest = l

        # if smallest is root, heap is already sorted! can just return heap
        # if smallest is NOT root, switch root w/ smallest and heapify again w/ new root as smallest index
        if smallest != root:
            self.heap[root], self.heap[smallest] = self.heap[smallest], self.heap[root]
            self.heapify(smallest)

        return self.heap

    def getThreadNum(self):
        return self.heap[0].threadNum

    def getStartTime(self):
        return self.heap[0].startTime

    def getFinishTime(self):
        return self.heap[0].finishTime

    def getLength(self):
        return len(self.heap)

    def isFull(self):
        if len(self.heap) >= self.maxLength:
            return True
        else:
            return False


