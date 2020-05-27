class Trie:
    def __init__(self, c):
        self.c = c
        self.children = {}
        self.is_word = False

    def add(self, string):
        if string:
            first = string[0]
            if first in self.children:
                child = self.children.get(first)
            else:
                child = Trie(first)
                self.children[first] = child
            child.add(string[1:])
        else:
            self.is_word = True

    def search(self, word: str) -> bool:
        if not word and self.is_word:
            return True
        elif not word and not self.is_word:
            return False
        else:
            first = word[0]
            if first != '.':
                if first in self.children:
                    return self.children.get(first).search(word[1:])
                else:
                    return False
            else:
                for key, trie in self.children.items():
                    if trie.search(word[1:]):
                        return True
                return False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie('')

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.root.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.root.search(word)


if __name__ == "__main__":
    from algorithms import test
    w = WordDictionary()
    w.addWord("bad")
    w.addWord("dad")
    w.addWord("mad")
    test("pad", False, w.search)
    test("bad", True, w.search)
    test(".ad", True, w.search)
    test("b..", True, w.search)
    test("b...", False, w.search)
    test("b", False, w.search)

    w = WordDictionary()
    w.addWord("a")
    w.addWord("ab")
    test("a", True, w.search)
    test("a.", True, w.search)
    test("ab", True, w.search)
    test(".a", False, w.search)
    test(".b", True, w.search)
    test("ab.", False, w.search)
    test(".", True, w.search)
    test("..", True, w.search)

    ["WordDictionary", "addWord", "addWord", "search", "search", "search", "search", "search", "search", "search",
     "search"]
    [[], ["a"], ["ab"], ["a"], ["a."], ["ab"], [".a"], [".b"], ["ab."], ["."], [".."]]
