class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def enough(cost):
            k = cars
            for r in ranks:
                n = int(math.sqrt(cost / r))
                k -= n
                if k <= 0:
                    return True
            return False
        
        ranks.sort()
        left = 0
        right = ranks[-1] * cars * cars
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left