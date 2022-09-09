# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 and root2 and root1.val == root2.val:
            return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        if root is None:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.length, subRoot) or self.isSubtree(root.right, subRoot)


s = Solution()
s.isSubtree()