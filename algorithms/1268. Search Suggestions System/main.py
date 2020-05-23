from typing import List


def make_trie(words: List[str]) -> 'Trie':
    root = Trie()
    for word in words:
        current = root
        trie = None
        for c in word:
            if c not in current.children:
                trie = Trie(current.value+c)
                current.children[c] = trie
                current.keys.append(c)
                current.keys.sort()
            else:
                trie = current.children.get(c)
            current = current.children.get(c)
        trie.is_leaf = True
    return root


class Trie:
    def __init__(self, value=''):
        self.children = {}
        self.keys = []
        self.value = value
        self.is_leaf = False

    def dfs(self):
        if self.is_leaf:
            yield self.value
        for k in self.keys:
            trie = self.children.get(k)
            yield from trie.dfs()

    def with_prefix(self, s: str, n: int) -> List[str]:
        if not s:
            i = 0
            res = []
            for value in self.dfs():
                if i < n:
                    res.append(value)
                else:
                    break
                i += 1
            return res
        else:
            trie = self.children.get(s[0])
            if not trie:
                return []
            else:
                return trie.with_prefix(s[1:], n)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = make_trie(products)
        word = ""
        res = []
        for c in searchWord:
            word += c
            res.append(trie.with_prefix(word, 3))
        return res


if __name__ == "__main__":
    t = make_trie(["mobile","mouse","moneypot","monitor","mousepad"])
    # print(t)
    # for value in t.dfs():
    #     print(value)
    s = Solution()
    print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
    print(s.suggestedProducts(["havana"], "havana"))
