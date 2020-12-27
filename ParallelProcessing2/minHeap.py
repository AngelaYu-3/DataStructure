# python3

#3911731663 2946336306 3104934106 2936370273 3114837717 3033959396 3470199591 3444003346 3205065638 3140480513
class HeapItem:
    def __init__(self, threadNum, finishTime):
        self.finishTime = finishTime
        self.threadNum = threadNum

    def __str__(self):
        return str(self.finishTime)

class MinHeap:
    def __init__(self, maxLength):
        self.maxLength = maxLength
        self.heap = []


    # inserting value into heap
    def insert(self, item):
        # sorting heap after inserting value at beginning of heap
        if len(self.heap) < self.maxLength:
            current = len(self.heap)
            self.heap.insert(len(self.heap), item)

            while(self.heap[current].finishTime < self.heap[int((current - 1) /2)].finishTime):
                self.heap[current], self.heap[int((current - 1)/2)] = self.heap[int((current - 1) /2)], self.heap[current]
                current = int((current - 1)/2)

        minValue = self.heap[0].finishTime
        for i in range(len(self.heap)):
            if (self.heap[i].finishTime < minValue):
                print("WRONG: Incorrect insert")
                self.print()
                exit(1)

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

        #print("Extract: {}".format(minValue))
        return minValue


    def heapify(self, root):
        size = len(self.heap)
        smallest = root
        r = 2 * root + 2
        l = 2 * root + 1

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

    def getFinishTime(self):
        return self.heap[0].finishTime

    def getLength(self):
        return len(self.heap)

    def isFull(self):
        if len(self.heap) == self.maxLength:
            return True
        else:
            return False

    def print(self):
        print(*self.heap)

#def main():
    #test = MinHeap(10)
    #time_array=[3911731663, 2946336306, 3104934106, 2936370273, 3114837717, 3033959396, 3470199591, 3444003346, 3205065638, 3140480513]
    #for i in range(len(time_array)):
         #item = HeapItem(0, time_array[i])
         #test.insert(item)
         #test.heap.append(item)
    #test.print()
    #test.heapify(0)
    #test.print()


#if __name__ == "__main__":
    #main()