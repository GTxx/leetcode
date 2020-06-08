from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        res = 0
        for c in chars:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for word in words:
            word_d = {}
            is_ok = True
            for c in word:
                if c not in d:
                    is_ok = False
                    break
                else:
                    if c in word_d:
                        word_d[c] += 1
                        if word_d[c] > d[c]:
                            is_ok = False
                            break
                    else:
                        word_d[c] = 1
            res += len(word) if is_ok else 0
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
    assert s.countCharacters(["cat", "bt", "hat", "tree"], "atach") == 6
    assert s.countCharacters(["hello", "world", "leetcode"], chars="welldonehoneyr") == 10
