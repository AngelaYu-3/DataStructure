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
        self.finish = [self.size]
        self.time = 0

    def process(self, request):
        while len(self.finish) > 0 and self.finish[0] == self.time:
            self.finish.pop(0)

        if len(self.finish) == 1:
            self.finish[0] = request.arrived_at + request.time_to_process
            self.time += 1
            return Response(False, request.arrived_at)


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

    print(len(buffer.finish))
    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
