class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_pair(a, b):
            if a == '(' and b == ')':
                return True
            if a == "[" and b == ']':
                return True
            if a == "{" and b == "}":
                return True
            return False

        stack = []
        for letter in s:
            stack.append(letter)
            if len(stack) >= 2:
                if is_pair(stack[-2], stack[-1]):
                    stack.pop()
                    stack.pop()
        return True if not stack else False

if __name__ == "__main__":
    s = Solution()
    print s.isValid("()")
    print s.isValid("()[]{}")
    print s.isValid("(]")
