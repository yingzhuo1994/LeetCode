# 1st solution, TLE
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        @cache
        def dfs(values, color):
            n = len(values)
            i = 1
            newColor = "B" if color == "A" else "A"
            while i < n - 1:
                if values[i] != color:
                    i += 1
                    continue
                if values[i - 1] == color:
                    if values[i + 1] == color:
                        if not dfs(values[:i] + values[i+1:], newColor):
                            return True
                    while i < n and values[i] == color:
                        i += 1
                else:
                    i += 1
            return False
        
        return dfs(colors, "A")

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        def countContinueColor(target):
            count = 0
            continueColor = 0
            for color in colors:
                if color == target:
                    continueColor += 1
                else:
                    count += max(0, continueColor - 2)
                    continueColor = 0
            count += max(0, continueColor - 2)
            return count
        Alice = countContinueColor("A")
        Bob = countContinueColor("B")

        diff = Alice - Bob
        return diff >= 1
        