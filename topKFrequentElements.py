import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = []
        lastVal = None
        while k > 0:
            topOfHeap = heapq.heappop(nums)
            if lastVal != topOfHeap:
                res.append(topOfHeap)
                lastVal = topOfHeap
                k -= 1
        return res

s = Solution()
res = s.topKFrequent([1,1,1,2,2,3], 2)
print(res)