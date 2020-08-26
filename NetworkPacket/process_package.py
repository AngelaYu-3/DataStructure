# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

class Node:
    def __init__(self, time_to_process, finish_time):
        self.time_to_process = time_to_process
        self.finish_time = finish_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish = []

    def process(self, request):
        #popping values--done processing by the time new value arrives
        while len(self.finish) > 0 and self.finish[0] <= request.arrived_at:
            self.finish.pop(0)

        #buffer not full
        if len(self.finish) < self.size:

            #buffer empty
            if len(self.finish) == 0:
                # finish_time: arrival_time + finish_time
                # start_time: arrival_time
                self.finish.append(request.arrived_at + request.time_to_process)
                return Response(False, request.arrived_at)
            #buffer has values
            else:
                # finish_time: process_time + finish_time of previous index
                # start_time: finish_time of previous index
                curr_index = len(self.finish) - 1
                finish_time = self.finish[curr_index] + request.time_to_process
                started_at = self.finish[curr_index]
                self.finish.append(finish_time)
                return Response(False, started_at)

        #buffer full
        else:
            return Response(True, -1)

#calling process() and adding returned values into responses[]
def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    #taking in first line
    buffer_size, n_requests = map(int, input().split())

    #taking in next lines as requests
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    #creating buffer and processing requests
    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    #printing outputs from responses[]
    for response in responses:
        print(response.started_at if not response.was_dropped else -1)

if __name__ == "__main__":
    main()
