class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            if letter in node.child:
                node = node.child[letter]
            else:
                child_node = TrieNode()
                node.child[letter] = child_node
                node = child_node
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            if letter in node.child:
                node = node.child[letter]
            else:
                return False

        if node.is_word == True:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            if letter in node.child:
                node = node.child[letter]
            else:
                return False
        return True


if __name__ == "__main__":
    # trie = Trie()
    # trie.insert("somestring")
    # trie.insert("someint")
    # print(trie.search("key"))
    # print(trie.search("somestring"))
    # print(trie.search("somein"))
    # print(trie.startsWith("some"))

    trie = Trie()
    trie.insert("abc")
    print(trie.search("abc"))
    print(trie.search("ab"))
    trie.insert("ab")
    print trie.search("ab")
    trie.insert("ab")
    print trie.search("ab")
    print trie.startsWith('a')
    print trie.startsWith('ab')

