# 1st solution
# O(n) time | O(n) space
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)
        lst = set()
        for num in dic.keys():
            curIdx = dic[num][0]
            if num - k in dic:
                lastIdx = dic[num - k][-1]
                if lastIdx > curIdx and (num - k, num) not in lst:
                    lst.add((num, num - k))
            if num + k in dic:
                lastIdx = dic[num + k][-1]
                if lastIdx > curIdx and (num + k, num) not in lst:
                    lst.add((num, num + k))
        return len(lst)

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = Counter(nums)
        if k > 0:
            count = sum([num + k in dic for num in dic])
        else:
            count = sum([dic[num] > 1 for num in dic])
        return count