# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from sys import maxunicode
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        depthLeft = 1 + self.maxDepth(root.left)
        depthRight = 1 + self.maxDepth(root.right)

        return max(depthLeft, depthRight)

s = Solution()
s.maxDepth([TreeNode(3),TreeNode(9),TreeNode(20),TreeNode(None),TreeNode(None),TreeNode(15),TreeNode(7)])