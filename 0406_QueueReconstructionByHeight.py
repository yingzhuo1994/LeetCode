# 1st solution
# O(n*log(n) + n^2) time | O(n) space
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        
        dic = defaultdict(list)
        for h, k in people:
            dic[h].append(k)
        heights = sorted(dic.keys())
        queue = []
        for i in reversed(range(len(heights))):
            h = heights[i]
            queue = self.insert(dic, h, queue)
        
        return queue
    
    def insert(self, dic, h, queue):
        result = []
        i = 0
        j = 0
        while i < len(dic[h]):
            k = dic[h][i]
            if k == len(result):
                result.append([h, k])
                i += 1
            else:
                length = k - len(result)
                result.extend(queue[j:j+length])
                j += length
        result.extend(queue[j:])
        return result

# 2nd solution
# O(n*log(n) + n^2) time | O(n) space
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()

        indices = [i for i in range(len(people))]
        queue = [None for _ in range(len(people))]
        dic = defaultdict(list)
        for h, k in people:
            dic[h].append(k)
        heights = sorted(dic.keys())
        for h in heights:
            for i in range(len(dic[h])):
                idx = dic[h][i] - i
                queue[indices[idx]] = [h, dic[h][i]]
                indices.pop(idx)
        
        return queue