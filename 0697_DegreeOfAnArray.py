class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {}
        idxDic = {}
        maxFreq = 0
        for i, num in enumerate(nums):
            dic[num] = dic.get(num, 0) + 1
            if num not in idxDic:
                idxDic[num] = [i, i]
            else:
                idxDic[num][1] = i
            if dic[num] > maxFreq:
                maxFreq = dic[num]
        minLength = len(nums)
        for num, freq in dic.items():
            if freq == maxFreq:
                length = idxDic[num][1] - idxDic[num][0] + 1
                if length < minLength:
                    minLength = length
        return minLength