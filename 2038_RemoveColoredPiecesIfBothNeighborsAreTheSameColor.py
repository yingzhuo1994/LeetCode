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