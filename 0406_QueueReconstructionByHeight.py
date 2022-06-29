# 1st solution
# O(n*log(n) + n^2) time | O(n) space
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        
        queue = []
        for h, k in people:
            queue.insert(k, [h, k])
        return queue