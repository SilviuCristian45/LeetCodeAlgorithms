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
    def jump(self, nums: list[int]) -> int:
        currentLevel = 0
        for i in range(0, len(nums)):
            print(i)
            currentLevel += 1
            step = i+1
            while step < len(nums) and step <= i + nums[i]:
                step += 1
            i = step
        return currentLevel

# 0 1 2 3 4
# 2 3 1 1 4
#level 1 
#step 3
#i 0
s = Solution()
res = s.jump([2,3,1,1,4]) 
print(res)