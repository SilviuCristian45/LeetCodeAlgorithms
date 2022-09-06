class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        #brute force
        # res = []
        # for i in range(0, len(temperatures)):
        #     days = 0
        #     ok = 0
        #     for j in range(i, len(temperatures)):
        #         print(temperatures[i], temperatures[j], i , j)
        #         if temperatures[j] > temperatures[i]:
        #             ok = 1
        #             break
        #         days += 1
        #     if ok == 0:
        #         res.append(0)
        #     else:
        #         res.append(days)
        # return res
        res = [0] * len(temperatures)
        stack = []
        for i in range(0, len(temperatures)):
            temp = temperatures[i] #store the current temperature
            while len(stack) > 0 and stack[-1][0] < temp: #while the top element of stack is smaller than the current Temperature
                poppedElementIndex = stack[-1][1] #store the topElement index
                res[poppedElementIndex] = i - poppedElementIndex
                stack.pop()
            stack.append((temp, i))
        return res

        
s = Solution()
res = s.dailyTemperatures([73,74,75,71,69,72,76,73])
print(res)