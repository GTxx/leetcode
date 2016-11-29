# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        bracket_stack = []
        idx = 0
        number = ""
        while idx < len(s):
            c = s[idx]
            if c == "[":
                bracket_stack.append(c)
            elif c.isdigit() or c == "-":
                number += c
            elif c == ",":
                if number != "":
                    number_int = int(number)
                    bracket_stack.append(number_int)
                    number = ""
            elif c == "]":
                if number != "":
                    bracket_stack.append(int(number))
                    number = ""
                elem = []
                while True:
                    val = bracket_stack.pop()
                    if val != "[":
                        elem.append(val)
                    else:
                        break
                elem.reverse()
                bracket_stack.append(elem)
            idx += 1

        if number != "":
            return NestedInteger(int(number))
        else:
            return NestedInteger(bracket_stack[0])

if __name__ == "__main__":
    s = Solution()
    print(s.deserialize("123"))
    print(s.deserialize("[123, 456]"))
    print(s.deserialize("[123, 456, -1]"))
    print(s.deserialize("[123, 456, -1, [1,2,3]]"))
    print(s.deserialize("[[-1, 0, 1], 123, 456, -1, [1,2,3]]"))
