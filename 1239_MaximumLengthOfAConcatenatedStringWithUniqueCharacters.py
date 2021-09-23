class Solution:
    # 1st solution
    # O(2^n) time | O(n) space
    def maxLength(self, arr: List[str]) -> int:
        ans = [0]
        path = ''
        self.dfs(arr, 0, path, ans)
        return ans[0]
    
    def dfs(self, arr, idx, path, ans):
        dic = Counter(path)
        for k, v in dic.items():
            if v > 1:
                return 
        ans[0] = max(ans[0], len(path))
        
        if ans[0] == 26 or idx == len(arr):
            return 
        
        for i in range(idx, len(arr)):
            self.dfs(arr, i + 1, path + arr[i], ans)