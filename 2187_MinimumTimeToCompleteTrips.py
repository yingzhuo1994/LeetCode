# 1st solution
# O(n * log(n)) time | O(n) space 
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        minTime = min(time)
        left = 1
        right = minTime * totalTrips
        time.sort()
        ans = right

        def count_trips(time, cur_time):
            count = 0
            for t in time:
                if t > cur_time:
                    break
                count += cur_time // t
            return count

        while left < right:
            mid = left + (right - left) // 2            
            count = count_trips(time, mid)

            if count >= totalTrips:
                ans = min(ans, mid)
                right = mid
            else:
                left = mid + 1
        return ans