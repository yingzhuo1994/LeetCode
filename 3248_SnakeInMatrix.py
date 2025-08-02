# 1st solution
# O(k) time | O(1) space
# where k = len(commands)
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        actions = {"UP": [-1, 0], "DOWN": [1, 0], "RIGHT": [0, 1], "LEFT": [0, -1]}
        i, j = 0, 0
        cnt = Counter(commands)

        for command in cnt:
            dx, dy = actions[command]
            i += dx * cnt[command]
            j += dy * cnt[command]
        return i * n + j