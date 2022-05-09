# O(4^n) time | O(4^n) space
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n < 1:
            return []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', "9": 'wxyz'}

        ans = [""]
        for i in range(n):
            ans = [ch1 + ch2 for ch1 in ans for ch2 in dic[digits[i]]]
        return ans