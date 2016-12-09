class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def prefix_is_words(s, word_count, length):
            word_count1 = {}
            while s:
                word = s[:length]
                if word in word_count:
                    if word in word_count1:
                        word_count1[word] += 1
                    else:
                        word_count1[word] = 1
                    if word_count1[word] > word_count[word]:
                        return False
                    s = s[length:]
                else:
                    return False
            return True

        length = len(words[0])
        word_num = len(words)

        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        res = []
        idx = 0
        while idx <= len(s) - length * word_num:
            if prefix_is_words(s[idx: idx + length * word_num], word_count, length):
                res.append(idx)
            idx += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print s.findSubstring("barfoothefoobarman", ["foo", "bar"])
    print s.findSubstring("barfoofoobarthefoobarman",["bar","foo","the"])
    print s.findSubstring("aaaaaaaa", ["aa","aa","aa"])