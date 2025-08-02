# 1st solution
# O(n) time | O(n) space
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        lst = text.split()
        ans = []
        for i in range(len(lst) - 2):
            if lst[i] == first and lst[i + 1] == second:
                ans.append(lst[i + 2])
        return ans