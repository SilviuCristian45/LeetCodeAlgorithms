class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]: #daca suntem in left portion
                if target < nums[left] or target > nums[mid]: #daca e mai mic target-ul decat left-ul, atunci cautam in dreapta
                    left = mid + 1
                else: #daca e mai mare atunci cautam aici intre left si mid
                    right = mid - 1
            else: #right portion
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

s = Solution()
res = s.search([4,5,6,7,0,1,2], 0)
print(res)