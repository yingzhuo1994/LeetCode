# 1st solution
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []
        if turnedOn == 0:
            return ["0:00"]
        def getPermutation(lst):
            if len(lst) == 0:
                return []
        
            if len(lst) == 1:
                return [lst]
        
        
            ans = [] # empty list that will store current permutation
        
            # Iterate the input(lst) and calculate the permutation
            for i in range(len(lst)):
                if i > 0 and lst[i] == lst[i-1]:
                    continue
                m = lst[i]
        
                # Extract lst[i] or m from the list.  remLst is
                # remaining list
                remLst = lst[:i] + lst[i+1:]
                # Generating all permutations where m is first
                # element
                for p in getPermutation(remLst):
                    ans.append([m] + p)
            return ans

        def getHour(k):
            left = 4 - k
            lst = [0] * left + [1] * k
            arrays = getPermutation(lst)
            ans = []
            for array in arrays:
                num = sum([array[i] * 2**i for i in range(len(array))])
                if num < 12:
                    ans.append(str(num))
            return ans
        
        def getMinutes(k):
            left = 6 - k
            lst = [0] * left + [1] * k
            arrays = getPermutation(lst)
            ans = []
            for array in arrays:
                num = sum([array[i] * 2**i for i in range(len(array))])
                if num < 60:
                    if num >= 10:
                        ans.append(str(num))
                    else:
                        ans.append("0" + str(num))
            return ans
        
        ans = []
        for h in range(5):
            m = turnedOn - h
            if m < 0 or m > 6:
                continue

            hours = getHour(h)
            minutes = getMinutes(m)
            for a in hours:
                for b in minutes:
                    ans.append(a + ":" + b)
        return ans

# 2nd solution
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == turnedOn:
                    times.append(f'{h}:{m:02d}')
        return times  