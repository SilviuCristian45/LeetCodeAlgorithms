from collections import defaultdict
import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dictS1 = {}
        dictS2 = {}
        dictS1 = defaultdict(lambda:0,dictS1)
        dictS2 = defaultdict(lambda:0,dictS2)
        for c in s1:
            dictS1[c]+=1
        left = 0
        for right in range(len(s2)):
            dictS2[s2[right]] += 1
            if right - left + 1 > len(s1):
                dictS2[s2[left]] -= 1
                left+=1
            #check if dictionaries matches
            doesMatch = True
            if s2[left:right] == "ba":
                print(dictS2)
                print(dictS1)
            #print(string.ascii_lowercase)
            for i in string.ascii_lowercase:
                if dictS1[i] != dictS2[i]:
                    doesMatch = False
            if doesMatch:
                return True
        return False

s = Solution()
res = s.checkInclusion("ab","eidbaooo")
print(res)