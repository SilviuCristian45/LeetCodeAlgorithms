class Solution:
    def operation(self, left, right, op):
        left = int(left)
        right = int(right)
        if op == "+":
            return left+right
        if op == "-":
            return left-right
        if op == "*":
            return left*right
        if op == "/":
            return left//right

    def evalRPN(self, tokens: list[str]) -> int:
        evalStack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                left = evalStack.pop()
                right = evalStack.pop()
                evalStack.append(self.operation(right, left, token))
            else:
                evalStack.append(token)
            
        return evalStack.pop()
                
                

s = Solution()
res = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"] )
print(res)