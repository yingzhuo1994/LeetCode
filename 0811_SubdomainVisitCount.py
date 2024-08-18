# 1st solution
# O(n) time | O(n) space
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = {}
        for cpdomain in cpdomains:
            num, domain = cpdomain.split()
            num = int(num)
            lst = domain.split(".")
            for i in range(len(lst)):
                key = ".".join(lst[i:])
                cnt[key] = cnt.get(key, 0) + num
        return [f"{val} {key}" for key, val in cnt.items()]