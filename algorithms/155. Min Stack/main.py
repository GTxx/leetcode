class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if x < self.min:
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            pop_val = self.stack[-1]
            self.stack = self.stack[:-1]
            if pop_val == self.min:
                if self.stack:
                    self.min = min(self.stack)
                else:
                    self.min = float('inf')

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
