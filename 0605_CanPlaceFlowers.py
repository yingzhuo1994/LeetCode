# 1st solution
# O(n) time | O(1) space
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed.append(0)
        for i in range(len(flowerbed) - 1):
            if flowerbed[i] == 0:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    if n <= 0:
                        return True
        return False