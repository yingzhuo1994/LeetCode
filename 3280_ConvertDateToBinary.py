# 1st solution
# O(n) time | O(n) space
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        lst = date.split("-")
        return "-".join([bin(int(s))[2:] for s in lst])