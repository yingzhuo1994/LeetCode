class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for x, y in operations:
            half = gem[x] // 2
            gem[y] += half
            gem[x] = gem[x] - half
        
        return max(gem) - min(gem)