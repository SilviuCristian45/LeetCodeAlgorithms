class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        longest = 0

        left = 0
        for right in range(len(s)):
            counter[s[right]] = 1 + counter.get(s[right], 0)
            if right-left+1 - max (counter.values()) <= k: #daca e valid window
                longest = max(longest, right-left+1)
            else: 
                counter[s[left]]-=1
                left+=1
            
        return longest

s = Solution()
res = s.characterReplacement("ABAB", 2)
print(res)