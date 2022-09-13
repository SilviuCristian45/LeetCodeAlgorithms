class KthLargest:

    k: int
    nums: list[int]

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse=True)
        return self.nums[self.k - 1]
        


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
x = param_1 = obj.add(3)
print(x)
x = obj.add(5);
print(x)