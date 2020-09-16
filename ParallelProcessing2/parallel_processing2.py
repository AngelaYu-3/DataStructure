# python3

#BUG WITH [2, 5] [1, 2, 3, 4, 5]
from collections import namedtuple
from ParallelProcessing2 import minHeap

Response = namedtuple("Response", ["thread", "start_at"])

class ThreadData:
    def __init__(self, process_time, index):
        self.process_time = process_time
        self.index = index

class Parallel:

    responses = []
    def __init__(self):
        self.n_threads, self.n_jobs = map(int, input().split())
        data = input()
        self.p_time = list(map(int, data.split()))
        self.threads = minHeap.MinHeap(self.n_threads)

    def process(self, index, p_time):
        #USE PRIORITY QUEUE (MAX HEAP) TO SORT!!!!! O(nlogn) instead of O(n)

        if index < self.n_threads:
            data = ThreadData(p_time, index)
            item = minHeap.HeapItem(p_time, data)
            self.threads.insert(item) #SORT BY FINISH TIME!!!
            self.responses.append(Response(index, 0))

        else:
            past_ft = self.threads.item.key
            past_id = self.threads.item.item.index
            self.threads.extract_min()
            data = ThreadData(p_time, past_id)
            item = minHeap.HeapItem(past_ft + p_time, data)
            self.threads.insert(item)
            self.responses.append(Response(past_id, past_ft))


def main():
    test = Parallel()
    #responses = test.process_helper()
    for i in range(test.n_jobs):
        test.process(i, test.p_time[i])

    for i in test.responses:
        print(i.thread, i.start_at)

if __name__ == "__main__":
    main()
