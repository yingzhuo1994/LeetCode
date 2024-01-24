# 1st solution
# O(n) time | O(n) space
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def get_dp(start, end, dir):
            k = abs(end - start)
            dp = [0] * k
            st = [start - 1 if dir > 0 else start + 1]  # 哨兵
            s = 0
            for i in range(start, end, dir):
                x = maxHeights[i]
                while len(st) > 1 and x <= maxHeights[st[-1]]:
                    j = st.pop()
                    s -= maxHeights[j] * abs(st[-1] - j)  # 撤销之前加到 s 中的
                s += x * abs(st[-1] - i)  # 从 i 到 st[-1]-1 都是 x
                dp[i] = s
                st.append(i)
            return dp
        
        n = len(maxHeights)
        leftDp = get_dp(0, n, 1)
        rightDp = get_dp(n - 1, -1, -1)
        ans = 0

        for i in range(n):
            ans = max(ans, leftDp[i] + rightDp[i] - maxHeights[i])
        
        return ans