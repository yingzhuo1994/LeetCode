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
        ans = 0
        for i in range(31,-1,-1):
            prefixs = set([num>>i for num in nums])
            #to get the first i digits of the num. In the given example [3, 10, 5, 25, 2, 8], 
            #since the largest number 25 is 11001 in binary, thus while i>=5, the prefix = {0}, ignoring all preceding '0'
            #prefix ={0,1} when i ==4, 
            #prefix ={00,01,11} when i ==3, etc.
            
            ans <<=1 # 0 -> 00  1 ->10
            candidate = ans+1 # 0->01 1->11
            #so ans and candidate basically gives two options (0 or 1) on every new digit added
            #and candidate is the largest possible number given the length of the digit. It's sort of a greedy algorithm here.
            #if previous ans == 1, then the new ans and candidate will be 10 and 11
            #depands on if we could get 1 on the new digit, we choose if we move forward with ans(10) or candidate(11)
            
            for pre in prefixs:
                if candidate ^ pre in prefixs:
                    ans = candidate
                    break
            # the if condition pre^candidate in prefix is based on the fact a^b^a = b
            # assume a, b in prefix could generate the largest possilbe xor resuglt "candidate". then if we use candidate^a, the result will be b
            # so if we do find pre^candidate in prefix, candidate will move forward(ans = candidate), meaning we get 1 in the new digit
            
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