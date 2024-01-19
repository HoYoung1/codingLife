# from typing import List
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
# 3 x 3 matrix
# 0,0 -> 0,2
# 0,1 -> 1,2
# 0,2 -> 2,2
#
# 1,0 -> 0,1
# 1,1 -> 1,1
# 1,2 -> 2,1
#
# 2,0 -> 0,0
# 2,1 -> 1,0
# 2,2 -> 2,0
#
# 4 x 4 matrix
# 0,0 -> 0,3
# 0,1 -> 1,3
# 0,2 -> 2,3
# 0,3 -> 3,3
#
#
from typing import List


class Solution:
    def rotate(self, x: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(x)):
            for j in range(i,len(x)):
                x[i][j],x[j][i]=x[j][i],x[i][j]
        for i in range(len(x)):
            x[i].reverse()
