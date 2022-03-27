# 1st solution
# O(mn + m*log(m)) time | O(m) space
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        array = [[sum(row), i] for i, row in enumerate(mat)]
        array.sort()
        return [array[i][1] for i in range(k)]

# 2nd solution
# O(m*log(n) + n) time | O(n) space
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def num_ones(L):
            start, end = 0, n
            while start < end:
                mid = (start + end)//2
                if L[mid] > 0: 
                    start = mid + 1
                else: 
                    end = mid
            return start
        
        m, n = len(mat), len(mat[0])
        buckets = [[] for _ in range(n+1)]
        for i, row in enumerate(mat):
            buckets[num_ones(row)].append(i)
            
        result = []
        for elem in buckets:
            if len(result) >= k:
                break
            result.extend(elem)
        return result[:k]