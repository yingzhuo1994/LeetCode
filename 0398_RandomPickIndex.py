# 1st solution
class Solution:
    def __init__(self, nums: List[int]):
        self.stack = nums[:]
        self.dic = {}
        for i, num in enumerate(self.stack):
            if num not in self.dic:
                self.dic[num] = []
            self.dic[num].append(i)
        
    def pick(self, target: int) -> int:
        return random.choice(self.dic[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)