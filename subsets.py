class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        result = []
        subset = []
        def bkt(i):
            if i >= N:
                print(subset)
                result.append(subset[:])
                return
            #include nums[i]
            subset.append(nums[i])
            bkt(i+1)
            #not include nums[i]
            subset.pop()
            subset.append(nums[i-1])
            bkt(i)
            subset.pop()
        bkt(0)
        return result
s = Solution()
res = s.subsets([1,2,3])
print(res)