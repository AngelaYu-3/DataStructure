# python3

class ParallelProcess:

    def __init__(self):
        # read in line 1: (number of threads, number of jobs)
        self.numThreads, self.numJobs = map(int, input().split())

        # read in line 2: (process time for jobs)
        self.processTime = list(map(int, input().split()))


def main():
    process = ParallelProcess()

if __name__== "__main__":
    main()