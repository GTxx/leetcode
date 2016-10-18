class Queue(object):
    def __init__(self):
        self._queue = []

    def size(self):
        return len(self._queue)

    def push(self, x):
        self._queue.append(x)

    def pop(self):
        first = self._queue[0]
        self._queue = self._queue[1:]
        return first

    def is_empty(self):
        return self._queue == []

    def peek(self):
        return self._queue[0]


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = Queue()
        self.q2 = Queue()
        self.temp = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.push(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while self.q1.size() > 1:
            x = self.q1.pop()
            self.q2.push(x)
        top = self.q1.pop()

        while self.q2.size() > 0:
            x = self.q2.pop()
            self.q1.push(x)
        return top

    def top(self):
        """
        :rtype: int
        """
        while self.q1.size() > 0:
            x = self.q1.pop()
            self.q2.push(x)
        top = x

        while self.q2.size() > 0:
            x = self.q2.pop()
            self.q1.push(x)
        return top

    def empty(self):
        """
        :rtype: bool
        """
        return self.q1.is_empty()


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert(stack.pop() == 2)
    assert(stack.pop() == 1)

