from collections import defaultdict
from typing import List

# 싸이클이 있는지 판단하면되는듯
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = [False] * numCourses

        graph = defaultdict(list)





numCourses = [[1,0]]
assert Solution().canFinish(len(numCourses), numCourses) == True
numCourses = [[1,0],[0,1]]
assert Solution().canFinish(len(numCourses), numCourses) == False

2000000

1 <- 0
1 <- 2 <- 0
numCourses = [[1,0],[1,2], [2,0]]
assert Solution().canFinish(len(numCourses), numCourses) == True

0 <- 1 < -2 <- 0
numCourses = [[0,1],[1,2], [2,0]]
assert Solution().canFinish(len(numCourses), numCourses) == False

