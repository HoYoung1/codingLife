from typing import List


def check_valid(temp):
    for s in temp:
        if temp.count(s) > 1:
            return True
    return False


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for line in board:
            temp = []
            for s in line:
                if s != '.':
                    temp.append(s)
            if check_valid(temp):
                return False

        # column
        for j in range(9):
            temp = []
            for i in range(9):
                if board[i][j] != '.':
                    temp.append(board[i][j])
            if check_valid(temp):
                return False

        # 3x3 area
        # 0,0, 0,3 0,6
        # 3,0, 3,3 3,6
        # 6,0, 6,3 6,6

        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                for i in range(x, 3):
                    temp = []
                    for j in range(y, 3):
                        if board[i][j] != '.':
                            temp.append(board[i][j])
                if check_valid(temp):
                    return False
        return True







# input_array = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
#
# assert Solution().isValidSudoku(input_array) is True
#
# input_array = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
#
# assert Solution().isValidSudoku(input_array) is False

input_array = [[".",".",".",".","5",".",".","1","."]
    ,[".","4",".","3",".",".",".",".","."]
    ,[".",".",".",".",".","3",".",".","1"]
    ,["8",".",".",".",".",".",".","2","."]
    ,[".",".","2",".","7",".",".",".","."]
    ,[".","1","5",".",".",".",".",".","."]
    ,[".",".",".",".",".","2",".",".","."]
    ,[".","2",".","9",".",".",".",".","."]
    ,[".",".","4",".",".",".",".",".","."]]

assert Solution().isValidSudoku(input_array) is False