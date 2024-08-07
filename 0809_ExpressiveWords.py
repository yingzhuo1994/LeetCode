# 1st solution
# O(nk) time | O(k) space
# where n = len(words), k is the longest length of words
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_list(word):
            lst = []
            ch = word[0]
            count = 0
            for i in range(len(word)):
                if word[i] == ch:
                    count += 1
                else:
                    lst.append([ch, count])
                    ch = word[i]
                    count = 1
            lst.append([ch, count])
            return lst
        target = get_list(s)
        ans = 0
        for word in words:
            lst = get_list(word)
            if len(lst) != len(target):
                continue
            valid = True
            for p1, p2 in zip(lst, target):
                if p1[0] != p2[0]:
                    valid = False
                    break
                if p1[1] == p2[1] or p1[1] <= p2[1] and p2[1] >= 3:
                    continue
                else:
                    valid = False
                    break
            ans += valid
        return ans