# Definition for a binary tree node.
# from typing import Optional, Self
# from typing_extensions import Self
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         return self.recur(root)
#
#     def recur(self, current_node: Optional[TreeNode]):
#         if current_node is None:
#             return True
#         if current_node.left is not None and current_node.left.val >= current_node.val:
#             return False
#         if current_node.right is not None and current_node.right.val <= current_node.val:
#             return False
#
#         return self.recur(current_node.left) and self.recur(current_node.right)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recur(root, -sys.maxsize, sys.maxsize)

    def recur(self, current_node: Optional[TreeNode], low, high):
        if current_node is None:
            return True
        if not (low < current_node.val < high):
            return False

        return self.recur(current_node.left, low, current_node.val) \
               and self.recur(current_node.right, current_node.val, high)



t = TreeNode(2, TreeNode(1), TreeNode(3))
assert Solution().isValidBST(t) is True

t = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
assert Solution().isValidBST(t) is False

t = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
assert Solution().isValidBST(t) is False
