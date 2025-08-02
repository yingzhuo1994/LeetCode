# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt = Counter()
        res = 0
        for x, y in zip(arr, sorted(arr)):
            cnt[x] += 1
            if cnt[x] == 0:
                del cnt[x]
            cnt[y] -= 1
            if cnt[y] == 0:
                del cnt[y]
            if len(cnt) == 0:
                res += 1
        return res


# 2nd solution
# O(n) time | O(n) space
class Solution:
    def maxChunksToSorted(self, arr: [int]) -> int:
        stack = []
        for num in arr:
            if len(stack) == 0 or num >= stack[-1]:
                stack.append(num)
            else:
                mx = stack.pop()
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(mx)
        return len(stack)