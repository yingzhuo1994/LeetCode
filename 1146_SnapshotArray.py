# 1st solution
class SnapshotArray:
    # O(n) time | O(n) space
    def __init__(self, length: int):
        self.array = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    # O(1) time | O(1) space
    def set(self, index: int, val: int) -> None:
        if self.array[index][0] == self.snap_id:
            self.array[index][1] = val
        else:
            self.array[index].append([self.snap_id, val])
    
    # O(1) time | O(1) space
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    # O(log(n)) time | O(1) space
    def get(self, index: int, snap_id: int) -> int:
        array = self.array[index]
        left, right = 0, len(array) - 1
        while left <= right:
            mid = left + (right - left) // 2
            id = array[mid][0]
            if id > snap_id:
                right = mid - 1
            else:
                left = mid + 1
        return array[left - 1][1]
    



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
