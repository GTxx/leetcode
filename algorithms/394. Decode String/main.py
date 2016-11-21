class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def stack_push(lst, val):
            lst.append(val)
            return lst

        def stack_pop(lst):
            if not lst:
                return None, None
            return lst[:-1], lst[-1]

        num = ""
        aph = ""
        num_stack = []
        aph_stack = []
        for c in s:
            if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num += c
                if aph != "":
                    aph_stack = stack_push(aph_stack, aph)
                    aph = ""
            elif c == '[':
                num_stack = stack_push(num_stack, int(num))
                aph_stack = stack_push(aph_stack, c)
                num = ""
            elif c == ']':
                aph_list = []
                while True:
                    aph_stack, val = stack_pop(aph_stack)
                    if val == "[":
                        break
                    else:
                        aph_list.append(val)
                aph_list.reverse()
                if aph_list:
                    aph = "".join(aph_list) + aph
                num_stack, num = stack_pop(num_stack)
                aph_stack = stack_push(aph_stack, aph*num)
                num = ""
                aph = ""
            else:
                aph += c
                num = ""

        res = ""
        aph_stack.reverse()
        while aph_stack:
            aph_stack, val = stack_pop(aph_stack)
            res += val
        if aph:
            res += aph
        return res

if __name__ == "__main__":
    s = Solution()
    print s.decodeString("3[a]2[bc]")
    print s.decodeString("3[a2[c]]")
    print s.decodeString("2[abc]3[cd]ef")
    print s.decodeString("10[lee]")
    print s.decodeString("sd2[f2[e]g]i")
    print s.decodeString("2[2[b]]")




