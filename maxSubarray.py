class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(curSum, maxSub)
        return maxSub
    def maxSubArray1(self, nums: list[int]) -> int:
        def cross(nums, left, mid, right):
            left_max, right_max = float("-inf"), float("-inf")
            left_sum, right_sum = 0, 0
            for i in range(mid, left-1, -1):
                left_sum += nums[i]
                if left_sum > left_max:
                    left_max = left_sum
            
            for i in range(mid+1, right+1):
                right_sum += nums[i]
                if right_sum > right_max:
                    right_max = right_sum
            
            return left_max + right_max

        def solution(nums, left, right):
            if left > right:
                return 0
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            L = solution(nums, left, mid)
            R = solution(nums, mid+1, right)
            C = cross(nums, left, mid, right)
            return max(L, R, C)
        
        return solution(nums, 0, len(nums) -1 )

s = Solution()
res = s.maxSubArray1([-2,1,-3,4,-1,2,1,-5,4])
print(res)