from typing import Collection, Counter


class Solution:
    # 1st solution
    # O(km) time | O(1) space
    # m, n are the length of s1 and s2, and k = n - m 
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
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n1 = len(s1)
        n2 = len(s2)
        dict_s1 = Counter(s1)
        dict_s2 = Counter(s2[:n1])
        for i in range(n1, n2 + 1):
            if dict_s1 == dict_s2:
                return True
            if i == n2:
                return False
            dict_s2[s2[i - n1]] -= 1
            if dict_s2[s2[i - n1]] <= 0:
                del dict_s2[s2[i - n1]]
            dict_s2[s2[i]] = dict_s2.get(s2[i], 0) + 1
        return False