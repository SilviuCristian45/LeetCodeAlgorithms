class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxValue):
            if root == None:
                return 0
            res = 0
            if root.val >= maxValue:
                res = 1
            maxValue = max(maxValue, root.val)
            
            left = dfs(root.left, maxValue)
            right = dfs(root.right, maxValue)

            return res + left + right
        
        return dfs(root, root.val)

s = Solution()
d = TreeNode(11)
c = TreeNode(99, right=d)
b = TreeNode(12)
a = TreeNode(35, b, c)
res = s.goodNodes(a)
print(res)