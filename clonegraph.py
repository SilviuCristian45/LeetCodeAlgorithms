
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        visited = dict()

        def dfs(node: Node):
            if node in visited:
                return visited[node]
            copy = Node(node.val)
            visited[node] = copy
            for neighbour in node.neighbors:
                copy.neighbors.append( dfs(neighbour))
            return copy
        
        return dfs(node) if node else None

s = Solution()
s.cloneGraph()