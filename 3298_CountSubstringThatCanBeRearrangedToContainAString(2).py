# 1st solution
# O(n) time | o(k) space
# where n = len(word1), and k = len(word2)
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            return 0

        # t 的字母出现次数与 s 的字母出现次数之差
        diff = defaultdict(int)  # 也可以用 Counter(t)，但是会慢很多
        for c in word2:
            diff[c] += 1

        # 窗口内有 less 个字母的出现次数比 t 的少
        less = len(diff)

        ans = left = 0
        for c in word1:
            diff[c] -= 1
            if diff[c] == 0:
                # c 移入窗口后，窗口内 c 的出现次数和 t 的一样
                less -= 1
            while less == 0:  # 窗口符合要求
                if diff[word1[left]] == 0:
                    # s[left] 移出窗口之前，检查出现次数，
                    # 如果窗口内 s[left] 的出现次数和 t 的一样，
                    # 那么 s[left] 移出窗口后，窗口内 s[left] 的出现次数比 t 的少
                    less += 1
                diff[word1[left]] += 1
                left += 1
            ans += left
        return ans
