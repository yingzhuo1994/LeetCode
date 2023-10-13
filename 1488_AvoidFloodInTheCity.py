# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [0 for _ in range(n)]
        floods = []
        dic = {}
        for day, rain in enumerate(rains):
            if rain == 0:
                continue
            dic[rain] = dic.get(rain, 0) + 1
            if dic[rain] > 1:
                floods.append([day, rain])
        
        lakes = set()
        for day, rain in enumerate(rains):
            if rain == 0:
                ans[day] = 1
                if floods:
                    for i in range(len(floods)):
                        last, lake = floods[i]
                        if lake in lakes:
                            ans[day] = lake
                            lakes.remove(lake)
                            floods.pop(i)
                            break
                continue

            if rain in lakes:
                return []
            lakes.add(rain)
            ans[day] = -1
        
        return ans

# 2nd solution
# O(n * log(n)) time | O(n) space
from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        st = SortedList()
        mp = {}
        for i, rain in enumerate(rains):
            if rain == 0:
                st.add(i)
            else:
                ans[i] = -1
                if rain in mp:
                    it = st.bisect(mp[rain])
                    if it == len(st):
                        return []
                    ans[st[it]] = rain
                    st.discard(st[it])
                mp[rain] = i
        return ans
    

# 3rd solution
# O(n) time | O(n) space
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        nxt = list(range(len(rains) + 1))
        pre = {}
        res = [1] * len(rains)

        def find(i):
            j = i if nxt[i] == i else find(nxt[i])
            nxt[i] = j + 1
            return j

        for i, a in enumerate(rains):
            if a == 0:
                continue

            nxt[i] = i + 1
            if a in pre:
                j = find(pre[a])
                if j > i:
                    return []
                res[j] = a
            
            res[i] = -1
            pre[a] = i
        
        return res