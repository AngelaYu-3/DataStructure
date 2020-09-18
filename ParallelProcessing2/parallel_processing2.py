# python3

from collections import namedtuple
from ParallelProcessing2 import minHeap

Response = namedtuple("Response", ["thread", "start_at"])

class Parallel:

    responses = []
    def __init__(self):
        self.n_threads, self.n_jobs = map(int, input().split())
        data = input()
        self.p_time = list(map(int, data.split()))
        self.threads = minHeap.MinHeap(self.n_threads)

    def process(self, index, p_time):

        if index < self.n_threads:
            item = minHeap.HeapItem(p_time, index)
            self.threads.insert(item)
            self.responses.append(Response(index, 0))

        else:
            self.threads.print()
            past_id = self.threads.get_min_index()
            past_ft = self.threads.get_min()
            self.threads.extract_min()
            item = minHeap.HeapItem(past_ft + p_time, past_id)
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