# 1st solution
# O(6^n) time | O(6^n) space
# where n = len(bottom)
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowedDic = {}
        for s in allowed:
            if s[:2] not in allowedDic:
                allowedDic[s[:2]] = []
            allowedDic[s[:2]].append(s[2])
        
        def buildTop(row):
            lst = []
            for i in range(len(row) - 1):
                key = row[i:i+2]
                if key not in allowedDic:
                    return []
                if not lst:
                    lst = allowedDic[key][:]
                else:
                    lst = [s + ch for s in lst for ch in allowedDic[key]]
            return lst
        
        level = [bottom]
        while level:
            newLevel = set()
            for row in level:
                if len(row) == 1:
                    return True
                lst = buildTop(row)
                for new in lst:
                    newLevel.add(new)
            level = newLevel
        return False
