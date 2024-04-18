# 1st solution
# O(n) time | O(1) space
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        countDic = {5:0, 10:0}
        for bill in bills:
            if bill == 5:
                countDic[5] += 1
            elif bill == 10:
                if countDic[5] == 0:
                    return False
                countDic[5] -= 1
                countDic[10] += 1
            else:
                if countDic[10] >= 1 and countDic[5] >= 1:
                    countDic[10] -= 1
                    countDic[5] -= 1
                elif countDic[5] >= 3:
                    countDic[5] -= 3
                else:
                    return False
        return True

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            elif ten > 0:
                five -= 1
                ten -= 1
            else:
                five -= 3

            if five < 0:
                return False
        return True