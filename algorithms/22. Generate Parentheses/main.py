class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def _generate(current, left_n, right_n):
            if right_n == 0:
                return current
            elif left_n == 0:
                res = []
                for s in current:
                    res.append(s + ')'*right_n)
                return res
            else:
                if left_n == right_n:
                    current = [s+'(' for s in current]
                    return _generate(current, left_n-1, right_n)
                else:
                    add_left_current = [s+'(' for s in current]
                    add_left_res = _generate(add_left_current, left_n-1, right_n)

                    add_right_current = [s + ')' for s in current]
                    add_right_res = _generate(add_right_current, left_n, right_n-1)
                    return add_left_res + add_right_res

        return _generate(['('], n-1, n)


if __name__ == "__main__":
    s = Solution()
    print s.generateParenthesis(3)

