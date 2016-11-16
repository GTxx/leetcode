class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def is_in_battle(row, col):
            left_r, left_c = row, col-1
            up_r, up_c = row-1, col
            if left_c >= 0 and board[left_r][left_c] == "X":
                return True
            if up_r >= 0 and board[up_r][up_c] == "X":
                return True
            return False

        total = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                c = board[row][col]

                if c == 'X':
                    if is_in_battle(row, col):
                        continue
                    else:
                        total += 1
        return total


if __name__ == "__main__":
    s = Solution()
    print s.countBattleships(['X..X', '...X', '...X'])
    print s.countBattleships(['XXX'])


