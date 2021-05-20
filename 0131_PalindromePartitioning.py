class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # def isPalindrome(s, low, high):
        #     while low < high:
        #         if s[low] != s[high]: 
        #             return False
        #         low += 1
        #         high -= 1
        #     return True

        # def dfs(start, result, currentList, s):
        #     if start >= len(s):
        #         result.append(currentList)
        #     end = start
        #     while end < len(s):
        #         if (isPalindrome(s, start, end)):
        #             #  add current substring in the currentList
        #             currentList.append(s[start: end + 1])
        #             dfs(end + 1, result, currentList, s)
        #             #  backtrack and remove the current substring from currentList
        #             currentList.pop()
        #         end += 1
        
        # result = []
        # dfs(0, result, [], s)
        # return result
        
        ret = []
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                for rest in self.partition(s[i:]):
                    ret.append([s[:i]]+rest)
        if not ret:
            return [[]]
        return ret


