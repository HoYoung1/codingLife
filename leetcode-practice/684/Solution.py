from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        self.parents = [n for _ in range(n)]

    # 1. 경로 압축
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])  # 재귀를 돌며 해당 부모를 최상위 노드로 설정
        return self.parents[x]



