class Solution:
    # 1st solution
    # O(2^n) time | O(n) space
    def maxLength(self, arr: List[str]) -> int:
        ans = [0]
        path = ''
        self.dfs(arr, path, ans)
        return ans[0]
    
    def dfs(self, arr, path, ans):
        dic = Counter(path)
        for k, v in dic.items():
            if v > 1:
                return 
        ans[0] = max(ans[0], len(path))
        
        if ans[0] == 26 or len(arr) == 0:
            return 
        
        for i in range(len(arr)):
            self.dfs(arr[i + 1:], path + arr[i], ans)