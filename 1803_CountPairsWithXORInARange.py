# 1st solution
# O(n) time | O(n) space
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def countLowerXOR(array, x):
            count = Counter(array)
            res = 0
            while x:
                if x & 1:
                    res += sum(count[a] * count[(x - 1) ^ a] for a in count)
                count = Counter({a >> 1: count[a] + count[a ^ 1] for a in count})
                x >>= 1
            return res // 2
        return countLowerXOR(nums, high + 1) - countLowerXOR(nums, low)

# 2nd solution, Trie
# O(n) time | O(n) space
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie()
        ans = 0
        for num in nums: 
            ans += trie.countLower(num, high + 1) - trie.countLower(num, low)
            trie.insert(num)
        return ans 

class Trie: 
    def __init__(self): 
        self.root = {}
        
    def insert(self, val): 
        node = self.root 
        for i in reversed(range(15)):
            bit = (val >> i) & 1
            if bit not in node: node[bit] = {"cnt": 0}
            node = node[bit]
            node["cnt"] += 1
        
    def countLower(self, val, target): 
        ans = 0 
        node = self.root
        for i in reversed(range(15)):
            if not node: break 
            bit = (val >> i) & 1 
            cmp = (target >> i) & 1
            if cmp: 
                if node.get(bit, {}): 
                    ans += node[bit]["cnt"]
                node = node.get(bit ^ 1, {})
            else: 
                node = node.get(bit, {})
        return ans 