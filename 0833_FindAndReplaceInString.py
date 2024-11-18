# 1st solution
# O(n + k * log(k)) time | O(n + k) space
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        tasks = list(zip(indices, sources, targets))
        tasks.sort()
        ans = []
        i = 0
        j = 0
        while i < len(s) and j < len(tasks):
            idx, source, target = tasks[j]
            if idx < i:
                j += 1
            elif idx > i:
                ans.append(s[i])
                i += 1
            else:
                k = len(source)
                if idx + k <= len(s) and s[idx:idx+k] == source:
                    ans.append(target)
                    i += k
                j += 1

        ans.append(s[i:])
        return "".join(ans)
            