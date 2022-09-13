# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root, left, right):
            if not root:
                return True
            if not (root.val < right and root.val > left):
                return False
            return dfs(root.left, left, min(root.val, right)) and dfs(root.right, max(root.val, left), right)

        return dfs(root, -2**31, 2**31)
    
    def lessThanRight2(self, value, root) -> bool:
            if not root:
                return True
            return value < root.val and (self.lessThanRight2(value, root.left) and self.lessThanRight2(value, root.right))

    def isValidBST2(self, root: TreeNode) -> bool: #bruteForce
        def lessThanRight(value, root):
            if not root:
                return True
            return value < root.val and (lessThanRight(value, root.left) and lessThanRight(value, root.right))
        def moreThanLeft(value, root):
            if not root:
                return True
            return value > root.val and (moreThanLeft(value, root.left) and moreThanLeft(value, root.right))
        def main(root):
            if not root:
                return True
            currentVal = moreThanLeft(root.val, root.left) and lessThanRight(root.val, root.right)
            return currentVal and main(root.left) and main(root.right)

        return main(root)
        


s = Solution()
c = TreeNode(27)
b = TreeNode(19, right=c)
a = TreeNode(26, left=b)
x = TreeNode(32, left=a)
res = s.isValidBST2(x)
print(res)