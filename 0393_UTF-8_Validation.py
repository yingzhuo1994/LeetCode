# 1st solution
# O(n) time | O(1) space
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            ones = self.getOnes(data[i])
            if ones == 0:
                i += 1
            elif ones == 1:
                return False
            elif ones <= 4:
                for _ in range(ones - 1):
                    i += 1
                    if i < len(data) and self.getOnes(data[i]) == 1:
                        continue
                    else:
                        return False
                i += 1            
            else:
                return False
        return True
    
    def getOnes(self, num):
        count = 0
        k = 7
        while k >= 3:
            d = num >> k
            if d & 1:
                count += 1
            else:
                break
            k -= 1
        return count
