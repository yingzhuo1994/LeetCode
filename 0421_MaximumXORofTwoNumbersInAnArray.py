# 1st solution, brute-force
# O(n^2) time | O(1) space
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        largest = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                x = nums[i] ^ nums[j]
                largest = max(largest, x)
        return largest

# 2nd solution, mask
# O(32n) time | O(n) space
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans, mask = 0, 0
        for i in reversed(range(32)):
            mask |= 1<<i
            found = set([num & mask for num in nums])
                
            start = ans | 1<<i
            for pref in found:
                if start^pref in found:
                    ans = start
                    break
         
        return ans

# 3rd solution, Trie
# O(32n) time | O(n) space
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        for num in nums:
            node = root
            for j in reversed(range(32)):
                tmp = num & 1 << j
                if tmp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero
                    
        ans = 0
        for num in nums:
            node = root
            tmp_val = 0
            for j in reversed(range(32)):
                tmp = num & 1 << j
                if node.one and node.zero:
                    if tmp:
                        node = node.zero
                    else:
                        node = node.one
                    tmp_val += 1 << j
                else:
                    if (node.zero and tmp) or (node.one and not tmp):
                        tmp_val += 1 << j
                    node = node.one or node.zero
            ans = max(ans, tmp_val)
                                                
        return ans

class TrieNode():
    def __init__(self):
        self.one = None
        self.zero = None