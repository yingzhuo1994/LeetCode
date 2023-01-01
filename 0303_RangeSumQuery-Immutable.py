class NumArray:
    def __init__(self, nums: List[int]):
        self.stack = [0]
        for num in nums:
            val = self.stack[-1] + num
            self.stack.append(val)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.stack[right + 1] - self.stack[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)