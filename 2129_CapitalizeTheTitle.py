# 1st solution
# O(n) time | O(n) space
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        lst = title.split()
        for i, word in enumerate(lst):
            lst[i] = word.lower()
            if len(word) > 2:
                lst[i] = lst[i].capitalize()
        return " ".join(lst)
        