from typing import Collection, Counter


class Solution:
    # 1st solution
    # O(km) time | O(m) space
    # m, n are the length of s1 and s2, and k = n - m 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n1 = len(s1)
        n2 = len(s2)
        dict_s1 = Counter(s1)
        
        for i in range(n2 - n1 + 1):
            dict_test = Counter(s2[i:n1 + i])
            check = True
            for k, v in dict_s1.items():
                if k not in dict_test or dict_test[k] != v:
                    check = False
                    break
            if check:
                return True
        return False
            

