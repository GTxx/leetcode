class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        first = word[0]
        positions = self.find(board, first)
        for position in positions:
            used_positions = set()
            r, c = position
            if self.is_ok(board, r, c, word, used_positions):
                return True
        return False

    def is_ok(self, board, row, col, word, used_positions):
        if len(word) == 1:
            if board[row][col] == word[0]:
                print(row, col)
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
                if self.is_ok(board, r, c, left, used_positions):
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

    def find(self, board, letter):
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

    # board = ["CAA", "AAA", "BCD"]
    # print(s.exist(board, "AAB"))
    board = ["ABCE","SFES","ADEE"]
    print(s.exist(board, "ABCESEEEFS"))
