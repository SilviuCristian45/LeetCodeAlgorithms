from fileinput import close


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
            
        backtrack(0, 0)
        return res

        # def backtrackv2(openN, closedN):
        #     if openN == closedN == n:
        #         return ""
        #     if openN < n:
        #         return "(" + backtrackv2(openN=openN+1, closedN=closedN)
        #     if closedN < openN:
        #         return ")" + backtrackv2(openN, closedN+1)
        
        return backtrackv2(0, 0)

s = Solution()
res = s.generateParenthesis(3)
print(res)