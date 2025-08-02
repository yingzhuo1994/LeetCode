# 1st solution
# O(n + L) time | O(n) space
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        ans = 0
        has_key = status  # 把开着的盒子当作有钥匙
        has_box = [False] * len(status)
        for x in initialBoxes:
            has_box[x] = True

        def dfs(x: int) -> None:
            nonlocal ans
            ans += candies[x]
            has_box[x] = False  # 避免找到钥匙后重新访问开着的盒子

            # 找到钥匙，打开盒子（说明我们先找到盒子，然后找到钥匙）
            for y in keys[x]:
                has_key[y] = True
                if has_box[y]:
                    dfs(y)

            # 找到盒子，使用钥匙（说明我们先找到钥匙，然后找到盒子）
            for y in containedBoxes[x]:
                has_box[y] = True
                if has_key[y]:
                    dfs(y)

        for x in initialBoxes:
            if has_key[x] and has_box[x]:  # 注意 dfs 中会修改 has_box
                dfs(x)
        return ans