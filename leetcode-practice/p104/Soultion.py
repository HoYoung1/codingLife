# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recur(0, root)

    def recur(self, current_depth: int, current_node: Optional[TreeNode]) -> int:
        if current_node is None:
            return current_depth
        return max(self.recur(current_depth + 1, current_node.left), self.recur(current_depth + 1, current_node.right))

t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert Solution().maxDepth(t) == 3