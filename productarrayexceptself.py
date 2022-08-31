class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        postfix = []
        answer = []
        p = 1
        for num in nums:
            prefix.append(p*num)
            p *= num
        #print(prefix)
        p = 1 
        for num in nums[::-1]:
            postfix.append(p*num)
            p *= num
        postfix = postfix[::-1]
        #print(postfix)
        for i in range(0, len(nums)):
            left = prefix[i-1] if i > 0 else 1
            right = postfix[i+1] if i < len(nums)-1 else 1
            answer.append(left*right)
        return answer
solution = Solution()
solution.productExceptSelf([-1,1,0,-3,3])