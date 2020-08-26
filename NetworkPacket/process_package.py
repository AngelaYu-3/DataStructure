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
        #self.time = 0

    def process(self, request):
        while len(self.finish) > 0 and self.finish[0] <= request.arrived_at:
            self.finish.pop(0)

        if len(self.finish) < self.size:
            if len(self.finish) == 0:
                self.finish.append(request.arrived_at + request.time_to_process)
                return Response(False, request.arrived_at)
            else:
                curr_index = len(self.finish) - 1
                finish_time = self.finish[curr_index] + request.time_to_process
                self.finish.append(finish_time)
                started_at = self.finish[curr_index]
                return Response(False, started_at)
        else:
            return Response(True, -1)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)

if __name__ == "__main__":
    main()
