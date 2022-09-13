import heapq
from multiprocessing import heap


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        #mapez distantele la puncte - distance
        #fac un heap de distante
        #pop pana cand k e 0 si fac append la result valoarea . cheia e distanta 
        map = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            map.append([distance, point[0], point[1]])

        heapq.heapify(map)
        result = []
        while k > 0:
            k -=  1
            minDistance,x,y = heapq.heappop(map)
            result.append([x,y])
        return result

s = Solution()
res = s.kClosest([[3,3],[5,-1],[-2,4]], 2)
print(res)