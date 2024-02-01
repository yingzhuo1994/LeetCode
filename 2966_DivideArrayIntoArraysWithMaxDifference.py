# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        count = Counter(nums)
        keys = sorted(list(count.keys()))
        ans = []
        for i, key in enumerate(keys):
            if count[key] == 0:
                continue
            while count[key] >= 3:
                ans.append([key] * 3)
                count[key] -= 3
            if count[key] > 0:
                ans.append([key] * count[key])
                count[key] = 0
            if len(ans[-1]) < 3:
                last = ans[-1][0]
                j = i + 1
                while j < len(keys) and len(ans[-1]) < 3:
                    if count[keys[j]] > 0:
                        if keys[j] - last <= k:
                            ans[-1].append(keys[j])
                            count[keys[j]] -= 1
                            continue
                        else:
                            break
                    j += 1
                if len(ans[-1]) < 3:
                    return []
        return ans

            