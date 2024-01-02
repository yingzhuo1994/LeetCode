class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        ans = []
        while True:
            maxFreq = max(count.values())
            if maxFreq == 0:
                break
            row = []
            for num, freq in count.items():
                if freq > 0:
                    row.append(num)
                    count[num] -= 1      
            ans.append(row)  
        return ans