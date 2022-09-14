from itertools import permutations


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        N = len(candidates)
        result = []
        subset = []
        def bkt(i):
            if i >= N:
                #print(subset)
                val = [candidates[el] for el in subset]
                if sum(val) == target:
                    result.append(val)
                return
            val = [candidates[el] for el in subset]
            if sum(val) > target:
                return
            subset.append(i)
            bkt(i)
            subset.pop()
            bkt(i+1)
        bkt(0)
        return result
s = Solution()
res = s.combinationSum([2,3,6,7], 7)
print(res)