class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        lst = ["1"]
        for i in range(1, n):
            num = ""
            prev = ""
            count = 0
            for c in lst[i-1] + "a":
                if prev == "":
                    prev = c
                    count += 1
                elif prev == c:
                    count += 1
                elif prev != c:
                    num += str(count) + prev
                    count = 1
                    prev = c
            lst.append(num)
        return lst[n-1]

if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(6))
    print(s.countAndSay(5))

