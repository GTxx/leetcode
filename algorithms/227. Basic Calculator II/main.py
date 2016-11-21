class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def op_nums(n1, n2, op):
            if op == "+":
                return n1 + n2
            elif op == "-":
                return n1 - n2
            elif op == "*":
                return n1 * n2
            elif op == "/":
                return n1/ n2

        num = ""
        num_stack = []
        op_stack = []
        for c in s:
            if c.isdigit():
                num += c
            elif c == " ":
                continue
            elif c in ('+', '-', '*', '/'):
                if num != "":
                    num_stack.append(int(num))
                    num = ""
                if op_stack != [] and op_stack[-1] in ('*', '/'):
                    op = op_stack.pop()
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    num_stack.append(op_nums(num1, num2, op))
                op_stack.append(c)
        else:
            if num != "":
                num_stack.append(int(num))
            if op_stack != [] and op_stack[-1] in ('*', '/'):
                op = op_stack.pop()
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(op_nums(num1, num2, op))

        res = 0
        while op_stack != []:
            op = op_stack.pop()
            num = num_stack.pop()
            res += num if op == "+" else -num
        return res + num_stack[0]

if __name__ == "__main__":
    s = Solution()
    print s.calculate("3+2*2")
    print s.calculate(" 3/2 ")
    print s.calculate(" 3+5 / 2 " )
    print s.calculate("1-1+1")

