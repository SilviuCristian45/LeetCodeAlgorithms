class Solution:
    def sortString(self, inputString):
        return ''.join(sorted(inputString))

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = {}
        for str in strs:
            sortedStr = self.sortString(str)
            if sortedStr not in hashMap:
                hashMap[sortedStr] = []
            hashMap[sortedStr].append(str)
        return hashMap.values()

s = Solution()
result = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)