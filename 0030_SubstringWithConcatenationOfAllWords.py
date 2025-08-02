# 1st solution
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        L = len(words[0])
        n = len(s)
        if n < L:
            return []
        wordDic = defaultdict(list)
        for i, word in enumerate(words):
            wordDic[word].append(i)

        dp = [[] for _ in range(n)]

        for i in range(n - L + 1):
            word = s[i : i + L]
            if word in wordDic:
                dp[i].extend(wordDic[word])

        ans = []
        for i in range(n):
            visited = [False] * len(words)
            if self.dfs(words, dp, i, visited):
                ans.append(i)
        return ans

    def dfs(self, words, dp, idx, visited):
        k = len(words)
        L = len(words[0])
        if sum(visited) == k:
            return True
        if idx >= len(dp) or len(dp[idx]) == 0:
            return False
        for i in dp[idx]:
            if visited[i]:
                return False
            visited[i] = True
            if self.dfs(words, dp, idx + L, visited):
                return True
            visited[i] = False
        return False


# 2nd solution
# O(n) time | O(n) space
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        L = len(words[0])
        n = len(s)
        if n < L:
            return []
        wordDic = collections.Counter(words)
        dp = ["" for _ in range(n)]

        for i in range(n - L + 1):
            word = s[i : i + L]
            if word in wordDic:
                dp[i] = word
        k = len(words)
        ans = []
        for i in range(L):
            start = i
            end = start + L * (k - 1)
            if end >= n:
                break
            dic = Counter(dp[start:end:L])
            validCount = 0
            for word in dic:
                if word in wordDic and dic[word] >= wordDic[word]:
                    validCount += 1
            while end < n:
                word = dp[end]
                if word != "":
                    dic[word] = dic.get(word, 0) + 1
                    if dic[word] == wordDic[word]:
                        validCount += 1
                if validCount == len(wordDic):
                    ans.append(start)
                word = dp[start]
                if word != "":
                    if dic[word] == wordDic[word]:
                        validCount -= 1
                    dic[word] -= 1
                start += L
                end += L
        return ans