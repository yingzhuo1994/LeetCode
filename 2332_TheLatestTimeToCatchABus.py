# 1st solution
# O(n * log(n) + m * log(m)) time | O(n + m) space
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        def check(array, bus):
            if len(array) == 0 or len(array) < capacity and passengers[array[-1]] != bus:
                return bus
            for i in reversed(array):
                if i > 0:
                    if passengers[i - 1] + 1 != passengers[i]:
                        return passengers[i] - 1
                else:
                    return passengers[i] - 1
            return 1
        n = len(passengers)
        m = len(buses)
        passengers.sort()
        buses.sort()
        q = deque()
        i = 0
        ans = 1
        for bus in buses:
            while i < n and passengers[i] <= bus:
                q.append(i)
                i += 1
            k = 0
            array = []
            while q and k < capacity:
                array.append(q.popleft())
                k += 1
            val = check(array, bus)
            ans = max(ans, val)
        return ans


# 2nd solution
# O(n * log(n) + m * log(m)) time | O(n + m) space
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        # 模拟乘客上车
        j = 0
        for t in buses:
            c = capacity
            while c and j < len(passengers) and passengers[j] <= t:
                j += 1
                c -= 1

        # 寻找插队时机
        j -= 1
        ans = buses[-1] if c else passengers[j]
        while j >= 0 and ans == passengers[j]:  # 往前找没人到达的时刻
            ans -= 1
            j -= 1
        return ans