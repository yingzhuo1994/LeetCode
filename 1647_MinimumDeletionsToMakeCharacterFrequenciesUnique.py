# 1st solution
# O(n) time | O(1) space
class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        frequencies = {}
        for _, k in count.items():
            frequencies[k] = frequencies.get(k, 0) + 1
        
        nums = sorted(list(frequencies.keys()))
        i = len(nums) - 1
        ans = 0
        freq = nums[i]
        while freq > 0:
            if frequencies.get(freq, 0) > 1:
                diff = frequencies[freq] - 1
                frequencies[freq] = 1
                ans += diff
                frequencies[freq - 1] = frequencies.get(freq - 1, 0) + diff
                freq -= 1
            else:
                if i > 0:
                    freq = nums[i - 1]
                    i -= 1
                else:
                    break
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        freqs = list(count.values())
        freqs.sort()
        freqs.reverse()
        last = len(s) + 1
        ans = 0

        for freq in freqs:
            if freq < last:
                last = freq
            else:
                ans += freq - (last - 1)
                last = last - 1
            last = max(last, 1)
        
        return ans