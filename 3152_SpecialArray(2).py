# 1st solution
# O(n + k * log(n)) time | (n) space
# where n = len(nums) and k = len(queries)
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        def buildTree(start, end):
            if start == end:
                return Node(start, end, True)
            mid = start + (end - start) // 2
            leftNode = buildTree(start, mid)
            rightNode = buildTree(mid + 1, end)
            valid = (nums[mid] ^ nums[mid + 1]) & 1
            root = Node(start, end, False, leftNode, rightNode)
            if valid and leftNode.value and rightNode.value:
                root.value = True
            return root

        root = buildTree(0, n - 1)

        def query(node, start, end):
            if node.value:
                return True
            if (node.start, node.end) == (start, end):
                return node.value
            mid = node.start + (node.end - node.start) // 2
            if end <= mid:
                return query(node.left, start, end)
            elif start > mid:
                return query(node.right, start, end)
            else:
                valid = (nums[mid] ^ nums[mid + 1]) & 1
                if valid:
                    return query(node.left, start, mid) and query(node.right, mid + 1, end)
                return False

        return [query(root, a, b) for a, b in queries]

class Node:
    def __init__(self, start, end, value, left=None, right=None):
        self.start = start
        self.end = end
        self.value = value
        self.left = left
        self.right = right


# 2nd solution
# O(n + k) time | (n) space
# where n = len(nums)
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        arr = [0] * n
        for i in range(n - 1):
            arr[i] = (nums[i] ^ nums[i + 1]) & 1
        
        preSum = [1]
        for v in arr:
            preSum.append(preSum[-1] + v)
        
        def query(start, end):
            if preSum[end] - preSum[start] == end - start:
                return True
            else:
                return False
        
        return [query(start, end) for start, end in queries]