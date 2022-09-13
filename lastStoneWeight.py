import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        negativeStones = [-x for x in stones]
        heapq.heapify(negativeStones)

        while len(negativeStones) > 1:
            x = heapq.heappop(negativeStones)
            y = heapq.heappop(negativeStones)

            if x != y:
                heapq.heappush(negativeStones, x - y)
        negativeStones.append(0)
        return abs(negativeStones[0])

s = Solution()
res = s.lastStoneWeight([2,7,4,1,8,1])
print(res)