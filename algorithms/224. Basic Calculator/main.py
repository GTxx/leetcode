class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_len = len(s)
        def _calc(idx, total_len, s):
            num = ""
            op_stack, num_stack = [], []
            while idx < total_len:
                c = s[idx]
                idx += 1
                if c.isdigit():
                    num += c
                elif c == " ":
                    continue
                elif c == "(":
                    s, num2, idx = _calc(idx, total_len, s)
                    num_stack.append(num2)
                    if op_stack != []:
                        op = op_stack.pop()
                        num2 = num_stack.pop()
                        num1 = num_stack.pop()
                        res = num1 + num2 if op == "+" else num1 - num2
                        num_stack.append(res)
                else:
                    if num != "":
                        num_stack.append(int(num))
                    num = ""

                    if len(num_stack) >= 2:
                        num2 = num_stack.pop()
                        num1 = num_stack.pop()
                        op = op_stack.pop()
                        if op == "+":
                            res = num1 + num2
                        elif op == "-":
                            res = num1 - num2
                        num_stack.append(res)

                    if c == "+" or c == "-":
                        op_stack.append(c)
                    elif c == ")":
                        res = num_stack.pop()
                        return s, res, idx

            if num != "":
                num_stack.append(int(num))
            if op_stack != []:
                op = op_stack.pop()
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                return num1 + num2 if op == "+" else num1 - num2
            else:
                return num_stack[0]

        return _calc(0, total_len, s)
if __name__ == "__main__":
    s = Solution()
    print s.calculate("1 + 1")
    print s.calculate(" 2-1 + 2 ")
    print s.calculate("(1+1)")
    print s.calculate("2+(1+1)")
    print s.calculate("2-(1+1)")
    print s.calculate("(2-(1+1))")
    print s.calculate("((2-(1+1)))")
    print s.calculate("(1+(4+5+2)-3)")
    print s.calculate("(1+(4+5+2)-3)+(6+8)")
    print s.calculate("1-11")
    f = open('data.txt')
    st = f.read()
    import time
    begin = time.time()
    print s.calculate(st)
    print("time: {}s".format(time.time()-begin))
