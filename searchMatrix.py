class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #bs on the first column 
        left = 0
        right = len(matrix) - 1
        print(right)

        while left <= right:
            mid = (left + right) // 2
            print(matrix[mid])
            if target in matrix[mid]:
                leftline = 0
                rightline = len(matrix[mid]) - 1

                while leftline <= rightline:
                    midline = (leftline + rightline) // 2
                    if matrix[mid][midline] == target:
                        return True
                    elif target > matrix[mid][midline]:
                        leftline = midline + 1
                    else:
                        rightline = midline - 1
                return False 
            elif target > matrix[mid][0]:
                left = mid + 1
            else:
                right = mid - 1
        return False
                    


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
s = Solution()
res = s.searchMatrix(matrix, 3)
print(res)