class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        sortedNums = sorted(nums, reverse=True)
        return sortedNums[k-1]

s = Solution()
res = s.findKthLargest([3,2,1,5,6,4], 2)
print(res)