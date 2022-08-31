def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i,n in enumerate(nums):
        if i > 0 and n == nums[i-1]:
            continue
        a = n
        #solve 2sum2
        left = i + 1
        right = len(nums) - 1

        while left < right:
            currentSum = a + nums[left] + nums[right]
            if currentSum == 0:
                result.append( [a, nums[left], nums[right]] )
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
            elif currentSum > 0:
                right -= 1  
            else:
                left += 1
    return result


res = threeSum([-1,0,1,2,-1,-4])
print(res)