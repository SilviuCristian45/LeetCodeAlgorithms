
class Solution:
    def trap(self, height: list[int]) -> int:
        total = 0
        maxL = height[0]
        maxR = height[-1]
        pointerLeft = 0
        pointerRight = len(height)-1

        while pointerLeft < pointerRight:
            if maxL <= maxR :
                pointerLeft += 1  
                waterUnits = maxL - height[pointerLeft] if  maxL - height[pointerLeft] > 0 else 0
                total += waterUnits
                maxL = max(height[pointerLeft], maxL)
            else:
                pointerRight -= 1
                waterUnits = maxR - height[pointerRight] if maxR - height[pointerRight] > 0 else 0
                total += waterUnits
                maxR = max(height[pointerRight], maxR)
        return total
        

s = Solution()
res = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(res)