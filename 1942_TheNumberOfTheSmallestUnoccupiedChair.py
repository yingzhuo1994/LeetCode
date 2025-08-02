# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        seq = []
        for i, (t1, t2) in enumerate(times):
            seq.append([t1, 1, i])
            seq.append([t2, -1, i])
        seq.sort()

        dic = {}
        n = len(times)
        minStack = [i for i in range(n)]
        for t, action, idx in seq:
            if action == 1:
                dic[idx] = heappop(minStack)
                if idx == targetFriend:
                    return dic[idx]
            else:
                heappush(minStack, dic[idx])
                del dic[idx]