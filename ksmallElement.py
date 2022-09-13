# Definition for a binary tree node.
from threading import local


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = None
        def inorder(root: TreeNode):
            nonlocal k, result
            if not root:
                return
            inorder(root.left)
            k -= 1
            if k == 0:
                result = root.val 
            inorder(root.right)
        
        inorder(root)
        return result

s = Solution()
c = TreeNode(21)
b = TreeNode(19, right=c)
a = TreeNode(26, left=b)
x = TreeNode(32, left=a)
res = s.kthSmallest(root=x, k=2)
print(res)