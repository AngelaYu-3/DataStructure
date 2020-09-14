# python3

from collections import namedtuple
from ParallelProcessing2 import MaxHeap

Response = namedtuple("Response", ["thread", "start_at"])
Data = namedtuple("Data", ["finish_time", "process_time"])

class Parallel:

    responses = []
    def __init__(self):
        self.n_threads, self.n_jobs = map(int, input().split())
        data = input()
        self.p_time = list(map(int, data.split()))
        self.threads = MaxHeap.MaxHeap(self.n_threads)

    def process(self, index, p_time):
        #USE PRIORITY QUEUE (MAX HEAP) TO SORT!!!!! O(nlogn) instead of O(n)

        if index < self.n_threads:
            self.threads.insert(p_time)
            self.responses.append(Response(index, 0))

        else:
            min_fin = 0
            for i in range(self.n_threads):
                if self.threads[min_fin].finish_time <= self.threads[i].finish_time:
                    pass
                else:
                    min_fin = i

            past_ft = self.threads[min_fin].finish_time

            self.threads.remove(Data(past_ft, self.threads[min_fin].process_time))
            self.threads.insert(min_fin, Data(past_ft + p_time, p_time))
            self.responses.append(Response(min_fin, past_ft))


def main():
    test = Parallel()
    #responses = test.process_helper()
    for i in range(test.n_jobs):
        test.process(i, test.p_time[i])

    for i in test.responses:
        print(i.thread, i.start_at)

if __name__ == "__main__":
    main()
