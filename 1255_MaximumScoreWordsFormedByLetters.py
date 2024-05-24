# 1st solution
# O(2^n) time | O(n) space
# where n = len(words)
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        cnt = Counter(letters)
        dic = {}
        for word in words:
            val = sum(score[ord(ch) - ord("a")] for ch in word)
            dic[word] = val

        def dfs(idx, count):
            if idx == len(words):
                return 0
            word = words[idx]
            word_dic = Counter(word)
            for ch in word_dic:
                if count[ch] < word_dic[ch]:
                    return dfs(idx + 1, count)
            ans = dfs(idx + 1, count)
            for ch in word_dic:
                count[ch] -= word_dic[ch]
            ans = max(ans, dic[word] + dfs(idx + 1, count))
            for ch in word_dic:
                count[ch] += word_dic[ch]
            return ans
        return dfs(0, cnt)

