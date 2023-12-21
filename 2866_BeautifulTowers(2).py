# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def help(idx):
            maxHeight = maxHeights[idx]
            ans = maxHeight
            leftMax = maxHeight
            for i in reversed(range(idx)):
                leftMax = min(leftMax, maxHeights[i])
                ans += leftMax
            rightMax = maxHeight
            for i in range(idx + 1, n):
                rightMax = min(rightMax, maxHeights[i])
                ans += rightMax
            return ans
        
        n = len(maxHeights)
        ans = 0
        for i in range(n):
            ans = max(ans, help(i))
        return ans
        
# 2nd solution
# O(n) time | O(n) space
class Solution:
    def maximumSumOfHeights(self, a: List[int]) -> int:
        n = len(a)
        suf = [0] * (n + 1)
        st = [n]  # 哨兵
        s = 0
        for i in range(n - 1, -1, -1):
            x = a[i]
            while len(st) > 1 and x <= a[st[-1]]:
                j = st.pop()
                s -= a[j] * (st[-1] - j)  # 撤销之前加到 s 中的
            s += x * (st[-1] - i)  # 从 i 到 st[-1]-1 都是 x
            suf[i] = s
            st.append(i)

        ans = s
        st = [-1]  # 哨兵
        pre = 0
        for i, x in enumerate(a):
            while len(st) > 1 and x <= a[st[-1]]:
                j = st.pop()
                pre -= a[j] * (j - st[-1])  # 撤销之前加到 pre 中的
            pre += x * (i - st[-1])  # 从 st[-1]+1 到 i 都是 x
            ans = max(ans, pre + suf[i + 1])
            st.append(i)
        return ans