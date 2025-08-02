# 1st solution
class NumberContainers:

    def __init__(self):
        self.idx_to_num = {}
        self.num_idx = {}
        
    def change(self, index: int, number: int) -> None:
        self.idx_to_num[index] = number
        if number not in self.num_idx:
            self.num_idx[number] = []
        heappush(self.num_idx[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_idx:
            return -1
        while self.num_idx[number] and self.idx_to_num[self.num_idx[number][0]] != number:
            heappop(self.num_idx[number])
        if len(self.num_idx[number]) > 0:
            return self.num_idx[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)