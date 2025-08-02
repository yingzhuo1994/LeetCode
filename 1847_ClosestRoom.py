# 1st solution
# O(n * log(n) + q * log(q) + q * log(n)) time | O(n + q) space
from sortedcontainers import SortedList
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda r: r[1])  # 按照 size 从小到大排序
        q = len(queries)
        ans = [-1] * q
        room_ids = SortedList()
        j = len(rooms) - 1
        for i in sorted(range(q), key=lambda i: -queries[i][1]):  # 按照 minSize 从大到小排序
            preferred_id, min_size = queries[i]
            while j >= 0 and rooms[j][1] >= min_size:
                room_ids.add(rooms[j][0])
                j -= 1

            diff = inf
            k = room_ids.bisect_left(preferred_id)
            if k:
                diff = preferred_id - room_ids[k - 1]  # 左边的差
                ans[i] = room_ids[k - 1]
            if k < len(room_ids) and room_ids[k] - preferred_id < diff:  # 右边的差更小
                ans[i] = room_ids[k]
        return ans