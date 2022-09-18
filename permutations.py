

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        subset = [0] * 7
        res = []
        def cont(i):
            for k in range(0, i):
                if subset[k] == subset[i]:
                    return False
            return True

        def bkt(i):
            for j in range(0, N):
                subset[i] = j
                if cont(i):
                    if i == N-1:
                        res.append([nums[x] for x in subset[0:N] ])
                    else:
                        bkt(i+1)
        bkt(0)
        return res
        # N = len(nums)
        # result = []
        # from itertools import permutations
        # indexes = list(permutations(range(0, N)))
        # for index in indexes:
        #     solution = [nums[i] for i in index]
        #     result.append(solution)
        # return result


s = Solution()
res = s.permute([1,2,3])
print(res)