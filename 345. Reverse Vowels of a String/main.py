class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels = vowels + [c.upper() for c in vowels]
        vowel_idx_lst = []
        for idx, c in enumerate(s):
            if c in vowels:
                vowel_idx_lst.append(idx)

        length = len(vowel_idx_lst)
        s_lst = [c for c in s]
        for i in range(length/2):
            idx1 = vowel_idx_lst[i]
            idx2 = vowel_idx_lst[length - i - 1]
            temp = s[idx1]
            s_lst[idx1] = s_lst[idx2]
            s_lst[idx2] = temp
        return ''.join(s_lst)


if __name__ == "__main__":
    s = Solution()
    assert(s.reverseVowels('leetcode')=='leotcede')
    assert(s.reverseVowels('aA')=='Aa')