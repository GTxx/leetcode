class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for c in S:
            if c != ')':
                stack.append(c)
            else:
                exp = []
                while stack[-1] != '(':
                    top = stack.pop()
                    exp.append(top)
                stack.pop()
                value = 2 * sum(exp) if exp else 1
                stack.append(value)
        return sum(stack)


if __name__ == "__main__":
    s = Solution()
    assert s.scoreOfParentheses("()") == 1
    assert s.scoreOfParentheses("(())") == 2
    assert s.scoreOfParentheses("()()") == 2
    assert s.scoreOfParentheses("(()(()))") == 6
