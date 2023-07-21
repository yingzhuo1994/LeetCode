# 1st solution
# O(n^2) time | O(n) space 
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = [dp[j][0] + 1, dp[j][1]]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
        
        dic = {}
        for length, count in dp:
            dic[length] = dic.get(length, 0) + count
        
        maxLnegth = max(dic.keys())
        return dic[maxLnegth]

# 2nd solution
# O(n * log(n)) time | O(n) space 
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        decks, ends_decks, paths = [], [], []
        for num in nums:
            deck_idx = bisect.bisect_left(ends_decks, num)
            n_paths = 1
            if deck_idx > 0:
                l = bisect.bisect(decks[deck_idx-1], -num)
                n_paths = paths[deck_idx-1][-1] - paths[deck_idx-1][l]
                
            if deck_idx == len(decks):
                decks.append([-num])
                ends_decks.append(num)
                paths.append([0, n_paths])
            else:
                decks[deck_idx].append(-num)
                ends_decks[deck_idx] = num
                paths[deck_idx].append(n_paths + paths[deck_idx][-1])
              
        return paths[-1][-1]