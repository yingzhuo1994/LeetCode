# 1st solution
# O(mn) time | O(1) space
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last = 0
        ans = 0
        for row in bank:
            count = row.count("1")
            if count > 0:
                ans += last * count
                last = count
        return ans