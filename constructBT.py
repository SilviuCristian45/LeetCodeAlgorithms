# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        currentNode = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        currentNode.left = self.buildTree(preorder=preorder[1: mid+1], inorder=inorder[:mid])
        currentNode.right = self.buildTree(preorder=preorder[mid+1:], inorder=inorder[mid+1:])

        return currentNode

s = Solution()
res = s.buildTree()