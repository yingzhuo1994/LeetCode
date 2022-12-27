# 1st solution
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        dic1 = {num: [] for num in range(10)}
        dic2 = {num: [] for num in range(10)}
        for i, num in enumerate(nums1):
            dic1[num].append(i)
        
        for i, num in enumerate(nums2):
            dic2[num].append(i)
        
        def getMaxList(lst, dic, length):
            array = []
            count = 0
            start = 0
            while count < length:
                for num in reversed(range(10)):
                    i = bisect.bisect_left(dic[num], start)
                    if  i < len(dic[num]) and count + len(lst) - dic[num][i] >= length:
                        array.append(num)
                        start = dic[num][i] + 1
                        count += 1
                        break
            return array
        
        def merge(lst1, lst2):
            array = []
            i, j = 0, 0
            while i < len(lst1) and j < len(lst2):
                if lst1[i] > lst2[j]:
                    array.append(lst1[i])
                    i += 1
                elif lst1[i] < lst2[j]:
                    array.append(lst2[j])
                    j += 1
                else:
                    a = i + 1
                    b = j + 1
                    while a < len(lst1) and b < len(lst2):
                        if lst1[a] > lst2[b]:
                            array.append(lst1[i])
                            i += 1
                            break
                        elif lst1[a] < lst2[b]:
                            array.append(lst2[j])
                            j += 1
                            break
                        a += 1
                        b += 1
                    if a >= len(lst1):
                        array.append(lst2[j])
                        j += 1
                    elif b >= len(lst2):
                        array.append(lst1[i])
                        i += 1
            array.extend(lst1[i:] or lst2[j:])
            return array

        def compare(lst1, lst2):
            for i in range(len(lst1)):
                if lst1[i] > lst2[i]:
                    return 1
                elif lst1[i] < lst2[i]:
                    return -1
            return 0 

        ans = [0 for _ in range(k)]
        for a in range(max(k - n, 0), min(m, k) + 1):
            b = k - a
            lst1 = getMaxList(nums1, dic1, a)
            lst2 = getMaxList(nums2, dic2, b)
            lst = merge(lst1, lst2)
            if compare(lst, ans) > 0:
                ans = lst
        return ans

# 2nd solution
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        dic1 = {num: [] for num in range(10)}
        dic2 = {num: [] for num in range(10)}
        for i, num in enumerate(nums1):
            dic1[num].append(i)
        
        for i, num in enumerate(nums2):
            dic2[num].append(i)
        
        def getMaxList(lst, dic, length):
            array = []
            count = 0
            start = 0
            while count < length:
                for num in reversed(range(10)):
                    i = bisect.bisect_left(dic[num], start)
                    if  i < len(dic[num]) and count + len(lst) - dic[num][i] >= length:
                        array.append(num)
                        start = dic[num][i] + 1
                        count += 1
                        break
            return array

        def merge(lst1, lst2):
            array = []
            i, j = 0, 0
            while len(array) < len(lst1) + len(lst2):
                if larger(lst1, lst2, i, j):
                    array.append(lst1[i])
                    i += 1
                else:
                    array.append(lst2[j])
                    j += 1
            return array

        def larger(lst1, lst2, i=0, j=0):
            while i < len(lst1) and j < len(lst2) and lst1[i] == lst2[j]:
                i += 1
                j += 1
            return j == len(lst2) or i < len(lst1) and lst1[i] > lst2[j]

        ans = [0 for _ in range(k)]
        for a in range(max(k - n, 0), min(m, k) + 1):
            b = k - a
            lst1 = getMaxList(nums1, dic1, a)
            lst2 = getMaxList(nums2, dic2, b)
            lst = merge(lst1, lst2)
            if larger(lst, ans):
                ans = lst
        return ans