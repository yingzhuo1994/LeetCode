# 1st solution, dfs
# O(n) time | O(n) space
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x_dic = defaultdict(list)
        y_dic = defaultdict(list)
        visited = set()
        for x, y in stones:
            x_dic[x].append(y)
            y_dic[y].append(x)
        
        ans = 0
        for x, y in stones:
            if (x, y) not in visited:
                size = self.dfs(x, y, visited, x_dic, y_dic)
                ans += size - 1
        return ans
    
    def dfs(self, x, y, visited, x_dic, y_dic):
        if (x, y) in visited:
            return 0
        size = 1
        visited.add((x, y))
        for b in x_dic[x]:
            size += self.dfs(x, b, visited, x_dic, y_dic)
        
        for a in y_dic[y]:
            size += self.dfs(a, y, visited, x_dic, y_dic)
        
        return size