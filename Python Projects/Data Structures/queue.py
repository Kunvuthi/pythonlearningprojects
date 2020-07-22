## Think of queueing to get lunch, first to go in will get lunch first, therefore, first to go out. ##
## This data structure works the same way ##
## One usage of queue would be the New York Stock Exchange, London Stock Exchange, etc.... where they are producer, and consumer are us to get their data. ##


from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

