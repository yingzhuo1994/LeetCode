# 1st solution
# O(n) time | O(n) space
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        return "".join([word[0] for word in words]) == s
    
# 2nd solution
# O(n) time | O(1) space
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return len(words) == len(s) and all(w[0] == c for w, c in zip(words, s))