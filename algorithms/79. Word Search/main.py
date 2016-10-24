class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                used_positions = set()
                if self.find_word(board, row, col, word, used_positions):
                    return True
        return False

    def find_word(self, board, row, col, word, used_positions):
        if len(word) == 1:
            if board[row][col] == word[0]:
                return True
            else:
                return False
        else:
            first, left = word[0], word[1:]
            if first != board[row][col]:
                return False
            used_positions1 = set(used_positions)
            used_positions1.add((row, col))

            locations = self.get_ajacent_positions(board, row, col, used_positions1)
            for location in locations:
                r, c = location
                if self.find_word(board, r, c, left, used_positions1):
                    return True
            return False

    def is_position_ok(self, position, max_row, max_col, used_positions):
        if position in used_positions:
            return False
        row, col = position
        if row < 0 or row >= max_row or col < 0 or col >= max_col:
            return False
        return True

    def get_ajacent_positions(self, board, row, col, used_positions):
        neighbor_positions = [
            (row-1, col), (row+1, col), (row, col-1), (row, col+1)
        ]
        return [position for position in neighbor_positions
                if self.is_position_ok(position, len(board), len(board[0]), used_positions)]

    def find_letter(self, board, letter):
        res = []
        for idx1, row in enumerate(board):
            for idx2, col in enumerate(row):
                if col == letter:
                    res.append((idx1, idx2))
        return res


if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    s = Solution()
    # print(s.find(board, 'A'))
    # print(s.exist(board, "ABCCED"))
    # print(s.exist(board, "SEE"))
    # print(s.exist(board, "ABCB"))
    #
    # board = ["ABCE","SFCS","ADEE"]
    # print(s.exist(board, 'ABCCED'))

    board = ["CAA", "AAA", "BCD"]
    assert(s.exist(board, "AAB") == True)
    board = ["ABCE","SFES","ADEE"]
    assert(s.exist(board, "ABCESEEEFS") == True)

    board = ["aa"]
    assert(s.exist(board, "aaa") == False)
