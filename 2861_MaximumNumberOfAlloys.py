# 1st solution
# O(kn * log(U)) time | O(1) space
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def check(num, comp):
            money = 0
            for s, base, c in zip(stock, comp, cost):
                if s < base * num:
                    money += (base * num - s) * c
                    if money > budget:
                        return False
            return True
        
        ans = 0
        mx = min(stock) + budget
        for comp in composition:

            left, right = ans, mx + 1
            while left + 1 < right:  # 开区间写法
                mid = (left + right) // 2
                if check(mid, comp):
                    left = mid
                else:
                    right = mid
            ans = left
        
        return ans