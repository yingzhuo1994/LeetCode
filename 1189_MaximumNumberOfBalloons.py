class Solution:
    # 1st solution
    # O(n) time | O(1) space
    def maxNumberOfBalloons(self, text: str) -> int:
        dic_text = collections.Counter(text)
        dic_goal = collections.Counter('balloon')
        count = float('inf')
        for k, v in dic_goal.items():
            if k not in dic_text or dic_text[k] < v:
                return 0
            quo = dic_text[k] // v
            count = min(quo, count)
        return count