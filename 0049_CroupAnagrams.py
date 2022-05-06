# O(n * k * log(k)) time | O(n) space
# where n is the length of strs, and k is the average length of each str.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            dic[tuple(sorted(s))].append(s)
        return dic.values()