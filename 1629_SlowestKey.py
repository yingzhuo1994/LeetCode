class Solution:
    # O(n) time | O(1) space
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ch = keysPressed[0]
        time = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            deltaTime = releaseTimes[i] - releaseTimes[i - 1]
            if deltaTime > time:
                ch = keysPressed[i]
                time = deltaTime
            elif deltaTime == time:
                ch = max(ch, keysPressed[i])
        return ch