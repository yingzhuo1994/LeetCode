# 1st solution, TLE
# O(kn) time | O(kn) space
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        dp = [[0, 0] for _ in range(n + 1)]
        for i in range(n):
            if answerKey[i] == "T":
                dp[i+1][0] = dp[i][0] + 1
                dp[i+1][1] = dp[i][1]
            else:
                dp[i+1][0] = dp[i][0]
                dp[i+1][1] = dp[i][1] + 1

        @cache
        def dfs(idx, left_k, target):
            if idx < 0:
                return 0, 0
            if target == "T":
                if dp[i + 1][1] <= left_k:
                    return i + 1, i + 1
            else:
                if dp[i + 1][0] <= left_k:
                    return i + 1, i + 1
            ans = 0
            ans_last = 0
            if answerKey[idx] == target:
                total, last = dfs(idx - 1, left_k, target)
                ans = max(ans, total)
                ans_last = max(ans_last, last + 1)
            else:
                if left_k > 0:
                    total, last = dfs(idx - 1, left_k - 1, target)
                    ans = max(ans, total)
                    ans_last = max(ans_last, last + 1)
                total, last = dfs(idx - 1, left_k, target)
                ans = max(ans, total)
                ans_last = max(ans_last, 0)
            ans = max(ans, ans_last)
            # print(idx, left_k, target, ":", ans, ans_last)
            return ans, ans_last
        
        T, _ = dfs(n - 1, k, "T")
        F, _ = dfs(n - 1, k, "F")
        return max(T, F)

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        s = answerKey
        maxf = res = 0
        count = collections.Counter()
        for i in range(len(s)):
            count[s[i]] += 1
            maxf = max(maxf, count[s[i]])
            if res - maxf < k:
                res += 1
            else:
                count[s[i - res]] -= 1
        return res