# python3
from collections import namedtuple
from ParallelProcessing2 import minHeap

Response = namedtuple("Response", ["threadNum", "startTime"])

class ParallelProcess:
    responses = []

    def __init__(self):
        # read in line 1: (number of threads, number of jobs)
        self.numThreads, self.numJobs = map(int, input().split())

        # read in line 2: (process time for jobs)
        self.processTime = list(map(int, input().split()))
        self.thread = minHeap.MinHeap(self.numThreads)

    def process(self, processTime):
        if not self.thread.isFull():
            threadNum = self.thread.getLength()
            item = minHeap.HeapItem(threadNum, processTime)
            self.thread.insert(item)
            #self.thread.print()
            #print(" ")

            self.responses.append(Response(threadNum, 0))
        else:
            threadNum = self.thread.getThreadNum()
            finishTime = self.thread.getFinishTime()
            item = minHeap.HeapItem(threadNum, finishTime + processTime)

            self.responses.append(Response(threadNum, finishTime))
            self.thread.extract()
            #self.thread.print()
            self.thread.insert(item)
            #self.thread.print()
            #print(" ")

def main():
    obj = ParallelProcess()

    for i in range(obj.numJobs):
        obj.process(obj.processTime[i])

    for i in obj.responses:
        print(i.threadNum, i.startTime)


if __name__== "__main__":
    main()