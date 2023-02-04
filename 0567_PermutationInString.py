# 1st solution
# O(km) time | O(1) space
# m, n are the length of s1 and s2, and k = n - m 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n1 = len(s1)
        n2 = len(s2)
        dict_s1 = Counter(s1)
        
        for i in range(n2 - n1 + 1):
            dict_test = Counter(s2[i:n1 + i])
            if dict_s1 == dict_test:
                return True
        return False
            
# 2nd solution, moving window
# O(km) time | O(1) space
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        dict_s1 = Counter(s1)
        dict_s2 = Counter(s2[:n1])
        if dict_s1 == dict_s2:
            return True
        for i in range(n1, n2):
            dict_s2[s2[i - n1]] -= 1
            if dict_s2[s2[i - n1]] <= 0:
                dict_s2.pop(s2[i - n1])
            dict_s2[s2[i]] = dict_s2.get(s2[i], 0) + 1
            if dict_s1 == dict_s2:
                return True
        return False

# 3rd solution, moving window
# O(n) time | O(1) space
# n = len(s2)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        count_s1 = Counter(s1)
        unique = len(count_s1)

        valid = 0
        dic = Counter()
        start = 0
        for i in range(n2):
            ch = s2[i]
            dic[ch] += 1
            if dic[ch] == count_s1[ch]:
                valid += 1
            while i - start + 1 > n1:
                ch = s2[start]
                if dic[ch] == count_s1[ch]:
                    valid -= 1
                dic[ch] -= 1
                start += 1
            if valid == unique:
                return True

        return False