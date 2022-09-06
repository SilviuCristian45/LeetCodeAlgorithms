class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []
        for p, s in pairs:
            stack.append( (target-p) / s) #punem in stiva timpul curent
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #daca sunt cel putin 2 el in stiva si cel din varf e mai mic decat ala de sub el
                stack.pop()

        return len(stack)

s = Solution()
res = s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])
print(res)