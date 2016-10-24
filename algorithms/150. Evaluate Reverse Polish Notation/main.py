class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def calc(a, b, calc_type):
            if calc_type == "+":
                return a+b
            elif calc_type == "-":
                return a - b
            elif calc_type == "*":
                return a * b
            elif calc_type == "/":
                # Just for leetcode
                return int(float(a) / b)

        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                res = calc(a, b, token)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]

if __name__ == "__main__":
    s = Solution()
    assert(s.evalRPN(["2", "1", "+", "3", "*"]) == 9)
    assert(s.evalRPN(["4", "13", "5", "/", "+"]) == 6)
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))