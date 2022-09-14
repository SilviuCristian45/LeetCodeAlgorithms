from collections import defaultdict
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = defaultdict(lambda : 0)
        for task in tasks:
            counter[task] += 1
        notasks = [-task for task in counter.values()]
        heapq.heapify(notasks)
        queue = []
        time = 0
        while notasks or queue:
            time += 1
            if not notasks:
                time = queue[0][1]
            else:
                top = 1 + heapq.heappop(notasks)
                if top:
                    queue.append([top, time + n]) #adaugam top-ul cu task-ul care e oblocat pana la time+n
            if queue:
                if queue[0][1] == time:
                    heapq.heappush(notasks, queue.pop(0)[0])
        return time

s = Solution()
res = s.leastInterval(["A","A","A","B","B","B"], 2)
print(res)