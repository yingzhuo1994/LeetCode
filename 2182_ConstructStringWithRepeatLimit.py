# 1st solution
# O(n) time | O(n) space
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        countDic = Counter(s)
        keys = list(countDic.keys())
        keys.sort(reverse=True)

        lst = []
        i = 0
        while i < len(keys):
            if countDic[keys[i]] > repeatLimit:
                lst.append(keys[i] * repeatLimit)
                countDic[keys[i]] -= repeatLimit
                findeNext = False
                for j in range(i + 1, len(keys)):
                    if countDic[keys[j]] > 0:
                        lst.append(keys[j])
                        countDic[keys[j]] -= 1
                        findeNext = True
                        break
                if not findeNext:
                    break
            elif countDic[keys[i]] > 0:
                lst.append(keys[i] * countDic[keys[i]])
                countDic[keys[i]] = 0
                i += 1
            else:
                i += 1
        
        return "".join(lst)