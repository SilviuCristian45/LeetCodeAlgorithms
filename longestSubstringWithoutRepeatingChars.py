class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        lenMax = 0
        r = 0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[r])
                r += 1
            window.add(s[i])
            lenMax = max(lenMax, len(window))

        return lenMax


s = Solution()
res = s.lengthOfLongestSubstring("pwwkew")
print(res)