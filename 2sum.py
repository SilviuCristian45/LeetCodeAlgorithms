class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        N = len(nums)
        for i in range(0, N-1):
            for j in range(i+1, N):
                if nums[i] + nums[j] == target:
                    return [i, j]