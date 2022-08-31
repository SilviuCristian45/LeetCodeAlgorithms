class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while True:
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return [left+1, right+1]
            if currentSum > target:
                right -= 1
            else:
                left += 1

s = Solution()
res = s.twoSum([-1, 0], -1)
print(res)