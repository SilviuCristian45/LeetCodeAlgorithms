class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        setClone = set(nums)
        longest = 0
        for number in nums:
            if (number-1) not in setClone:
                currentLength = 0
                while number+currentLength in setClone:
                    currentLength+=1
                longest = max(currentLength, longest)
        return longest

s = Solution()
result = s.longestConsecutive([100,4,200,1,3,2])
print(result)