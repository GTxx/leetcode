from timeit import timeit
from collections import defaultdict

# class TrieNode(object):
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.child = defaultdict(TrieNode)
#         self.is_word = False


class Trie(object):
    def __init__(self):
        # self.root = TrieNode()
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            # node = node.child[letter]
            # if letter in node.child:
            #     node = node.child[letter]
            # else:
            #     child_node = TrieNode()
            #     node.child[letter] = child_node
            #     node = child_node
            if letter in node:
                node = node[letter]
            else:
                node[letter] = {}
                node = node[letter]
        node['#'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            if letter in node:
                node = node[letter]
            else:
                return False

        return True if node.get('#') else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            if letter in node:
                node = node[letter]
            else:
                return False
        return True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.res = set()
        self.adj = self.ajacent_positions(board)
        words = list(set(words))
        trie = Trie()
        for word in words:
            trie.insert(word)

        row_len = len(board)
        col_len = len(board[0])
        used_positions = [x[:] for x in [[False] * col_len] * row_len]
        for row in xrange(len(board)):
            for col in xrange(len(board[0])):
                used_positions[row][col] = True
                self.dfs(row, col, board, used_positions, board[row][col], trie)
                used_positions[row][col] = False
        return list(self.res)

    def dfs(self, row, col, board, used_positions, prefix_word, trie):

        if not trie.startsWith(prefix_word):
            return

        if trie.search(prefix_word):
            self.res.add(prefix_word)

        positions = self.get_ajacent_positions(row, col, used_positions)

        for position in positions:
            r, c = position
            used_positions[r][c] = True
            self.dfs(r, c, board, used_positions, prefix_word+board[r][c], trie)
            used_positions[r][c] = False

    def get_ajacent_positions(self, row, col, used_positions):
        neighbor_positions = self.adj[(row, col)]
        return [(row, col) for row, col in neighbor_positions if used_positions[row][col] == False]

    def ajacent_positions(self, board):
        res = {}
        row_len = len(board)
        col_len = len(board[0])
        for row in range(row_len):
            for col in range(col_len):
                neighbor_positions = [
                    (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
                ]
                res[(row, col)] = tuple(
                    (row, col) for row, col in neighbor_positions if
                    ( 0 <= row < row_len and 0 <= col < col_len))
        return res

if __name__ == "__main__":
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    s = Solution()
    print(s.findWords(board, ["oath","pea","eat","rain"]))

    board = ["a"]
    print(s.findWords(board, ["a","a"]))

    board = ["aaaa", "aaaa", "aaaa", "aaaa", "bcde", "fghi", "jklm", "nopq",
             "rstu",
             "vwxy", "zzzz"]
    words = ["aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaab", "aaaaaaaaaaaaaaac",
             "aaaaaaaaaaaaaaad", "aaaaaaaaaaaaaaae", "aaaaaaaaaaaaaaaf",
             "aaaaaaaaaaaaaaag", "aaaaaaaaaaaaaaah", "aaaaaaaaaaaaaaai",
             "aaaaaaaaaaaaaaaj", "aaaaaaaaaaaaaaak", "aaaaaaaaaaaaaaal",
             "aaaaaaaaaaaaaaam", "aaaaaaaaaaaaaaan", "aaaaaaaaaaaaaaao",
             "aaaaaaaaaaaaaaap", "aaaaaaaaaaaaaaaq", "aaaaaaaaaaaaaaar",
             "aaaaaaaaaaaaaaas", "aaaaaaaaaaaaaaat", "aaaaaaaaaaaaaaau",
             "aaaaaaaaaaaaaaav", "aaaaaaaaaaaaaaaw", "aaaaaaaaaaaaaaax",
             "aaaaaaaaaaaaaaay", "aaaaaaaaaaaaaaaz", "aaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaab", "aaaaaaaaaaaaaaac", "aaaaaaaaaaaaaaad",
             "aaaaaaaaaaaaaaae", "aaaaaaaaaaaaaaaf", "aaaaaaaaaaaaaaag",
             "aaaaaaaaaaaaaaah", "aaaaaaaaaaaaaaai", "aaaaaaaaaaaaaaaj",
             "aaaaaaaaaaaaaaak", "aaaaaaaaaaaaaaal", "aaaaaaaaaaaaaaam",
             "aaaaaaaaaaaaaaan", "aaaaaaaaaaaaaaao", "aaaaaaaaaaaaaaap",
             "aaaaaaaaaaaaaaaq", "aaaaaaaaaaaaaaar", "aaaaaaaaaaaaaaas",
             "aaaaaaaaaaaaaaat", "aaaaaaaaaaaaaaau", "aaaaaaaaaaaaaaav",
             "aaaaaaaaaaaaaaaw", "aaaaaaaaaaaaaaax", "aaaaaaaaaaaaaaay",
             "aaaaaaaaaaaaaaaz", "aaaaaaaaaaaaaaba", "aaaaaaaaaaaaaabb",
             "aaaaaaaaaaaaaabc", "aaaaaaaaaaaaaabd", "aaaaaaaaaaaaaabe",
             "aaaaaaaaaaaaaabf", "aaaaaaaaaaaaaabg", "aaaaaaaaaaaaaabh",
             "aaaaaaaaaaaaaabi", "aaaaaaaaaaaaaabj", "aaaaaaaaaaaaaabk",
             "aaaaaaaaaaaaaabl", "aaaaaaaaaaaaaabm", "aaaaaaaaaaaaaabn",
             "aaaaaaaaaaaaaabo", "aaaaaaaaaaaaaabp", "aaaaaaaaaaaaaabq",
             "aaaaaaaaaaaaaabr", "aaaaaaaaaaaaaabs", "aaaaaaaaaaaaaabt",
             "aaaaaaaaaaaaaabu", "aaaaaaaaaaaaaabv", "aaaaaaaaaaaaaabw",
             "aaaaaaaaaaaaaabx", "aaaaaaaaaaaaaaby", "aaaaaaaaaaaaaabz",
             "aaaaaaaaaaaaaaca", "aaaaaaaaaaaaaacb", "aaaaaaaaaaaaaacc",
             "aaaaaaaaaaaaaacd", "aaaaaaaaaaaaaace", "aaaaaaaaaaaaaacf",
             "aaaaaaaaaaaaaacg", "aaaaaaaaaaaaaach", "aaaaaaaaaaaaaaci",
             "aaaaaaaaaaaaaacj", "aaaaaaaaaaaaaack", "aaaaaaaaaaaaaacl",
             "aaaaaaaaaaaaaacm", "aaaaaaaaaaaaaacn", "aaaaaaaaaaaaaaco",
             "aaaaaaaaaaaaaacp", "aaaaaaaaaaaaaacq", "aaaaaaaaaaaaaacr",
             "aaaaaaaaaaaaaacs", "aaaaaaaaaaaaaact", "aaaaaaaaaaaaaacu",
             "aaaaaaaaaaaaaacv", "aaaaaaaaaaaaaacw", "aaaaaaaaaaaaaacx",
             "aaaaaaaaaaaaaacy", "aaaaaaaaaaaaaacz", "aaaaaaaaaaaaaada",
             "aaaaaaaaaaaaaadb", "aaaaaaaaaaaaaadc", "aaaaaaaaaaaaaadd",
             "aaaaaaaaaaaaaade", "aaaaaaaaaaaaaadf", "aaaaaaaaaaaaaadg",
             "aaaaaaaaaaaaaadh", "aaaaaaaaaaaaaadi", "aaaaaaaaaaaaaadj",
             "aaaaaaaaaaaaaadk", "aaaaaaaaaaaaaadl", "aaaaaaaaaaaaaadm",
             "aaaaaaaaaaaaaadn", "aaaaaaaaaaaaaado", "aaaaaaaaaaaaaadp",
             "aaaaaaaaaaaaaadq", "aaaaaaaaaaaaaadr", "aaaaaaaaaaaaaads",
             "aaaaaaaaaaaaaadt", "aaaaaaaaaaaaaadu", "aaaaaaaaaaaaaadv",
             "aaaaaaaaaaaaaadw", "aaaaaaaaaaaaaadx", "aaaaaaaaaaaaaady",
             "aaaaaaaaaaaaaadz", "aaaaaaaaaaaaaaea", "aaaaaaaaaaaaaaeb",
             "aaaaaaaaaaaaaaec", "aaaaaaaaaaaaaaed", "aaaaaaaaaaaaaaee",
             "aaaaaaaaaaaaaaef", "aaaaaaaaaaaaaaeg", "aaaaaaaaaaaaaaeh",
             "aaaaaaaaaaaaaaei", "aaaaaaaaaaaaaaej", "aaaaaaaaaaaaaaek",
             "aaaaaaaaaaaaaael", "aaaaaaaaaaaaaaem", "aaaaaaaaaaaaaaen",
             "aaaaaaaaaaaaaaeo", "aaaaaaaaaaaaaaep", "aaaaaaaaaaaaaaeq",
             "aaaaaaaaaaaaaaer", "aaaaaaaaaaaaaaes", "aaaaaaaaaaaaaaet",
             "aaaaaaaaaaaaaaeu", "aaaaaaaaaaaaaaev", "aaaaaaaaaaaaaaew",
             "aaaaaaaaaaaaaaex", "aaaaaaaaaaaaaaey", "aaaaaaaaaaaaaaez",
             "aaaaaaaaaaaaaafa", "aaaaaaaaaaaaaafb", "aaaaaaaaaaaaaafc",
             "aaaaaaaaaaaaaafd", "aaaaaaaaaaaaaafe", "aaaaaaaaaaaaaaff",
             "aaaaaaaaaaaaaafg", "aaaaaaaaaaaaaafh", "aaaaaaaaaaaaaafi",
             "aaaaaaaaaaaaaafj", "aaaaaaaaaaaaaafk", "aaaaaaaaaaaaaafl",
             "aaaaaaaaaaaaaafm", "aaaaaaaaaaaaaafn", "aaaaaaaaaaaaaafo",
             "aaaaaaaaaaaaaafp", "aaaaaaaaaaaaaafq", "aaaaaaaaaaaaaafr",
             "aaaaaaaaaaaaaafs", "aaaaaaaaaaaaaaft", "aaaaaaaaaaaaaafu",
             "aaaaaaaaaaaaaafv", "aaaaaaaaaaaaaafw", "aaaaaaaaaaaaaafx",
             "aaaaaaaaaaaaaafy", "aaaaaaaaaaaaaafz", "aaaaaaaaaaaaaaga",
             "aaaaaaaaaaaaaagb", "aaaaaaaaaaaaaagc", "aaaaaaaaaaaaaagd",
             "aaaaaaaaaaaaaage", "aaaaaaaaaaaaaagf", "aaaaaaaaaaaaaagg",
             "aaaaaaaaaaaaaagh", "aaaaaaaaaaaaaagi", "aaaaaaaaaaaaaagj",
             "aaaaaaaaaaaaaagk", "aaaaaaaaaaaaaagl", "aaaaaaaaaaaaaagm",
             "aaaaaaaaaaaaaagn", "aaaaaaaaaaaaaago", "aaaaaaaaaaaaaagp",
             "aaaaaaaaaaaaaagq", "aaaaaaaaaaaaaagr", "aaaaaaaaaaaaaags",
             "aaaaaaaaaaaaaagt", "aaaaaaaaaaaaaagu", "aaaaaaaaaaaaaagv",
             "aaaaaaaaaaaaaagw", "aaaaaaaaaaaaaagx", "aaaaaaaaaaaaaagy",
             "aaaaaaaaaaaaaagz", "aaaaaaaaaaaaaaha", "aaaaaaaaaaaaaahb",
             "aaaaaaaaaaaaaahc", "aaaaaaaaaaaaaahd", "aaaaaaaaaaaaaahe",
             "aaaaaaaaaaaaaahf", "aaaaaaaaaaaaaahg", "aaaaaaaaaaaaaahh",
             "aaaaaaaaaaaaaahi", "aaaaaaaaaaaaaahj", "aaaaaaaaaaaaaahk",
             "aaaaaaaaaaaaaahl", "aaaaaaaaaaaaaahm", "aaaaaaaaaaaaaahn",
             "aaaaaaaaaaaaaaho", "aaaaaaaaaaaaaahp", "aaaaaaaaaaaaaahq",
             "aaaaaaaaaaaaaahr", "aaaaaaaaaaaaaahs", "aaaaaaaaaaaaaaht",
             "aaaaaaaaaaaaaahu", "aaaaaaaaaaaaaahv", "aaaaaaaaaaaaaahw",
             "aaaaaaaaaaaaaahx", "aaaaaaaaaaaaaahy", "aaaaaaaaaaaaaahz",
             "aaaaaaaaaaaaaaia", "aaaaaaaaaaaaaaib", "aaaaaaaaaaaaaaic",
             "aaaaaaaaaaaaaaid", "aaaaaaaaaaaaaaie", "aaaaaaaaaaaaaaif",
             "aaaaaaaaaaaaaaig", "aaaaaaaaaaaaaaih", "aaaaaaaaaaaaaaii",
             "aaaaaaaaaaaaaaij", "aaaaaaaaaaaaaaik", "aaaaaaaaaaaaaail",
             "aaaaaaaaaaaaaaim", "aaaaaaaaaaaaaain", "aaaaaaaaaaaaaaio",
             "aaaaaaaaaaaaaaip", "aaaaaaaaaaaaaaiq", "aaaaaaaaaaaaaair",
             "aaaaaaaaaaaaaais", "aaaaaaaaaaaaaait", "aaaaaaaaaaaaaaiu",
             "aaaaaaaaaaaaaaiv", "aaaaaaaaaaaaaaiw", "aaaaaaaaaaaaaaix",
             "aaaaaaaaaaaaaaiy", "aaaaaaaaaaaaaaiz", "aaaaaaaaaaaaaaja",
             "aaaaaaaaaaaaaajb", "aaaaaaaaaaaaaajc", "aaaaaaaaaaaaaajd",
             "aaaaaaaaaaaaaaje", "aaaaaaaaaaaaaajf", "aaaaaaaaaaaaaajg",
             "aaaaaaaaaaaaaajh", "aaaaaaaaaaaaaaji", "aaaaaaaaaaaaaajj",
             "aaaaaaaaaaaaaajk", "aaaaaaaaaaaaaajl", "aaaaaaaaaaaaaajm",
             "aaaaaaaaaaaaaajn", "aaaaaaaaaaaaaajo", "aaaaaaaaaaaaaajp",
             "aaaaaaaaaaaaaajq", "aaaaaaaaaaaaaajr", "aaaaaaaaaaaaaajs",
             "aaaaaaaaaaaaaajt", "aaaaaaaaaaaaaaju", "aaaaaaaaaaaaaajv",
             "aaaaaaaaaaaaaajw", "aaaaaaaaaaaaaajx", "aaaaaaaaaaaaaajy",
             "aaaaaaaaaaaaaajz", "aaaaaaaaaaaaaaka", "aaaaaaaaaaaaaakb",
             "aaaaaaaaaaaaaakc", "aaaaaaaaaaaaaakd", "aaaaaaaaaaaaaake",
             "aaaaaaaaaaaaaakf", "aaaaaaaaaaaaaakg", "aaaaaaaaaaaaaakh",
             "aaaaaaaaaaaaaaki", "aaaaaaaaaaaaaakj", "aaaaaaaaaaaaaakk",
             "aaaaaaaaaaaaaakl", "aaaaaaaaaaaaaakm", "aaaaaaaaaaaaaakn",
             "aaaaaaaaaaaaaako", "aaaaaaaaaaaaaakp", "aaaaaaaaaaaaaakq",
             "aaaaaaaaaaaaaakr", "aaaaaaaaaaaaaaks", "aaaaaaaaaaaaaakt",
             "aaaaaaaaaaaaaaku", "aaaaaaaaaaaaaakv", "aaaaaaaaaaaaaakw",
             "aaaaaaaaaaaaaakx", "aaaaaaaaaaaaaaky", "aaaaaaaaaaaaaakz",
             "aaaaaaaaaaaaaala", "aaaaaaaaaaaaaalb", "aaaaaaaaaaaaaalc",
             "aaaaaaaaaaaaaald", "aaaaaaaaaaaaaale", "aaaaaaaaaaaaaalf",
             "aaaaaaaaaaaaaalg", "aaaaaaaaaaaaaalh", "aaaaaaaaaaaaaali",
             "aaaaaaaaaaaaaalj", "aaaaaaaaaaaaaalk", "aaaaaaaaaaaaaall",
             "aaaaaaaaaaaaaalm", "aaaaaaaaaaaaaaln", "aaaaaaaaaaaaaalo",
             "aaaaaaaaaaaaaalp", "aaaaaaaaaaaaaalq", "aaaaaaaaaaaaaalr",
             "aaaaaaaaaaaaaals", "aaaaaaaaaaaaaalt", "aaaaaaaaaaaaaalu",
             "aaaaaaaaaaaaaalv", "aaaaaaaaaaaaaalw", "aaaaaaaaaaaaaalx",
             "aaaaaaaaaaaaaaly", "aaaaaaaaaaaaaalz", "aaaaaaaaaaaaaama",
             "aaaaaaaaaaaaaamb", "aaaaaaaaaaaaaamc", "aaaaaaaaaaaaaamd",
             "aaaaaaaaaaaaaame", "aaaaaaaaaaaaaamf", "aaaaaaaaaaaaaamg",
             "aaaaaaaaaaaaaamh", "aaaaaaaaaaaaaami", "aaaaaaaaaaaaaamj",
             "aaaaaaaaaaaaaamk", "aaaaaaaaaaaaaaml", "aaaaaaaaaaaaaamm",
             "aaaaaaaaaaaaaamn", "aaaaaaaaaaaaaamo", "aaaaaaaaaaaaaamp",
             "aaaaaaaaaaaaaamq", "aaaaaaaaaaaaaamr", "aaaaaaaaaaaaaams",
             "aaaaaaaaaaaaaamt", "aaaaaaaaaaaaaamu", "aaaaaaaaaaaaaamv",
             "aaaaaaaaaaaaaamw", "aaaaaaaaaaaaaamx", "aaaaaaaaaaaaaamy",
             "aaaaaaaaaaaaaamz", "aaaaaaaaaaaaaana", "aaaaaaaaaaaaaanb",
             "aaaaaaaaaaaaaanc", "aaaaaaaaaaaaaand", "aaaaaaaaaaaaaane",
             "aaaaaaaaaaaaaanf", "aaaaaaaaaaaaaang", "aaaaaaaaaaaaaanh",
             "aaaaaaaaaaaaaani", "aaaaaaaaaaaaaanj", "aaaaaaaaaaaaaank",
             "aaaaaaaaaaaaaanl", "aaaaaaaaaaaaaanm", "aaaaaaaaaaaaaann",
             "aaaaaaaaaaaaaano", "aaaaaaaaaaaaaanp", "aaaaaaaaaaaaaanq",
             "aaaaaaaaaaaaaanr", "aaaaaaaaaaaaaans", "aaaaaaaaaaaaaant",
             "aaaaaaaaaaaaaanu", "aaaaaaaaaaaaaanv", "aaaaaaaaaaaaaanw",
             "aaaaaaaaaaaaaanx", "aaaaaaaaaaaaaany", "aaaaaaaaaaaaaanz",
             "aaaaaaaaaaaaaaoa", "aaaaaaaaaaaaaaob", "aaaaaaaaaaaaaaoc",
             "aaaaaaaaaaaaaaod", "aaaaaaaaaaaaaaoe", "aaaaaaaaaaaaaaof",
             "aaaaaaaaaaaaaaog", "aaaaaaaaaaaaaaoh", "aaaaaaaaaaaaaaoi",
             "aaaaaaaaaaaaaaoj", "aaaaaaaaaaaaaaok", "aaaaaaaaaaaaaaol",
             "aaaaaaaaaaaaaaom", "aaaaaaaaaaaaaaon", "aaaaaaaaaaaaaaoo",
             "aaaaaaaaaaaaaaop", "aaaaaaaaaaaaaaoq", "aaaaaaaaaaaaaaor",
             "aaaaaaaaaaaaaaos", "aaaaaaaaaaaaaaot", "aaaaaaaaaaaaaaou",
             "aaaaaaaaaaaaaaov", "aaaaaaaaaaaaaaow", "aaaaaaaaaaaaaaox",
             "aaaaaaaaaaaaaaoy", "aaaaaaaaaaaaaaoz", "aaaaaaaaaaaaaapa",
             "aaaaaaaaaaaaaapb", "aaaaaaaaaaaaaapc", "aaaaaaaaaaaaaapd",
             "aaaaaaaaaaaaaape", "aaaaaaaaaaaaaapf", "aaaaaaaaaaaaaapg",
             "aaaaaaaaaaaaaaph", "aaaaaaaaaaaaaapi", "aaaaaaaaaaaaaapj",
             "aaaaaaaaaaaaaapk", "aaaaaaaaaaaaaapl", "aaaaaaaaaaaaaapm",
             "aaaaaaaaaaaaaapn", "aaaaaaaaaaaaaapo", "aaaaaaaaaaaaaapp",
             "aaaaaaaaaaaaaapq", "aaaaaaaaaaaaaapr", "aaaaaaaaaaaaaaps",
             "aaaaaaaaaaaaaapt", "aaaaaaaaaaaaaapu", "aaaaaaaaaaaaaapv",
             "aaaaaaaaaaaaaapw", "aaaaaaaaaaaaaapx", "aaaaaaaaaaaaaapy",
             "aaaaaaaaaaaaaapz", "aaaaaaaaaaaaaaqa", "aaaaaaaaaaaaaaqb",
             "aaaaaaaaaaaaaaqc", "aaaaaaaaaaaaaaqd", "aaaaaaaaaaaaaaqe",
             "aaaaaaaaaaaaaaqf", "aaaaaaaaaaaaaaqg", "aaaaaaaaaaaaaaqh",
             "aaaaaaaaaaaaaaqi", "aaaaaaaaaaaaaaqj", "aaaaaaaaaaaaaaqk",
             "aaaaaaaaaaaaaaql", "aaaaaaaaaaaaaaqm", "aaaaaaaaaaaaaaqn",
             "aaaaaaaaaaaaaaqo", "aaaaaaaaaaaaaaqp", "aaaaaaaaaaaaaaqq",
             "aaaaaaaaaaaaaaqr", "aaaaaaaaaaaaaaqs", "aaaaaaaaaaaaaaqt",
             "aaaaaaaaaaaaaaqu", "aaaaaaaaaaaaaaqv", "aaaaaaaaaaaaaaqw",
             "aaaaaaaaaaaaaaqx", "aaaaaaaaaaaaaaqy", "aaaaaaaaaaaaaaqz",
             "aaaaaaaaaaaaaara", "aaaaaaaaaaaaaarb", "aaaaaaaaaaaaaarc",
             "aaaaaaaaaaaaaard", "aaaaaaaaaaaaaare", "aaaaaaaaaaaaaarf",
             "aaaaaaaaaaaaaarg", "aaaaaaaaaaaaaarh", "aaaaaaaaaaaaaari",
             "aaaaaaaaaaaaaarj", "aaaaaaaaaaaaaark", "aaaaaaaaaaaaaarl",
             "aaaaaaaaaaaaaarm", "aaaaaaaaaaaaaarn", "aaaaaaaaaaaaaaro",
             "aaaaaaaaaaaaaarp", "aaaaaaaaaaaaaarq", "aaaaaaaaaaaaaarr",
             "aaaaaaaaaaaaaars", "aaaaaaaaaaaaaart", "aaaaaaaaaaaaaaru",
             "aaaaaaaaaaaaaarv", "aaaaaaaaaaaaaarw", "aaaaaaaaaaaaaarx",
             "aaaaaaaaaaaaaary", "aaaaaaaaaaaaaarz", "aaaaaaaaaaaaaasa",
             "aaaaaaaaaaaaaasb", "aaaaaaaaaaaaaasc", "aaaaaaaaaaaaaasd",
             "aaaaaaaaaaaaaase", "aaaaaaaaaaaaaasf", "aaaaaaaaaaaaaasg",
             "aaaaaaaaaaaaaash", "aaaaaaaaaaaaaasi", "aaaaaaaaaaaaaasj",
             "aaaaaaaaaaaaaask", "aaaaaaaaaaaaaasl", "aaaaaaaaaaaaaasm",
             "aaaaaaaaaaaaaasn", "aaaaaaaaaaaaaaso", "aaaaaaaaaaaaaasp",
             "aaaaaaaaaaaaaasq", "aaaaaaaaaaaaaasr", "aaaaaaaaaaaaaass",
             "aaaaaaaaaaaaaast", "aaaaaaaaaaaaaasu", "aaaaaaaaaaaaaasv",
             "aaaaaaaaaaaaaasw", "aaaaaaaaaaaaaasx", "aaaaaaaaaaaaaasy",
             "aaaaaaaaaaaaaasz", "aaaaaaaaaaaaaata", "aaaaaaaaaaaaaatb",
             "aaaaaaaaaaaaaatc", "aaaaaaaaaaaaaatd", "aaaaaaaaaaaaaate",
             "aaaaaaaaaaaaaatf", "aaaaaaaaaaaaaatg", "aaaaaaaaaaaaaath",
             "aaaaaaaaaaaaaati", "aaaaaaaaaaaaaatj", "aaaaaaaaaaaaaatk",
             "aaaaaaaaaaaaaatl", "aaaaaaaaaaaaaatm", "aaaaaaaaaaaaaatn",
             "aaaaaaaaaaaaaato", "aaaaaaaaaaaaaatp", "aaaaaaaaaaaaaatq",
             "aaaaaaaaaaaaaatr", "aaaaaaaaaaaaaats", "aaaaaaaaaaaaaatt",
             "aaaaaaaaaaaaaatu", "aaaaaaaaaaaaaatv", "aaaaaaaaaaaaaatw",
             "aaaaaaaaaaaaaatx", "aaaaaaaaaaaaaaty", "aaaaaaaaaaaaaatz",
             "aaaaaaaaaaaaaaua", "aaaaaaaaaaaaaaub", "aaaaaaaaaaaaaauc",
             "aaaaaaaaaaaaaaud", "aaaaaaaaaaaaaaue", "aaaaaaaaaaaaaauf",
             "aaaaaaaaaaaaaaug", "aaaaaaaaaaaaaauh", "aaaaaaaaaaaaaaui",
             "aaaaaaaaaaaaaauj", "aaaaaaaaaaaaaauk", "aaaaaaaaaaaaaaul",
             "aaaaaaaaaaaaaaum", "aaaaaaaaaaaaaaun", "aaaaaaaaaaaaaauo",
             "aaaaaaaaaaaaaaup", "aaaaaaaaaaaaaauq", "aaaaaaaaaaaaaaur",
             "aaaaaaaaaaaaaaus", "aaaaaaaaaaaaaaut", "aaaaaaaaaaaaaauu",
             "aaaaaaaaaaaaaauv", "aaaaaaaaaaaaaauw", "aaaaaaaaaaaaaaux",
             "aaaaaaaaaaaaaauy", "aaaaaaaaaaaaaauz", "aaaaaaaaaaaaaava",
             "aaaaaaaaaaaaaavb", "aaaaaaaaaaaaaavc", "aaaaaaaaaaaaaavd",
             "aaaaaaaaaaaaaave", "aaaaaaaaaaaaaavf", "aaaaaaaaaaaaaavg",
             "aaaaaaaaaaaaaavh", "aaaaaaaaaaaaaavi", "aaaaaaaaaaaaaavj",
             "aaaaaaaaaaaaaavk", "aaaaaaaaaaaaaavl", "aaaaaaaaaaaaaavm",
             "aaaaaaaaaaaaaavn", "aaaaaaaaaaaaaavo", "aaaaaaaaaaaaaavp",
             "aaaaaaaaaaaaaavq", "aaaaaaaaaaaaaavr", "aaaaaaaaaaaaaavs",
             "aaaaaaaaaaaaaavt", "aaaaaaaaaaaaaavu", "aaaaaaaaaaaaaavv",
             "aaaaaaaaaaaaaavw", "aaaaaaaaaaaaaavx", "aaaaaaaaaaaaaavy",
             "aaaaaaaaaaaaaavz", "aaaaaaaaaaaaaawa", "aaaaaaaaaaaaaawb",
             "aaaaaaaaaaaaaawc", "aaaaaaaaaaaaaawd", "aaaaaaaaaaaaaawe",
             "aaaaaaaaaaaaaawf", "aaaaaaaaaaaaaawg", "aaaaaaaaaaaaaawh",
             "aaaaaaaaaaaaaawi", "aaaaaaaaaaaaaawj", "aaaaaaaaaaaaaawk",
             "aaaaaaaaaaaaaawl", "aaaaaaaaaaaaaawm", "aaaaaaaaaaaaaawn",
             "aaaaaaaaaaaaaawo", "aaaaaaaaaaaaaawp", "aaaaaaaaaaaaaawq",
             "aaaaaaaaaaaaaawr", "aaaaaaaaaaaaaaws", "aaaaaaaaaaaaaawt",
             "aaaaaaaaaaaaaawu", "aaaaaaaaaaaaaawv", "aaaaaaaaaaaaaaww",
             "aaaaaaaaaaaaaawx", "aaaaaaaaaaaaaawy", "aaaaaaaaaaaaaawz",
             "aaaaaaaaaaaaaaxa", "aaaaaaaaaaaaaaxb", "aaaaaaaaaaaaaaxc",
             "aaaaaaaaaaaaaaxd", "aaaaaaaaaaaaaaxe", "aaaaaaaaaaaaaaxf",
             "aaaaaaaaaaaaaaxg", "aaaaaaaaaaaaaaxh", "aaaaaaaaaaaaaaxi",
             "aaaaaaaaaaaaaaxj", "aaaaaaaaaaaaaaxk", "aaaaaaaaaaaaaaxl",
             "aaaaaaaaaaaaaaxm", "aaaaaaaaaaaaaaxn", "aaaaaaaaaaaaaaxo",
             "aaaaaaaaaaaaaaxp", "aaaaaaaaaaaaaaxq", "aaaaaaaaaaaaaaxr",
             "aaaaaaaaaaaaaaxs", "aaaaaaaaaaaaaaxt", "aaaaaaaaaaaaaaxu",
             "aaaaaaaaaaaaaaxv", "aaaaaaaaaaaaaaxw", "aaaaaaaaaaaaaaxx",
             "aaaaaaaaaaaaaaxy", "aaaaaaaaaaaaaaxz", "aaaaaaaaaaaaaaya",
             "aaaaaaaaaaaaaayb", "aaaaaaaaaaaaaayc", "aaaaaaaaaaaaaayd",
             "aaaaaaaaaaaaaaye", "aaaaaaaaaaaaaayf", "aaaaaaaaaaaaaayg",
             "aaaaaaaaaaaaaayh", "aaaaaaaaaaaaaayi", "aaaaaaaaaaaaaayj",
             "aaaaaaaaaaaaaayk", "aaaaaaaaaaaaaayl", "aaaaaaaaaaaaaaym",
             "aaaaaaaaaaaaaayn", "aaaaaaaaaaaaaayo", "aaaaaaaaaaaaaayp",
             "aaaaaaaaaaaaaayq", "aaaaaaaaaaaaaayr", "aaaaaaaaaaaaaays",
             "aaaaaaaaaaaaaayt", "aaaaaaaaaaaaaayu", "aaaaaaaaaaaaaayv",
             "aaaaaaaaaaaaaayw", "aaaaaaaaaaaaaayx", "aaaaaaaaaaaaaayy",
             "aaaaaaaaaaaaaayz", "aaaaaaaaaaaaaaza", "aaaaaaaaaaaaaazb",
             "aaaaaaaaaaaaaazc", "aaaaaaaaaaaaaazd", "aaaaaaaaaaaaaaze",
             "aaaaaaaaaaaaaazf", "aaaaaaaaaaaaaazg", "aaaaaaaaaaaaaazh",
             "aaaaaaaaaaaaaazi", "aaaaaaaaaaaaaazj", "aaaaaaaaaaaaaazk",
             "aaaaaaaaaaaaaazl", "aaaaaaaaaaaaaazm", "aaaaaaaaaaaaaazn",
             "aaaaaaaaaaaaaazo", "aaaaaaaaaaaaaazp", "aaaaaaaaaaaaaazq",
             "aaaaaaaaaaaaaazr", "aaaaaaaaaaaaaazs", "aaaaaaaaaaaaaazt",
             "aaaaaaaaaaaaaazu", "aaaaaaaaaaaaaazv", "aaaaaaaaaaaaaazw",
             "aaaaaaaaaaaaaazx", "aaaaaaaaaaaaaazy", "aaaaaaaaaaaaaazz",
             "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaab", "aaaaaaaaaaaaaaac",
             "aaaaaaaaaaaaaaad", "aaaaaaaaaaaaaaae", "aaaaaaaaaaaaaaaf",
             "aaaaaaaaaaaaaaag", "aaaaaaaaaaaaaaah", "aaaaaaaaaaaaaaai",
             "aaaaaaaaaaaaaaaj", "aaaaaaaaaaaaaaak", "aaaaaaaaaaaaaaal",
             "aaaaaaaaaaaaaaam", "aaaaaaaaaaaaaaan", "aaaaaaaaaaaaaaao",
             "aaaaaaaaaaaaaaap", "aaaaaaaaaaaaaaaq", "aaaaaaaaaaaaaaar",
             "aaaaaaaaaaaaaaas", "aaaaaaaaaaaaaaat", "aaaaaaaaaaaaaaau",
             "aaaaaaaaaaaaaaav", "aaaaaaaaaaaaaaaw", "aaaaaaaaaaaaaaax",
             "aaaaaaaaaaaaaaay", "aaaaaaaaaaaaaaaz", "aaaaaaaaaaaaaaba",
             "aaaaaaaaaaaaaabb", "aaaaaaaaaaaaaabc", "aaaaaaaaaaaaaabd",
             "aaaaaaaaaaaaaabe", "aaaaaaaaaaaaaabf", "aaaaaaaaaaaaaabg",
             "aaaaaaaaaaaaaabh", "aaaaaaaaaaaaaabi", "aaaaaaaaaaaaaabj",
             "aaaaaaaaaaaaaabk", "aaaaaaaaaaaaaabl", "aaaaaaaaaaaaaabm",
             "aaaaaaaaaaaaaabn", "aaaaaaaaaaaaaabo", "aaaaaaaaaaaaaabp",
             "aaaaaaaaaaaaaabq", "aaaaaaaaaaaaaabr", "aaaaaaaaaaaaaabs",
             "aaaaaaaaaaaaaabt", "aaaaaaaaaaaaaabu", "aaaaaaaaaaaaaabv",
             "aaaaaaaaaaaaaabw", "aaaaaaaaaaaaaabx", "aaaaaaaaaaaaaaby",
             "aaaaaaaaaaaaaabz", "aaaaaaaaaaaaaaca", "aaaaaaaaaaaaaacb",
             "aaaaaaaaaaaaaacc", "aaaaaaaaaaaaaacd", "aaaaaaaaaaaaaace",
             "aaaaaaaaaaaaaacf", "aaaaaaaaaaaaaacg", "aaaaaaaaaaaaaach",
             "aaaaaaaaaaaaaaci", "aaaaaaaaaaaaaacj", "aaaaaaaaaaaaaack",
             "aaaaaaaaaaaaaacl", "aaaaaaaaaaaaaacm", "aaaaaaaaaaaaaacn",
             "aaaaaaaaaaaaaaco", "aaaaaaaaaaaaaacp", "aaaaaaaaaaaaaacq",
             "aaaaaaaaaaaaaacr", "aaaaaaaaaaaaaacs", "aaaaaaaaaaaaaact",
             "aaaaaaaaaaaaaacu", "aaaaaaaaaaaaaacv", "aaaaaaaaaaaaaacw",
             "aaaaaaaaaaaaaacx", "aaaaaaaaaaaaaacy", "aaaaaaaaaaaaaacz",
             "aaaaaaaaaaaaaada", "aaaaaaaaaaaaaadb", "aaaaaaaaaaaaaadc",
             "aaaaaaaaaaaaaadd", "aaaaaaaaaaaaaade", "aaaaaaaaaaaaaadf",
             "aaaaaaaaaaaaaadg", "aaaaaaaaaaaaaadh", "aaaaaaaaaaaaaadi",
             "aaaaaaaaaaaaaadj", "aaaaaaaaaaaaaadk", "aaaaaaaaaaaaaadl",
             "aaaaaaaaaaaaaadm", "aaaaaaaaaaaaaadn", "aaaaaaaaaaaaaado",
             "aaaaaaaaaaaaaadp", "aaaaaaaaaaaaaadq", "aaaaaaaaaaaaaadr",
             "aaaaaaaaaaaaaads", "aaaaaaaaaaaaaadt", "aaaaaaaaaaaaaadu",
             "aaaaaaaaaaaaaadv", "aaaaaaaaaaaaaadw", "aaaaaaaaaaaaaadx",
             "aaaaaaaaaaaaaady", "aaaaaaaaaaaaaadz", "aaaaaaaaaaaaaaea",
             "aaaaaaaaaaaaaaeb", "aaaaaaaaaaaaaaec", "aaaaaaaaaaaaaaed",
             "aaaaaaaaaaaaaaee", "aaaaaaaaaaaaaaef", "aaaaaaaaaaaaaaeg",
             "aaaaaaaaaaaaaaeh", "aaaaaaaaaaaaaaei", "aaaaaaaaaaaaaaej",
             "aaaaaaaaaaaaaaek", "aaaaaaaaaaaaaael", "aaaaaaaaaaaaaaem",
             "aaaaaaaaaaaaaaen", "aaaaaaaaaaaaaaeo", "aaaaaaaaaaaaaaep",
             "aaaaaaaaaaaaaaeq", "aaaaaaaaaaaaaaer", "aaaaaaaaaaaaaaes",
             "aaaaaaaaaaaaaaet", "aaaaaaaaaaaaaaeu", "aaaaaaaaaaaaaaev",
             "aaaaaaaaaaaaaaew", "aaaaaaaaaaaaaaex", "aaaaaaaaaaaaaaey",
             "aaaaaaaaaaaaaaez", "aaaaaaaaaaaaaafa", "aaaaaaaaaaaaaafb",
             "aaaaaaaaaaaaaafc", "aaaaaaaaaaaaaafd", "aaaaaaaaaaaaaafe",
             "aaaaaaaaaaaaaaff", "aaaaaaaaaaaaaafg", "aaaaaaaaaaaaaafh",
             "aaaaaaaaaaaaaafi", "aaaaaaaaaaaaaafj", "aaaaaaaaaaaaaafk",
             "aaaaaaaaaaaaaafl", "aaaaaaaaaaaaaafm", "aaaaaaaaaaaaaafn",
             "aaaaaaaaaaaaaafo", "aaaaaaaaaaaaaafp", "aaaaaaaaaaaaaafq",
             "aaaaaaaaaaaaaafr", "aaaaaaaaaaaaaafs", "aaaaaaaaaaaaaaft",
             "aaaaaaaaaaaaaafu", "aaaaaaaaaaaaaafv", "aaaaaaaaaaaaaafw",
             "aaaaaaaaaaaaaafx", "aaaaaaaaaaaaaafy", "aaaaaaaaaaaaaafz",
             "aaaaaaaaaaaaaaga", "aaaaaaaaaaaaaagb", "aaaaaaaaaaaaaagc",
             "aaaaaaaaaaaaaagd", "aaaaaaaaaaaaaage", "aaaaaaaaaaaaaagf",
             "aaaaaaaaaaaaaagg", "aaaaaaaaaaaaaagh", "aaaaaaaaaaaaaagi",
             "aaaaaaaaaaaaaagj", "aaaaaaaaaaaaaagk", "aaaaaaaaaaaaaagl",
             "aaaaaaaaaaaaaagm", "aaaaaaaaaaaaaagn", "aaaaaaaaaaaaaago",
             "aaaaaaaaaaaaaagp", "aaaaaaaaaaaaaagq", "aaaaaaaaaaaaaagr",
             "aaaaaaaaaaaaaags", "aaaaaaaaaaaaaagt", "aaaaaaaaaaaaaagu",
             "aaaaaaaaaaaaaagv", "aaaaaaaaaaaaaagw", "aaaaaaaaaaaaaagx",
             "aaaaaaaaaaaaaagy", "aaaaaaaaaaaaaagz", "aaaaaaaaaaaaaaha",
             "aaaaaaaaaaaaaahb", "aaaaaaaaaaaaaahc", "aaaaaaaaaaaaaahd",
             "aaaaaaaaaaaaaahe", "aaaaaaaaaaaaaahf", "aaaaaaaaaaaaaahg",
             "aaaaaaaaaaaaaahh", "aaaaaaaaaaaaaahi", "aaaaaaaaaaaaaahj",
             "aaaaaaaaaaaaaahk", "aaaaaaaaaaaaaahl", "aaaaaaaaaaaaaahm",
             "aaaaaaaaaaaaaahn", "aaaaaaaaaaaaaaho", "aaaaaaaaaaaaaahp",
             "aaaaaaaaaaaaaahq", "aaaaaaaaaaaaaahr", "aaaaaaaaaaaaaahs",
             "aaaaaaaaaaaaaaht", "aaaaaaaaaaaaaahu", "aaaaaaaaaaaaaahv",
             "aaaaaaaaaaaaaahw", "aaaaaaaaaaaaaahx", "aaaaaaaaaaaaaahy",
             "aaaaaaaaaaaaaahz", "aaaaaaaaaaaaaaia", "aaaaaaaaaaaaaaib",
             "aaaaaaaaaaaaaaic", "aaaaaaaaaaaaaaid", "aaaaaaaaaaaaaaie",
             "aaaaaaaaaaaaaaif", "aaaaaaaaaaaaaaig", "aaaaaaaaaaaaaaih",
             "aaaaaaaaaaaaaaii", "aaaaaaaaaaaaaaij", "aaaaaaaaaaaaaaik",
             "aaaaaaaaaaaaaail", "aaaaaaaaaaaaaaim", "aaaaaaaaaaaaaain",
             "aaaaaaaaaaaaaaio", "aaaaaaaaaaaaaaip", "aaaaaaaaaaaaaaiq",
             "aaaaaaaaaaaaaair", "aaaaaaaaaaaaaais", "aaaaaaaaaaaaaait",
             "aaaaaaaaaaaaaaiu", "aaaaaaaaaaaaaaiv", "aaaaaaaaaaaaaaiw",
             "aaaaaaaaaaaaaaix", "aaaaaaaaaaaaaaiy", "aaaaaaaaaaaaaaiz",
             "aaaaaaaaaaaaaaja", "aaaaaaaaaaaaaajb", "aaaaaaaaaaaaaajc",
             "aaaaaaaaaaaaaajd", "aaaaaaaaaaaaaaje", "aaaaaaaaaaaaaajf",
             "aaaaaaaaaaaaaajg", "aaaaaaaaaaaaaajh", "aaaaaaaaaaaaaaji",
             "aaaaaaaaaaaaaajj", "aaaaaaaaaaaaaajk", "aaaaaaaaaaaaaajl",
             "aaaaaaaaaaaaaajm", "aaaaaaaaaaaaaajn", "aaaaaaaaaaaaaajo",
             "aaaaaaaaaaaaaajp", "aaaaaaaaaaaaaajq", "aaaaaaaaaaaaaajr",
             "aaaaaaaaaaaaaajs", "aaaaaaaaaaaaaajt", "aaaaaaaaaaaaaaju",
             "aaaaaaaaaaaaaajv", "aaaaaaaaaaaaaajw", "aaaaaaaaaaaaaajx",
             "aaaaaaaaaaaaaajy", "aaaaaaaaaaaaaajz", "aaaaaaaaaaaaaaka",
             "aaaaaaaaaaaaaakb", "aaaaaaaaaaaaaakc", "aaaaaaaaaaaaaakd",
             "aaaaaaaaaaaaaake", "aaaaaaaaaaaaaakf", "aaaaaaaaaaaaaakg",
             "aaaaaaaaaaaaaakh", "aaaaaaaaaaaaaaki", "aaaaaaaaaaaaaakj",
             "aaaaaaaaaaaaaakk", "aaaaaaaaaaaaaakl", "aaaaaaaaaaaaaakm",
             "aaaaaaaaaaaaaakn", "aaaaaaaaaaaaaako", "aaaaaaaaaaaaaakp",
             "aaaaaaaaaaaaaakq", "aaaaaaaaaaaaaakr", "aaaaaaaaaaaaaaks",
             "aaaaaaaaaaaaaakt", "aaaaaaaaaaaaaaku", "aaaaaaaaaaaaaakv",
             "aaaaaaaaaaaaaakw", "aaaaaaaaaaaaaakx", "aaaaaaaaaaaaaaky",
             "aaaaaaaaaaaaaakz", "aaaaaaaaaaaaaala", "aaaaaaaaaaaaaalb",
             "aaaaaaaaaaaaaalc", "aaaaaaaaaaaaaald", "aaaaaaaaaaaaaale",
             "aaaaaaaaaaaaaalf", "aaaaaaaaaaaaaalg", "aaaaaaaaaaaaaalh",
             "aaaaaaaaaaaaaali", "aaaaaaaaaaaaaalj", "aaaaaaaaaaaaaalk",
             "aaaaaaaaaaaaaall"]

    print(s.findWords(board, words))
    print(timeit(lambda: s.findWords(board, words), number=10))

    # print(s.get_alphabet_postions(board))
    board = ["baabab", "abaaaa", "abaaab", "ababba", "aabbab", "aabbba", "aabaab"]
    words = ["aab"
     "bbaabaabaaaaabaababaaaaababb", "aabbaaabaaabaabaaaaaabbaaaba",
     "babaababbbbbbbaabaababaabaaa", "bbbaaabaabbaaababababbbbbaaa",
     "babbabbbbaabbabaaaaaabbbaaab", "bbbababbbbbbbababbabbbbbabaa",
     "babababbababaabbbbabbbbabbba", "abbbbbbaabaaabaaababaabbabba",
     "aabaabababbbbbbababbbababbaa", "aabbbbabbaababaaaabababbaaba",
     "ababaababaaabbabbaabbaabbaba", "abaabbbaaaaababbbaaaaabbbaab",
     "aabbabaabaabbabababaaabbbaab", "baaabaaaabbabaaabaabababaaaa",
     "aaabbabaaaababbabbaabbaabbaa", "aaabaaaaabaabbabaabbbbaabaaa",
     "abbaabbaaaabbaababababbaabbb", "baabaababbbbaaaabaaabbababbb",
     "aabaababbaababbaaabaabababab", "abbaaabbaabaabaabbbbaabbbbbb",
     "aaababaabbaaabbbaaabbabbabab", "bbababbbabbbbabbbbabbbbbabaa",
     "abbbaabbbaaababbbababbababba", "bbbbbbbabbbababbabaabababaab",
     "aaaababaabbbbabaaaaabaaaaabb", "bbaaabbbbabbaaabbaabbabbaaba",
     "aabaabbbbaabaabbabaabababaaa", "abbababbbaababaabbababababbb",
     "aabbbabbaaaababbbbabbababbbb", "babbbaabababbbbbbbbbaabbabaa"]
    print(s.findWords(board, words))
    print(timeit(lambda: s.findWords(board, words), number=10))
