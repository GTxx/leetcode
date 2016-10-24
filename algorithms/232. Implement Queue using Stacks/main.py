class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s1.append(x)
        self.s2 = self.s1[::-1]

    def pop(self):
        """
        :rtype: nothing
        """
        self.s2.pop()
        self.s1 = self.s2[::-1]

    def peek(self):
        """
        :rtype: int
        """
        return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return self.s1 == []
