class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
    def canJumpBrute(self, nums: list[int]) -> bool:
        memo = [0] * len(nums)

        def helper(step: int):
            if memo[step] != 0:
                return memo[step]
            if step == len(nums) - 1:
                return True
            if nums[step] == 0:
                return False
            res = False
            for s in range(1, nums[step]+1):
                newPos = step + s
                res = res or helper(newPos)
            memo[step] = res
            return memo[step]

        return helper(0)

s = Solution()
res = s.canJumpBrute([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]) 
print(res)