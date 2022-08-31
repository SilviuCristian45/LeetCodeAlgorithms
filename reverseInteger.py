
class Solution:
    def reverse(self, x: int) -> int:
        isPositive = (x > 0)
        if not isPositive:
            x = x*-1
        inverse = 0
        while x > 0:
            inverse = inverse*10 + x%10
            x //= 10
        if not isPositive:
            inverse *= -1
        if inverse < -2**31 or inverse > 2**31:
            return 0



s = Solution()
s.reverse(341)