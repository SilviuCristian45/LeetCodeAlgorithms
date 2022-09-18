class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 46
        dp[1] = 1
        dp[2] = 2

        for j in range(3, n+1):
            dp[j] = dp[j-1] + dp[j-2]
        return dp[n]


s = Solution()
res = s.climbStairs(2)
print(res)