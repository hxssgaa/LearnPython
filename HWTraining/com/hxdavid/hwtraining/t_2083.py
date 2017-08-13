# coding=utf-8
"""
Sudoku-Java

问题描述：数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，推算出所有剩余空格的数字，
并且满足每一行、每一列、每一个粗线宫内的数字均含1-9，并且不重复。
输入：
包含已知数字的9X9盘面数组[空缺位以数字0表示]
输出：
完整的9X9盘面数组
0 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
0 4 5 2 7 6 8 3 1
"""


class Solution(object):
    def solve_sudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.solve(board, 0)

    def solve(self, board, pos):
        """
        :type board: list[list[str]]
        :type pos: 0
        :rtype: bool
        """
        if pos >= 81:
            return True
        i, j = pos // 9, pos % 9
        if board[i][j] == '0':
            for c in range(1, 10):  # Trial. Try 1 through 9 for each cell
                if self.is_valid(board, i, j, c):
                    board[i][j] = str(c)  # Put c for this cell
                    if self.solve(board, pos + 1):  # If it's the solution return true
                        return True
                    else:
                        board[i][j] = '0'  # Otherwise go back
            return False
        return self.solve(board, pos + 1)

    def is_valid(self, board, i, j, c):
        """
        :type board: list[list[str]]
        :type i: int
        :type j: int
        :type c: int
        :rtype: bool
        """
        c = str(c)
        # Check column
        for row in range(9):
            if board[row][j] == c:
                return False
        # Check row
        for col in range(9):
            if board[i][col] == c:
                return False
        # Check 3 x 3 block
        for row in range((i // 3) * 3, (i // 3) * 3 + 3):
            for col in range((j // 3) * 3, (j // 3) * 3 + 3):
                if board[row][col] == c:
                    return False
        return True


def main():
    board = [raw_input().split() for _ in range(9)]
    Solution().solve_sudoku(board)
    for i in range(9):
        print " ".join(board[i])


if __name__ == '__main__':
    main()
