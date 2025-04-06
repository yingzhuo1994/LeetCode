# 1st solution
# O(1) time | O(1) space
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        def permutation(lst):
            if len(lst) == 1:
                return [lst]
            ans = []
            for i in range(len(lst)):
                temp = permutation(lst[:i]+lst[i+1:])
                ans.extend([[lst[i]] + t for t in temp])
            
            return ans
        
        def isValidTime(lst):
            if lst[0] > 2:
                return False
            if lst[0] == 2:
                if lst[1] > 3:
                    return False
            if lst[2] > 5:
                return False
            return True
        
        lsts = permutation(arr)
        ans = ""
        for lst in lsts:
            if isValidTime(lst):
                if not ans:
                    ans = lst
                else:
                    for a, b in zip(lst, ans):
                        if a < b:
                            break
                        elif a > b:
                            ans = lst

        if not ans:
            return ans
        
        return f"{ans[0]}{ans[1]}:{ans[2]}{ans[3]}"