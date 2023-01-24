class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res
        # binaryN = bin(n)
        # res = 0
        # for char in binaryN[2:]:
        #     if char == "1":
        #         res += 1
        # return res

s = Solution()
res = s.hammingWeight(5)
print(res)