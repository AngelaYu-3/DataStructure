from collections import namedtuple
from queue import Queue

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])
BufferTime = namedtuple("BufferTime", ["final_time", "started_at"])

#priority queue???--to order final_times in order to pop them accordingly in order

class Buffer:
    global finalTime
    global time
    time = 0;
    size = 0
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    finalTime = Queue(maxsize=size)
    def process(self, request):
        # write your code here
        if finalTime.full() is False:
            final_time = request.arrived_at + request.time_to_process
            finalTime.append(BufferTime(final_time, request.arrived_at))
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

    #print(buffer.size)


if __name__ == "__main__":
    main()
