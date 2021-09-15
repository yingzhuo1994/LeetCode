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

    # 2nd solution
    # O(n) time | O(1) space
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
            
        lastState = self.getState(arr, 0, 1)
        count = 0
        start = 0
        k = 1
        
        while k < len(arr):
            curState = self.getState(arr, k - 1, k)
            if curState == 0:
                start = k + 1
            elif curState + lastState != 0:
                start = k
            count = max(count, k - start + 1)
            lastState = curState
            k += 1
        return count + 1

    def getState(self, arr, i, j):
        if arr[i] > arr[j]:
            return 1
        elif arr[i] < arr[j]:
            return -1
        else:
            return 0