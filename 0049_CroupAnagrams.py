class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1st soluton
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()