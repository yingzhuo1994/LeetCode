# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array
        
    def shuffle(self) -> List[int]:
        aux = list(self.array)

        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)
        return self.array

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array
        
    def shuffle(self) -> List[int]:
        for idx in range(len(self.array)):
            swap_idx = random.randrange(idx, len(self.array))
            self.array[idx], self.array[swap_idx] = self.array[swap_idx], self.array[idx]
        return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()