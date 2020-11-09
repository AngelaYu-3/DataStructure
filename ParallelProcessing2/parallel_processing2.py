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
            #print("L1")
            threadNum = self.thread.getLength()
            item = minHeap.HeapItem(processTime, threadNum, 0)
            self.thread.insert(item)
            self.responses.append(Response(threadNum, 0))
        else:
            #print("L2")
            startTime = self.thread.getStartTime()
            #print(startTime)
            threadNum = self.thread.getThreadNum()

            finishTime = self.thread.getFinishTime()
            #print(finishTime)
            item = minHeap.HeapItem(processTime + finishTime, threadNum, finishTime)
            self.thread.extract()
            self.thread.insert(item)
            self.responses.append(Response(threadNum, finishTime))



def main():
    process = ParallelProcess()

    # responses = test.process_helper()
    for i in range(process.numJobs):
        process.process(process.processTime[i])

    for i in process.responses:
        print(i.threadNum, i.startTime)

if __name__== "__main__":
    main()