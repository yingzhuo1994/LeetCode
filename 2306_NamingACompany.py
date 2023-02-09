# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dic = defaultdict(set)
        for idea in ideas:
            dic[idea[1:]].add(idea[0])
        
        ans = 0
        keys = list(dic.keys())
        for i in range(len(keys)):
            for j in range(i):
                suffix1 = keys[i]
                suffix2 = keys[j]
                for ch1 in dic[suffix1]:
                    if ch1 in dic[suffix2]:
                        continue
                    for ch2 in dic[suffix2]:
                        if ch2 in dic[suffix1]:
                            continue
                        ans += 2
        return ans