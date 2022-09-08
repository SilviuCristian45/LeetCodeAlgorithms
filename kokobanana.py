from turtle import speed
import math

class Solution:
    def minEatingSpeed2(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        for speed in range(left, right+1):
            totalTime = 0
            for pile in piles:
                totalTime += pile/speed
            if totalTime <= h:
                return speed
        return 0
    def minEatingSpeed(self, piles: list[int], h: int) -> int: 
        left = 1
        right = max(piles)
        k = 0
        while left <= right:
            mid = (left + right) // 2
            totalTime = 0
            for pile in piles:
                fractPart, integerPart = math.modf(pile/mid)
                if fractPart >= 0.5:
                    integerPart += 1
                totalTime += integerPart
            if totalTime <= h:
                k = mid
                right = mid-1
            else:
                left = mid+1
        return k


s = Solution()
res = s.minEatingSpeed([30,11,23,4,20], 5)
print(res)