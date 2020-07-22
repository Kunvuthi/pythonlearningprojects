## In Python, stack can be implemented by using list and deque, but list isn't as efficient to use for stack since it is more of a dynamic array. ##
## Therefore, we'll be using deque for implementation ##
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)




stk = Stack()
stk.push(99)
stk.push('John')
print("Before pop(): ", stk.peek())
print(stk.size())
print("After pop(): ", stk)