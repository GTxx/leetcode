from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda word: len(word))
        res = []
        for idx, word in enumerate(words):
            for word1 in words[idx+1:]:
                if word in word1:
                    print(word, word1)
                    res.append(word)
                    break
        return res

if __name__ == "__main__":
    s = Solution()
    s.stringMatching(["mass","as","hero","superhero"])