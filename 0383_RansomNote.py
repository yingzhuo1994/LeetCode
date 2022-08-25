# O(m + n) time | O(1) space
# where m, n are the length of ransomNote and magazine, separately
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCount = Counter(ransomNote)
        magazineCount = Counter(magazine)
        for ch in ransomCount:
            if ransomCount[ch] > magazineCount[ch]:
                return False
        return True