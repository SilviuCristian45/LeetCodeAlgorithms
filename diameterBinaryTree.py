# Definition for a binary tree node.
from operator import truediv
from posixpath import isabs


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)
            return 1 + max(left, right)
        
        dfs(root)

        return res[0]

    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return (True, -1)

            left = dfs(root.left)
            right = dfs(root.right)

            return ( left[0] and right[0] and abs(left[1] - right[1]) <= 1 , 1 + max(left[1], right[1]) )
        return dfs(root)[0]
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return p.val == q.val and left and right
    
    def binaryTreeTraversal(self, root: TreeNode) -> list[list[int]]:
        #facem un bfs
        queue = [root]
        result = []

        while len(queue) > 0:
            
            tempResult = []
            for _ in range(len(queue)):
                currentNode = queue.pop(0)   
                if currentNode:   
                    tempResult.append(currentNode.val)
                    queue.append(currentNode.left)
                    queue.append(currentNode.right)
                
            if len(tempResult) > 0:
                result.append(tempResult)
        return result
    
    def rightSideView(self, root: TreeNode) -> list[int]:
        queue = [root]
        result = []

        while len(queue) > 0:
            rightSide = None
            for _ in range(len(queue)):
                currentNode = queue.pop() 
                if currentNode:   
                    rightSide = currentNode
                    queue.append(currentNode.left)
                    queue.append(currentNode.right)
                
            if rightSide:
                result.append(rightSide.val)
        return result


s = Solution()
four = TreeNode(4)
five = TreeNode(5)
two = TreeNode(2,four, five)
three = TreeNode(3)
head = TreeNode(1,two, three)
res = s.diameterOfBinaryTree(head)
print(res)
res2 = s.isBalanced(head)
print(res2)

res3 = s.binaryTreeTraversal(head)
print(res3)