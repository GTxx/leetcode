class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        res = 0
        dirs = input.split("\n")

        stack = []
        for dir in dirs:
            depth = 0
            while dir.startswith('\t'):
                depth += 1
                dir = dir[1:]
            for _ in range(len(stack) - depth):
                stack.pop()
            if "." in dir:
                length = sum([len(s) for s in stack]) + len(dir) + len(stack)
                if length > res:
                    res = length
            else:
                stack.append(dir)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
    print(s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
