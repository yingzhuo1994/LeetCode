# 1st solution
# O(n) time | O(n) space
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" == target:
            return 0
        visited = set(deadends)
        if "0000" in visited:
            return -1
        current = deque([["0000", 0]])

        while current:
            code, step = current.popleft()
            if code == target:
                return step
            for i in range(len(code)):
                a = (int(code[i]) - 1) % 10
                b = (int(code[i]) + 1) % 10
                new1 = code[:i] + str(a) + code[i+1:]
                new2 = code[:i] + str(b) + code[i+1:]
                for new in [new1, new2]:
                    if new in visited:
                        continue
                    visited.add(new)
                    current.append([new, step + 1])
        return -1