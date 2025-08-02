# 1st solution
# O(n) time | O(n) space
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        path = []
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if path:
                    path.pop()
            else:
                path.append(log)
        return len(path)