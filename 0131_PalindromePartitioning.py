# 1st backtracking solution
# O(n * 2^n) time | O(n) space
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s, low, high):
            while low < high:
                if s[low] != s[high]: 
                    return False
                low += 1
                high -= 1
            return True

        def dfs(start, result, currentList, s):
            if start >= len(s):
                # Pay attention to currentList, must use currentList[:]
                result.append(currentList[:])
            end = start
            while end < len(s):
                if (isPalindrome(s, start, end)):
                    #  add current substring in the currentList
                    currentList.append(s[start: end + 1])
                    dfs(end + 1, result, currentList, s)
                    #  backtrack and remove the current substring from currentList
                    currentList.pop()
                end += 1
        
        result = []
        dfs(0, result, [], s)
        return result

# 2nd solution, backtracing with dynamic programming
# O(n * 2^n) time | O(n^2) space
class Solution:
    def partition(self, s: str) -> List[List[str]]:        
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        result = []
        self.dfs(result, s, 0, [], dp)
        return result

    def dfs(self, result, s, start, curLst, dp):
        if start >= len(s):
            result.append(curLst[:])
        end = start
        while end < len(s):
            if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end- 1]):
                dp[start][end] = True
                curLst.append(s[start:end+1])
                self.dfs(result, s, end + 1, curLst, dp)
                curLst.pop()
            end += 1
        
# 3rd solution
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                for rest in self.partition(s[i:]):
                    ret.append([s[:i]]+rest)
        if not ret:
            return [[]]
        return ret