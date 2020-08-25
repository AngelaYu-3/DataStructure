from collections import namedtuple
from NetworkPacket import circularQueue

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

class Node:
    def __init__(self, time_to_process, finish_time):
        self.time_to_process = time_to_process
        self.finish_time = finish_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.buffer = circularQueue.CircularQueue(self.size)
        self.head = self.tail = Node(None, None)

    global time
    time = 0
    def process(self, request):
        # write your code here
        while True:
            if time == self.buffer[self.head.finish_time]:

            if time == request.arrived_at:
                if self.buffer.empty() is True:
                    self.buffer.queue(Node(request.time_to_process, request.time_to_process + time))
                    time += 1
                else:


        time += 1


        return Response(False, -1)


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
