from multiprocessing.heap import Arena


class Solution:
    def area(self, l, r, height):
        return (r-l) * min(height[r], height[l])

    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArie = 0

        while left < right:
            currentArea = self.area(left, right, height)
            maxArie = max(maxArie, currentArea)

            if height[left] < height[right]: #inseamna ca stalpul din stanga e mai mic decat cel din dreapta
                left += 1 #shiftam aici ca poate dam de un stalp mai inalt
            else:
                right -=1 #aici e cazul in care e mai mic cel din dreapta sau sunt egale
        
        return maxArie


s = Solution()
res = s.maxArea([1,8,6,2,5,4,8,3,7])
print(res)