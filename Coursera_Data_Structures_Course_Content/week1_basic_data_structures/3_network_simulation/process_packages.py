# python3
import queue
from datetime import datetime as dt

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, buffer_size, responses):
        self.buffer_size = buffer_size
        self.buff_dict = {}
        self.start_time = dt.now()
        self.storage = 0 
        self.responses = responses    
        self.last_time = -1

    def curr_time(self):
        return dt.now() - self.start_time

    def process(self, request):
        
        for fin_time, req in self.buff_dict.items():
            if fin_time >= self.curr_time():
                self.buff_dict.pop(fin_time)
        
        was_dropped = True
        start_time = -1
        if request.arrived_at > self.curr_time() and \
            self.storage <= self.buffer_size and \
            request.arrived_at != self.last_time:

            fin_time = request.arrived_at + request.time_to_process
            if fin_time not in self.buff_dict.keys():
                self.buff_dict[fin_time] = request
                self.storage += 1
                was_dropped = False
                start_time = request.arrived_at
            
        self.last_time = request.arrived_at

        return Response(was_dropped, start_time)


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

    buffer = Buffer(buffer_size, responses)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
