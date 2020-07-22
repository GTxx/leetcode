from typing import List
from itertools import product


class Solution:
    def mark_mask(self, mask, num, points):
        for x, y in points:
            mask[x][y] = num

    def solve1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Time limit exceeded
        """
        if not board:
            return
        num = 2  # 0 represent boarder O, 1 represent X, other number represent an connected area
        num_points = {0: []}
        mask = [[1 for _ in row] for row in board]
        for idx, letter in enumerate(board[0]):
            if letter == 'O':
                mask[0][idx] = 0
        for idx in range(len(board)):
            if board[idx][0] == 'O':
                mask[idx][0] = 0
        for i, row in enumerate(board[1:], 1):
            for j, letter in enumerate(row[1:], 1):
                if letter == 'X':
                    continue
                if letter == 'O':
                    if i == 0 or i == len(board) - 1 or j == 0 or j == len(row) - 1:
                        mask[i][j] = 0
                        if mask[i - 1][j] not in [0, 1]:
                            self.mark_mask(mask, 0, num_points[mask[i - 1][j]])
                        if mask[i][j - 1] not in [0, 1]:
                            self.mark_mask(mask, 0, num_points[mask[i][j - 1]])
                    else:
                        if mask[i][j - 1] == 1 and mask[i - 1][j] == 1:
                            mask[i][j] = num
                            num_points[num] = [(i, j)]
                            num += 1
                        elif mask[i][j - 1] == 1 and mask[i - 1][j] != 1:
                            mask[i][j] = mask[i - 1][j]
                            num_points[mask[i - 1][j]].append((i, j))
                        elif mask[i][j - 1] != 1 and mask[i - 1][j] == 1:
                            mask[i][j] = mask[i][j - 1]
                            num_points[mask[i][j - 1]].append((i, j))
                        else:
                            if mask[i][j - 1] != 0 and mask[i - 1][j] != 0:
                                mask[i][j] = mask[i][j - 1]
                                num_points[mask[i][j]].append((i, j))
                                num_points[mask[i][j]] += num_points[mask[i - 1][j]]
                                self.mark_mask(mask, mask[i][j], num_points[mask[i - 1][j]])
                            elif mask[i][j - 1] == 0:
                                mask[i][j] = 0
                                num_points[0].append((i, j))
                                self.mark_mask(mask, 0, num_points[mask[i - 1][j]])
                            elif mask[i - 1][j] == 0:
                                mask[i][j] = 0
                                num_points[0].append((i, j))
                                self.mark_mask(mask, 0, num_points[mask[i][j - 1]])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if mask[i][j] != 0:
                    board[i][j] = 'X'

    def dfs(self, start, board: List[List[str]]) -> None:
        width, height = len(board[0]), len(board)
        x, y = start
        neighbor = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
        neighbor = [(i, j) for i, j in neighbor if 0 <= i < height and 0 <= j < width]
        neighbor = [(i, j) for i, j in neighbor if board[i][j] == 'O']
        board[x][y] = 'V'
        for i, j in neighbor:
            self.dfs((i, j), board)

    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        width, height = len(board[0]), len(board)
        for y in range(width):
            if board[0][y] == "O":
                self.dfs((0, y), board)
            if board[-1][y] == "O":
                self.dfs((height - 1, y), board)
        for x in range(height):
            if board[x][0] == "O":
                self.dfs((x, 0), board)
            if board[x][-1] == "O":
                self.dfs((x, width - 1), board)
        for x in range(height):
            for y in range(width):
                if board[x][y] == "V":
                    board[x][y] = "O"
                else:
                    board[x][y] = "X"
