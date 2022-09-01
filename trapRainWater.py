class Solution:
    def trap(self, height: list[int]) -> int:
        total = 0
        #build maxLeft
        maxLeft = [0]
        for i in range(1, len(height)):
            newMax = max(height[i-1], maxLeft[i-1])
            maxLeft.append(newMax)
        #build maxright
        maxRight = [0]
        for i in range(len(height)-2, 0, -1):
            newMax = max(height[i+1], maxRight[-1])
            maxRight.append(newMax)
        maxRight.append(max(height[-1], maxRight[-1]))
        maxRight = maxRight[::-1]
        #build solution
        for i,el in enumerate(height):
            waterUnits = (min( maxLeft[i], maxRight[i] ) - el)
            total += (waterUnits if waterUnits > 0 else 0)
        return total
        

s = Solution()
res = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(res)