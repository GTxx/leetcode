class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        STATE_ALPHA, STATE_SLASH = "alpha", "slash"
        state = STATE_ALPHA
        alpha = ""
        for c in path + "/":
            if state == STATE_ALPHA:
                if c == "/":
                    state = STATE_SLASH
                    if alpha == ".":
                        alpha = ""
                    elif alpha == "..":
                        alpha = ""
                        if len(stack) > 0:
                            stack.pop()
                    elif alpha != "":
                        stack.append(alpha)
                        alpha = ""
                else:
                    alpha += c
            elif state == STATE_SLASH:
                if c == "/":
                    continue
                else:
                    state = STATE_ALPHA
                    alpha += c
        return "/" + "/".join(stack)

if __name__ == "__main__":
    s = Solution()
    assert(s.simplifyPath("/home/") == "/home")
    assert(s.simplifyPath("/a/./b/../../c/") == "/c")
    assert(s.simplifyPath("/home//foo/") == "/home/foo")
    assert(s.simplifyPath("/../") == "/")
    assert(s.simplifyPath("/") == "/")
    assert(s.simplifyPath("/...") == "/...")
    assert(s.simplifyPath("/..hidden") == "/..hidden")
