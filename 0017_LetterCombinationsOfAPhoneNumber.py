class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # O(4^n) time | O(4^n) space
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', "9": 'wxyz'}
        n = len(digits)
        if n < 1:
            return []
        lst = [ch for ch in dic[digits[0]]]
        for i in range(1, n):
            new = [ch for ch in dic[digits[i]]]
            lst = [ch1 + ch2 for ch1 in lst for ch2 in new]
        return lst
