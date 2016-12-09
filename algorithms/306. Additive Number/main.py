class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        length = len(num)
        if length < 3:
            return False
        if num.startswith("0"):
            i_range = (1, )
        else:
            i_range = range(1, length-1)
        for i in i_range:
            if i > length - i:
                break
            if num[i] == "0":
                j_range = (i+1, )
            else:
                j_range = range(i+1, length)
            for j in j_range:
                if j - i > length - j:
                    break
                first = int(num[:i])
                second = int(num[i: j])
                start = j
                while start < length:
                    if num[start] == "0" and first + second != 0:
                        break
                    first, second = second, first + second
                    if not num[start:].startswith(str(second)):
                        break
                    else:
                        start += len(str(second))

                if start == length:
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.isAdditiveNumber("199100199"))
    print(s.isAdditiveNumber("112358"))
    print(s.isAdditiveNumber("123"))
    print(s.isAdditiveNumber("101"))
    print(s.isAdditiveNumber("10112"))
    print(s.isAdditiveNumber("000"))
    print(s.isAdditiveNumber("211738"))

    print(s.isAdditiveNumber("0235813"))
    print(s.isAdditiveNumber("1023"))
