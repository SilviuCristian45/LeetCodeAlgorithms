class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A,B = B,A
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        #binary search on A
        while True:
            middle = (l+r) // 2
            secondPart = half - middle - 2

            #verificam daca e corecta partitionarea
            Aleft = A[middle] if middle >= 0 else float("-infinity")
            Aright = A[middle+1] if middle + 1 < len(A) else float("+infinity")
            Bleft = B[secondPart] if secondPart >= 0 else float("-infinity")
            Bright = B[secondPart+1] if secondPart + 1 < len(B) else float("+infinity")

            if Aleft <= Bright and Bleft <= Aright:
                #odd number of elements
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright) ) / 2
                else:
                    return  min(Bright, Aright)
            elif Aleft > Bright:
                r = middle - 1
            else:
                l = middle + 1

         

solution = Solution()
result = solution.findMedianSortedArrays([0, 0], [0, 0])
print(result)