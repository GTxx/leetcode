class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))

    def multiply1(self, num1, num2):
        res = [0] * (len(num1) + len(num2))
        for idx1, str1 in enumerate(num1):
            for idx2, str2 in enumerate(num2):
                temp = int(str1) * int(str2)
                temp = '0' + str(temp) if int(temp) < 10 else str(temp)
                res[idx1 + idx2] += int(temp[0])
                res[idx1 + idx2 + 1] += int(temp[1])

        rev_res = list(reversed(res))
        for idx, val in enumerate(rev_res):
            if val >= 10:
                rev_res[idx+1] += val // 10
                rev_res[idx] = val % 10

        str_res = "".join([str(i) for i in reversed(rev_res)])
        # remove 0 in the front
        while True:
            if str_res[0] == "0" and len(str_res) > 1:
                str_res = str_res[1:]
            else:
                break
        return str_res


if __name__ == "__main__":
    s = Solution()
    assert(s.multiply1("123", "123") == str(123 * 123))
    assert(s.multiply1("0", "123") == "0")
