class Solution:
    # 1st solution
    # O(n) time | O(n) space
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
            
        signLst = self.getSignList(arr)
        count = 0
        start = 0
        k = 0
        while k < len(signLst):
            if abs(signLst[k]) > 0 and signLst[k] + signLst[k - 1] == 0:
                count = max(count, k - start + 1)
            else:
                start = k
                if signLst[start] != 0:
                    count = max(1, count)
            k += 1
        return count + 1

    def getSignList(self, arr):
        res = []
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                res.append(1)
            elif arr[i] < arr[i + 1]:
                res.append(-1)
            else:
                res.append(0)
        return res